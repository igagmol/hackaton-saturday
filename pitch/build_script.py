from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
B=lambda t:f'<font backColor="#FFF3B0" color="#B00020"><b>[ {t} ]</b></font>'
h=ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=14,textColor=HexColor('#0072BC'),spaceBefore=14,spaceAfter=4)
t=ParagraphStyle('t',fontName='Helvetica-Bold',fontSize=20,textColor=HexColor('#0B2A4A'),spaceAfter=4)
n=ParagraphStyle('n',fontName='Helvetica-Oblique',fontSize=9,textColor=HexColor('#5B6B7A'),spaceAfter=6)
b=ParagraphStyle('b',fontName='Helvetica',fontSize=12,leading=18)
S=[("Slide 1 - Cover (~10 s)",f"Good morning. The person you need is already in the company. We are the team from CDTM Valencia Hacks, and we present a marketplace for the automatic prediction of high-performance teams."),
("Slide 2 - Problem & user (~40 s)",f"We built this for a senior, non-technical staffing team. It sits inside HR, but it is not HR. Its only job is matching people to projects. They understand needs and strategy, not technology. The person we need is already in the company, but finding them is slow and unreliable. We found four dimensions. One: lack of standardization. Briefs and skills are described in different ways. Two: skills and people are hard to match to projects. Three: decisions are not explained. Managers get a name without the reason. Four: information is missing. Nobody sees the trade-offs between candidates."),
("Slide 3 - Solution (~55 s)",f"Our solution is {B('what it is')}. It is fully functional and already integrates {B('data sources')}. It solves the four dimensions in four steps. Interpret: {B('how')}. Match: {B('how')}. Explain: {B('how')}. Compare: {B('how')}. It is built for {B('user')} because {B('why it fits the user')}."),
("Slide 4 - Viability & impact (~55 s)",f"What does it cost? A validation MVP needs {B('time')}, {B('money')} and {B('other resources')}. The return: {B('X')} in talent productivity, {B('X')} in revenue generation and {B('X')} in time saved. Why is this real? {B('link between data and benefit')}. For the company, the impact is {B('impact')}."),
("Slide 5 - Evaluation & scalability (~40 s)",f"To measure success, in the MVP and in the long term, we use this dashboard. Three indicators matter most: {B('KPI 1')}, {B('KPI 2')} and {B('KPI 3')}. If they reach {B('thresholds')}, the pilot has succeeded. Then we scale: {B('how to scale')}. Thank you.")]
d=SimpleDocTemplate('/mnt/project-files/pitch/NTTDATA_pitch_script.pdf',pagesize=A4,leftMargin=56,rightMargin=56,topMargin=50,bottomMargin=50,title='NTT DATA Pitch Script')
el=[Paragraph('Pitch script - 3 minutes',t),Paragraph('Target: about 420 words (3 min at ~140 wpm). Red/yellow [ blanks ] are still to fill in. Version 0.1',n)]
for a,x in S: el+=[Paragraph(a,h),Paragraph(x,b)]
d.build(el)
