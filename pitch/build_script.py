from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
B=lambda t:f'<font backColor="#FFF3B0" color="#B00020"><b>[ {t} ]</b></font>'
h=ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=14,textColor=HexColor('#0072BC'),spaceBefore=14,spaceAfter=4)
t=ParagraphStyle('t',fontName='Helvetica-Bold',fontSize=20,leading=26,textColor=HexColor('#0B2A4A'),spaceAfter=6)
n=ParagraphStyle('n',fontName='Helvetica-Oblique',fontSize=9,textColor=HexColor('#5B6B7A'),spaceAfter=6)
b=ParagraphStyle('b',fontName='Helvetica',fontSize=12,leading=18)
S=[("Slide 1 - Cover (~10 s)","Good morning. The person you need is already in the company. We present Synerg-IA: automatic prediction of high-performance teams."),
("Slide 2 - Problem & user (~20 s)",["Our user is a staffing manager with a non-technical background. We found four problems, and we divided them into four dimensions:","1) Lack of data standardization.","2) Lack of crucial information to make the decision.","3) Matching takes a lot of time, because there is too much information.","4) The reasons behind decisions are not clear."]),
("Slide 3 - Solution (~60 s)",["Our solution is a fully functional predictor of high-performance teams. It solves all four dimensions:","1) <b>Automated standardization</b> of all existing and new data.","2) <b>Complete profiles.</b> The company's surveys fill in each person's preferences and risks, to create high-performance, synergistic teams. A five-minute psychological test, based on Belbin's team roles, adds each person's psychological profile, so it is also taken into account.","3) <b>Plain-language prediction.</b> The manager only describes the needs of the project. The system asks for any missing data and proposes a team, with a synergy percentage.","4) <b>Explained decisions.</b> Every match is explained, so it is clear why each decision was made. You can change any decision manually, or ask for a different team. The human is always in control."]),
("Slide 4 - Viability & impact (~35 s)",["The MVP lasts six months. Each month, two members of our team give two full days to tune the algorithm with real data. That is 192 hours at 50 euros an hour: a total cost of 9,600 euros.","The return, as a hypothesis: we reduce staffing time by 80 percent. Every 40 hours a manager spends become just 8. At 75 euros an hour, that saves 2,400 euros per team, so the MVP pays back after just four teams. Plus higher productivity and fewer bench days: between 0.7 and 1.4 million euros a year per 1,000 people.","The impact: the right person, found inside the company, in minutes, with the reason why."]),
("Slide 5 - Evaluation & scalability (~30 s)",["We will test it on 5 pilot projects, and use three indicators to fine-tune the AI. Synergy gap: under 10 points. Performance: plus 10 percent versus teams staffed by hand. Time to staff: at least minus 50 percent.","After that, the AI keeps fine-tuning itself with the feedback of the managers, always comparing the same indicators. This makes it very easy to scale, because the system improves itself and the cost does not rise. And it gets better and better at predicting high-performance teams. Thank you."])]
d=SimpleDocTemplate('/mnt/project-files/pitch/NTTDATA_pitch_script.pdf',pagesize=A4,leftMargin=56,rightMargin=56,topMargin=50,bottomMargin=50,title='NTT DATA Pitch Script')
el=[Paragraph('Pitch script - 3 minutes',t),Paragraph('Target: 2.5 to 3 min (~145 wpm). All figures are hypotheses to validate with real data. Version 0.4',n)]
pt=ParagraphStyle('pt',parent=b,leftIndent=14,spaceBefore=5)
for a,x in S:
    el.append(Paragraph(a,h))
    xs=x if isinstance(x,list) else [x]
    for i,y in enumerate(xs): el.append(Paragraph(y,pt if i and len(xs)>1 else b))
d.build(el)
