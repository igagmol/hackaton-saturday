from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
B=lambda t:f'<font backColor="#FFF3B0" color="#B00020"><b>[ {t} ]</b></font>'
h=ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=14,textColor=HexColor('#0072BC'),spaceBefore=14,spaceAfter=4)
t=ParagraphStyle('t',fontName='Helvetica-Bold',fontSize=20,leading=26,textColor=HexColor('#0B2A4A'),spaceAfter=6)
n=ParagraphStyle('n',fontName='Helvetica-Oblique',fontSize=9,textColor=HexColor('#5B6B7A'),spaceAfter=6)
b=ParagraphStyle('b',fontName='Helvetica',fontSize=12,leading=18)
S=[("Slide 1 - Cover (~10 s)","Good morning. The person you need is already in the company. We want to present a system for the automatic prediction of high-performance teams."),
("Slide 2 - Problem & user (~25 s)",["The problem we identified, for a staffing manager with a non-technical background, is that finding the right person is slow and unreliable. It has four dimensions:","1) Lack of automatic standardization of the data.","2) Lack of important information to better relocate human resources where they will work best.","3) It takes a lot of time to make the best match because of lots of information.","4) Managers cannot see why a decision was made."]),
("Slide 3 - Solution (~60 s)",["Our solution is a fully functional predictor of high-performance team combinations. It solves all four dimensions of the problem:","1) <b>Automated standardization.</b> We automated the standardization of all existing data, and of any new data we add.","2) <b>Complete profiles.</b> Two more datasets complete the data. The company's satisfaction and performance surveys automatically fill a preferences-and-risks dataset: each person's work preferences, and the opportunity cost for the team they would leave, if any. And a five-minute psychological test, based on Belbin's team-role research and studies of high-performance teams, predicts the best-performing team.","3) <b>Plain-language prediction.</b> The user only describes the needs of a new or existing team in plain language. The system asks for any missing data and proposes a high-performance team.","4) <b>Explained decisions.</b> The final decision is always human: they can ask for winning combinations and add people manually. Every synergy and match decision is explained in natural language."]),
("Slide 4 - Viability & impact (~55 s)",f"What does it cost? A validation MVP needs {B('time')}, {B('money')} and {B('other resources')}. The return: {B('X')} in talent productivity, {B('X')} in revenue generation and {B('X')} in time saved. Why is this real? {B('link between data and benefit')}. For the company, the impact is {B('impact')}."),
("Slide 5 - Evaluation & scalability (~40 s)",f"To measure success, in the MVP and in the long term, we use this dashboard. Three indicators matter most: {B('KPI 1')}, {B('KPI 2')} and {B('KPI 3')}. If they reach {B('thresholds')}, the pilot has succeeded. Then we scale: {B('how to scale')}. Thank you.")]
d=SimpleDocTemplate('/mnt/project-files/pitch/NTTDATA_pitch_script.pdf',pagesize=A4,leftMargin=56,rightMargin=56,topMargin=50,bottomMargin=50,title='NTT DATA Pitch Script')
el=[Paragraph('Pitch script - 3 minutes',t),Paragraph('Target: about 420 words (3 min at ~140 wpm). Red/yellow [ blanks ] are still to fill in. Version 0.1',n)]
pt=ParagraphStyle('pt',parent=b,leftIndent=14,spaceBefore=5)
for a,x in S:
    el.append(Paragraph(a,h))
    xs=x if isinstance(x,list) else [x]
    for i,y in enumerate(xs): el.append(Paragraph(y,pt if i and len(xs)>1 else b))
d.build(el)
