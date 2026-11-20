from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
B=lambda t:f'<font backColor="#FFF3B0" color="#B00020"><b>[ {t} ]</b></font>'
h=ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=14,textColor=HexColor('#0072BC'),spaceBefore=14,spaceAfter=4)
t=ParagraphStyle('t',fontName='Helvetica-Bold',fontSize=20,textColor=HexColor('#0B2A4A'),spaceAfter=4)
n=ParagraphStyle('n',fontName='Helvetica-Oblique',fontSize=9,textColor=HexColor('#5B6B7A'),spaceAfter=6)
b=ParagraphStyle('b',fontName='Helvetica',fontSize=12,leading=18)
S=[("Slide 1 - Cover (~10 s)",f"Good morning. {B('SLOGAN')}. We are {B('team / product name')}."),
("Slide 2 - Problem & user (~35 s)",f"The problem we identified is {B('main problem')}. We are building for {B('user')}. We found four dimensions of this problem. One: {B('dimension 1')}. Two: {B('dimension 2')}. Three: {B('dimension 3')}. Four: {B('dimension 4')}."),
("Slide 3 - Solution (~55 s)",f"Our solution is {B('what it is')}. It is fully functional and already integrates {B('data sources')}. It solves the four dimensions with four innovations: {B('innovation 1')}, {B('innovation 2')}, {B('innovation 3')} and {B('innovation 4')}. It is built for {B('user')} because {B('why it fits the user')}."),
("Slide 4 - Viability & impact (~55 s)",f"What does it cost? A validation MVP needs {B('time')}, {B('money')} and {B('other resources')}. The return: {B('X')} in talent productivity, {B('X')} in revenue generation and {B('X')} in time saved. Why is this real? {B('link between data and benefit')}. For the company, the impact is {B('impact')}."),
("Slide 5 - Evaluation & scalability (~40 s)",f"To measure success, in the MVP and in the long term, we use this dashboard. Three indicators matter most: {B('KPI 1')}, {B('KPI 2')} and {B('KPI 3')}. If they reach {B('thresholds')}, the pilot has succeeded. Then we scale: {B('how to scale')}. Thank you.")]
d=SimpleDocTemplate('/mnt/project-files/pitch/NTTDATA_pitch_script.pdf',pagesize=A4,leftMargin=56,rightMargin=56,topMargin=50,bottomMargin=50,title='NTT DATA Pitch Script')
el=[Paragraph('Pitch script - 3 minutes',t),Paragraph('Target: about 420 words (3 min at ~140 wpm). Red/yellow [ blanks ] are still to fill in. Version 0.1',n)]
for a,x in S: el+=[Paragraph(a,h),Paragraph(x,b)]
d.build(el)
