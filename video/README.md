# Vídeo demo (ElevenLabs + ffmpeg)

1. Grabar la demo en pantalla **sin audio** (1080p, MP4/MOV).
2. Editar `script.json`: cada frase con su `start` (segundo de la grabación). ~2,6 palabras/s.
3. `export ELEVENLABS_API_KEY=...` (nunca al repo).
4. `python video/make_video.py voices` → elegir voz · `test --voice ID` → muestra de 10 s.
5. `python video/make_video.py build --recording demo.mp4 --voice ID` → `video/out/demo_final.mp4` (voz + subtítulos quemados + `subtitles.srt`).

- `--mock`: sin ElevenLabs (audio mudo) para probar tiempos gratis.
- Solo regenera frases cambiadas (caché por hash) → ahorra créditos.
- Avisa si una frase se solapa con la siguiente; si la voz dura más que la grabación, congela el último frame.
- Requisitos: Python 3 (stdlib) + ffmpeg con libass.
