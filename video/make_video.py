#!/usr/bin/env python3
"""Demo video pipeline: ElevenLabs TTS narration + screen recording + burned subtitles.

Usage:
  export ELEVENLABS_API_KEY=...            # never commit it
  python video/make_video.py voices                       # list voices (id, name)
  python video/make_video.py test --voice ID [--voice ID2] # 10 s sample per voice -> out/test_<name>.mp3
  python video/make_video.py build --recording demo.mp4 [--voice ID] [--script video/script.json] [--mock]

script.json: {"voice_id": "...", "segments": [{"start": 0.0, "text": "..."}, ...]}
  start = second in the recording where that line should begin.
--mock skips ElevenLabs (silent audio sized by word count) to test timing/assembly offline.
Stdlib only + ffmpeg/ffprobe on PATH.
"""
import argparse, hashlib, json, os, subprocess, sys, urllib.request, urllib.error
from pathlib import Path

API = "https://api.elevenlabs.io/v1"
MODEL = os.environ.get("ELEVENLABS_MODEL", "eleven_multilingual_v2")
OUT = Path(__file__).parent / "out"
TEST_TEXT = ("Every year, companies lose millions because the right people never meet the right projects. "
             "We built an AI that fixes that, in minutes, not months.")


def key():
    k = os.environ.get("ELEVENLABS_API_KEY")
    if not k:
        sys.exit("Set ELEVENLABS_API_KEY")
    return k


def api(path, body=None):
    req = urllib.request.Request(API + path, data=json.dumps(body).encode() if body else None,
                                 headers={"xi-api-key": key(), "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        sys.exit(f"ElevenLabs {e.code}: {e.read().decode()[:300]}")


def tts(text, voice, dest):
    audio = api(f"/text-to-speech/{voice}?output_format=mp3_44100_128", {
        "text": text, "model_id": MODEL,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True}})
    dest.write_bytes(audio)


def duration(f):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", str(f)]).decode().strip())


def run(cmd):
    print("+", " ".join(map(str, cmd))[:200])
    subprocess.run(cmd, check=True)


def ts(t):
    h, m = divmod(int(t), 3600)
    m, s = divmod(m, 60)
    return f"{h:02}:{m:02}:{s:02},{int((t % 1) * 1000):03}"


def srt_chunks(text, start, dur, max_words=9):
    """Split a segment into subtitle lines, timed proportionally to word count."""
    words = text.split()
    chunks = [words[i:i + max_words] for i in range(0, len(words), max_words)]
    t, out = start, []
    for c in chunks:
        d = dur * len(c) / len(words)
        out.append((t, t + d, " ".join(c)))
        t += d
    return out


def cmd_voices(a):
    for v in json.loads(api("/voices"))["voices"]:
        print(f'{v["voice_id"]}  {v["name"]:<25} {v.get("category", "")}  {v.get("labels", {})}')


def cmd_test(a):
    OUT.mkdir(exist_ok=True)
    for v in a.voice:
        f = OUT / f"test_{v}.mp3"
        tts(a.text or TEST_TEXT, v, f)
        print(f"{f}  ({duration(f):.1f}s)")


def cmd_build(a):
    OUT.mkdir(exist_ok=True)
    spec = json.loads(Path(a.script).read_text())
    voice = a.voice or spec.get("voice_id")
    if not a.mock and not voice:
        sys.exit("No voice: pass --voice or set voice_id in script.json")
    segs = sorted(spec["segments"], key=lambda s: s["start"])
    rec_len = duration(a.recording)
    clips, subs, warn = [], [], []
    for i, s in enumerate(segs):
        h = hashlib.sha1(f'{voice}|{MODEL}|{s["text"]}|{a.mock}'.encode()).hexdigest()[:10]
        f = OUT / f"seg{i:02}_{h}.mp3"
        if not f.exists():  # cache: only re-generate changed lines (saves credits)
            if a.mock:
                d = max(1.0, len(s["text"].split()) / 2.6)  # ~156 wpm
                run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
                     "-t", f"{d:.2f}", "-q:a", "9", str(f)])
            else:
                tts(s["text"], voice, f)
        d = duration(f)
        end = s["start"] + d
        nxt = segs[i + 1]["start"] if i + 1 < len(segs) else rec_len
        if end > nxt + 0.05:
            warn.append(f"seg {i} ends {end:.1f}s but next starts {nxt:.1f}s (overlap {end - nxt:.1f}s): shorten text or move start")
        clips.append((f, s["start"]))
        subs += srt_chunks(s["text"], s["start"], d)
    srt = OUT / "subtitles.srt"
    srt.write_text("\n".join(f"{n}\n{ts(b)} --> {ts(e)}\n{t}\n" for n, (b, e, t) in enumerate(subs, 1)))

    # narration track: each clip delayed to its start, mixed (no normalisation so levels stay intact)
    inputs, filt = [], []
    for n, (f, st) in enumerate(clips):
        inputs += ["-i", str(f)]
        ms = int(st * 1000)
        filt.append(f"[{n}:a]adelay={ms}|{ms},apad[a{n}]")
    mix = "".join(f"[a{n}]" for n in range(len(clips)))
    filt.append(f"{mix}amix=inputs={len(clips)}:normalize=0:duration=longest,atrim=0:{max(rec_len, end):.2f}[out]")
    narr = OUT / "narration.m4a"
    run(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", ";".join(filt), "-map", "[out]",
         "-c:a", "aac", "-b:a", "192k", str(narr)])

    final = Path(a.output)
    style = "FontName=Arial,FontSize=20,PrimaryColour=&H00FFFFFF,OutlineColour=&H80000000,BorderStyle=3,Outline=1,Shadow=0,MarginV=28"
    vf = f"subtitles={srt.as_posix()}:force_style='{style}'" if not a.no_subs else "null"
    # if narration outlasts the recording, freeze last frame
    pad = max(0.0, end - rec_len)
    if pad > 0:
        vf += f",tpad=stop_mode=clone:stop_duration={pad:.2f}"
    run(["ffmpeg", "-y", "-v", "error", "-i", str(a.recording), "-i", str(narr), "-map", "0:v:0", "-map", "1:a:0",
         "-vf", vf, "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
         "-c:a", "copy", "-shortest", "-movflags", "+faststart", str(final)])
    print(f"\nOK -> {final} ({duration(final):.1f}s)  subtitles: {srt}")
    for w in warn:
        print("WARN", w)


p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
sp = p.add_subparsers(dest="cmd", required=True)
sp.add_parser("voices").set_defaults(fn=cmd_voices)
t = sp.add_parser("test"); t.add_argument("--voice", action="append", required=True); t.add_argument("--text")
t.set_defaults(fn=cmd_test)
b = sp.add_parser("build")
b.add_argument("--recording", required=True)
b.add_argument("--script", default=str(Path(__file__).parent / "script.json"))
b.add_argument("--voice"); b.add_argument("--output", default=str(OUT / "demo_final.mp4"))
b.add_argument("--mock", action="store_true"); b.add_argument("--no-subs", action="store_true")
b.set_defaults(fn=cmd_build)
a = p.parse_args(); a.fn(a)
