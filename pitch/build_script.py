from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
B=lambda t:f'<font backColor="#FFF3B0" color="#B00020"><b>[ {t} ]</b></font>'
h=ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=14,textColor=HexColor('#0072BC'),spaceBefore=14,spaceAfter=4)
t=ParagraphStyle('t',fontName='Helvetica-Bold',fontSize=20,leading=26,textColor=HexColor('#0B2A4A'),spaceAfter=6)
n=ParagraphStyle('n',fontName='Helvetica-Oblique',fontSize=9,textColor=HexColor('#5B6B7A'),spaceAfter=6)
b=ParagraphStyle('b',fontName='Helvetica',fontSize=12,leading=18)
S=[("Slide 1 - Cover (~10 s)","Good morning. The person you need is already in the company. We present a system for the automatic prediction of high-performance teams."),
("Slide 2 - Problem & user (~20 s)",["Our user is a staffing manager with a non-technical background. We found four problems:","1) Lack of data standardization.","2) Lack of crucial information to make the decision.","3) Matching takes a lot of time, because there is too much information.","4) The reasons behind decisions are not clear."]),
("Slide 3 - Solution (~50 s)",["Our solution is a fully functional predictor of high-performance teams. It solves all four problems:","1) <b>Automated standardization</b> of all existing and new data.","2) <b>Complete profiles.</b> Surveys fill in preferences and risks, and a five-minute psychological test, based on Belbin's team roles, adds psychological features.","3) <b>Plain-language prediction.</b> The manager describes the need; the system asks for any missing data and proposes a team.","4) <b>Explained decisions.</b> Every match is explained in plain language, and the final decision is always human."]),
("Slide 4 - Viability & impact (~30 s)",["The MVP lasts six months. Each month, two team members give two full days to tune the algorithm with real data. That is 192 hours at 50 euros an hour: a total cost of 9,600 euros.","Return, as hypotheses: staffing a team drops from 40 hours of manager time to 4. At 75 euros an hour, that saves 2,700 euros per team. The MVP pays back after just four teams. Fewer bench days add 0.7 to 1.4 million euros a year per 1,000 people.","The impact: the right person, found inside the company, in minutes, with the reason why."]),
("Slide 5 - Evaluation & scalability (~30 s)",["We test it on 5 pilot projects and measure three things. Synergy gap: predicted versus perceived synergy after two months, under 10 points. Performance: plus 10 percent versus teams staffed by hand. Time to staff: minus 90 percent. These targets are hypotheses; we replace them with real data.","Then we expand. Next step: managers' feedback refines the system, so cost goes down and reach goes up. Thank you."])]
d=SimpleDocTemplate('/mnt/project-files/pitch/NTTDATA_pitch_script.pdf',pagesize=A4,leftMargin=56,rightMargin=56,topMargin=50,bottomMargin=50,title='NTT DATA Pitch Script')
el=[Paragraph('Pitch script - 3 minutes',t),Paragraph('Target: about 350 words (2.5 min at ~145 wpm). All figures are hypotheses to validate with real data. Version 0.3',n)]
pt=ParagraphStyle('pt',parent=b,leftIndent=14,spaceBefore=5)
for a,x in S:
    el.append(Paragraph(a,h))
    xs=x if isinstance(x,list) else [x]
    for i,y in enumerate(xs): el.append(Paragraph(y,pt if i and len(xs)>1 else b))
d.build(el)
