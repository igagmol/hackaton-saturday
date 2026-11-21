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
("Slide 4 - Viability & impact (~30 s)",["The MVP is already built. A pilot would cost about 20,000 euros, as a hypothesis: two engineers for six weeks, plus around 500 euros a month for models and hosting. It pays back after roughly two avoided external hires, at about 10,000 euros each. Staffing a team drops from days to minutes. Hypothesis: one more point of utilization is worth about 700,000 euros a year per 1,000 people.","The impact: the right person, found inside the company, in minutes, with the reason why."]),
("Slide 5 - Evaluation, scaling & next steps (~50 s)",["We will test it on 5 pilot projects. Three indicators:","1) <b>Synergy gap.</b> Predicted team synergy versus the synergy members report after two months. Target: under 10 points.","2) <b>Performance.</b> Pilot teams versus similar teams staffed by hand, using the company's own reviews. Target: plus 10 percent.","3) <b>Time to staff.</b> Target: minus 80 percent.","All targets are hypotheses; we will replace them with the client's real data. If all three hit, we scale to more projects and departments.","Next steps: managers' feedback tunes the system, so each team costs less to build and our reach keeps growing."])]
d=SimpleDocTemplate('/mnt/project-files/pitch/NTTDATA_pitch_script.pdf',pagesize=A4,leftMargin=56,rightMargin=56,topMargin=50,bottomMargin=50,title='NTT DATA Pitch Script')
el=[Paragraph('Pitch script - 3 minutes',t),Paragraph('Target: about 420 words (3 min at ~140 wpm). Red/yellow [ blanks ] are still to fill in. Version 0.2 - figures marked as hypotheses',n)]
pt=ParagraphStyle('pt',parent=b,leftIndent=14,spaceBefore=5)
for a,x in S:
    el.append(Paragraph(a,h))
    xs=x if isinstance(x,list) else [x]
    for i,y in enumerate(xs): el.append(Paragraph(y,pt if i and len(xs)>1 else b))
d.build(el)
