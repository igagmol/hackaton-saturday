from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
B=lambda t:f'<font backColor="#FFF3B0" color="#B00020"><b>[ {t} ]</b></font>'
h=ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=14,textColor=HexColor('#0072BC'),spaceBefore=14,spaceAfter=4)
t=ParagraphStyle('t',fontName='Helvetica-Bold',fontSize=20,textColor=HexColor('#0B2A4A'),spaceAfter=4)
n=ParagraphStyle('n',fontName='Helvetica-Oblique',fontSize=9,textColor=HexColor('#5B6B7A'),spaceAfter=6)
b=ParagraphStyle('b',fontName='Helvetica',fontSize=12,leading=18)
S=[("Slide 1 - Cover (~10 s)","Good morning. The person you need is already in the company. We want to present a system for the automatic prediction of high-performance teams."),
("Slide 2 - Problem & user (~25 s)","The problem we identified is that finding the right person is slow and unreliable. It has four dimensions. 1) Lack of automatic standardization of the data. 2) Lack of important information to better relocate human resources where they will work best. 3) It takes a lot of time to make the best match because of lots of information. 4) Managers cannot see why a decision was made. Our user: senior non-technical staffing managers."),
("Slide 3 - Solution (~55 s)",f"Our solution is {B('what it is')}. It is fully functional and already integrates {B('data sources')}. It solves the four dimensions in four steps. Interpret: {B('how')}. Match: {B('how')}. Explain: {B('how')}. Compare: {B('how')}. It is built for {B('user')} because {B('why it fits the user')}."),
("Slide 4 - Viability & impact (~55 s)",f"What does it cost? A validation MVP needs {B('time')}, {B('money')} and {B('other resources')}. The return: {B('X')} in talent productivity, {B('X')} in revenue generation and {B('X')} in time saved. Why is this real? {B('link between data and benefit')}. For the company, the impact is {B('impact')}."),
("Slide 5 - Evaluation & scalability (~40 s)",f"To measure success, in the MVP and in the long term, we use this dashboard. Three indicators matter most: {B('KPI 1')}, {B('KPI 2')} and {B('KPI 3')}. If they reach {B('thresholds')}, the pilot has succeeded. Then we scale: {B('how to scale')}. Thank you.")]
d=SimpleDocTemplate('/mnt/project-files/pitch/NTTDATA_pitch_script.pdf',pagesize=A4,leftMargin=56,rightMargin=56,topMargin=50,bottomMargin=50,title='NTT DATA Pitch Script')
el=[Paragraph('Pitch script - 3 minutes',t),Paragraph('Target: about 420 words (3 min at ~140 wpm). Red/yellow [ blanks ] are still to fill in. Version 0.1',n)]
for a,x in S: el+=[Paragraph(a,h),Paragraph(x,b)]
d.build(el)
