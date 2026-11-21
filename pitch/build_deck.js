const pptxgen=require('pptxgenjs');
const p=new pptxgen();p.layout='LAYOUT_16x9';p.title='NTT DATA Hackathon Deck';
const BLUE='0072BC',NAVY='0B2A4A',LIGHT='E8F3FA',GREY='5B6B7A',WHITE='FFFFFF',AC='00A3E0';
const F='Calibri';
function logo(s,dark){if(dark)s.addShape(p.ShapeType.roundRect,{x:7.65,y:0.15,w:2.1,h:0.6,rectRadius:0.1,fill:{color:WHITE},line:{color:WHITE}});
s.addImage({path:'logo.png',x:7.8,y:0.25,w:1.8,h:0.37,objectName:'NTT DATA logo',altText:'NTT DATA logo'});}
function title(s,t){s.background={color:WHITE};logo(s,false);s.addText(t,{x:0.5,y:0.25,w:7,h:0.6,fontFace:F,fontSize:30,bold:true,color:NAVY,margin:0,isTextBox:true});}
function ph(s,t,o){s.addText(t,Object.assign({fontFace:F,fontSize:14,italic:true,color:GREY,margin:4,isTextBox:true,valign:'middle'},o));}
function box(s,x,y,w,h,head,ph_,fill,hc){s.addShape(p.ShapeType.roundRect,{x,y,w,h,rectRadius:0.15,fill:{color:fill||LIGHT},line:{color:BLUE,width:1.25}});
 s.addText(head,{x:x+0.15,y:y+0.1,w:w-0.3,h:0.35,fontFace:F,fontSize:14,bold:true,color:hc||BLUE,margin:0,isTextBox:true});
 ph(s,ph_,{x:x+0.15,y:y+0.45,w:w-0.3,h:h-0.55,valign:'top',margin:0});}
// 1 cover
let s=p.addSlide();s.background={color:NAVY};logo(s,true);
s.addText('CDTM Valencia Hacks',{x:0.6,y:0.9,w:6,h:0.4,fontFace:F,fontSize:18,bold:true,color:AC,margin:0,isTextBox:true});
s.addText('Marketplace for the Automatic Prediction of High-Performance Teams',{x:0.6,y:1.4,w:8.8,h:1.7,fontFace:F,fontSize:40,bold:true,color:WHITE,margin:0,isTextBox:true,valign:'middle'});
s.addText('The person you need is already in the company',{x:0.6,y:3.2,w:8.8,h:0.5,fontFace:F,fontSize:20,italic:true,color:'BFD9EE',margin:0,isTextBox:true});
s.addText('Sarah Vasquez  ·  José Antonio Calamardo Manrique  ·  Ignacio Aguera Molto\nDavid García Carrión  ·  Damián Lorca Andría',{x:0.6,y:4.3,w:8.8,h:0.8,fontFace:F,fontSize:14,color:WHITE,margin:0,isTextBox:true,valign:'top',paraSpaceAfter:4});
// 2 problem
s=p.addSlide();title(s,'The problem');
const cx=5,cy=2.75;
[[3.4,2.0,0],[6.6,2.0,1],[3.4,4.3,1],[6.6,4.3,0]].forEach(([x,y,fv])=>s.addShape(p.ShapeType.line,{x:Math.min(cx,x),y:Math.min(cy,y),w:Math.abs(x-cx),h:Math.abs(y-cy),flipV:!!fv,line:{color:BLUE,width:2}}));
const dims=[[0.5,1.0],[6.6,1.0],[0.5,3.9],[6.6,3.9]];
const DT=[['1 · Data','Lack of automatic standardization of the data'],['2 · Fit','Lack of important information to better relocate human resources where they will work best'],['3 · Matching','It takes a lot of time to make the best match because of lots of information'],['4 · Decisions','Managers cannot see why a decision was made']];
dims.forEach(([x,y],i)=>{s.addShape(p.ShapeType.roundRect,{x,y,w:2.9,h:1.3,rectRadius:0.15,fill:{color:LIGHT},line:{color:BLUE,width:1.25}});
s.addText(DT[i][0],{x:x+0.15,y:y+0.1,w:2.6,h:0.35,fontFace:F,fontSize:14,bold:true,color:BLUE,margin:0,isTextBox:true});
s.addText(DT[i][1],{x:x+0.15,y:y+0.5,w:2.6,h:0.7,fontFace:F,fontSize:14,color:NAVY,margin:0,valign:'top',isTextBox:true});});
s.addShape(p.ShapeType.ellipse,{x:cx-0.6,y:cy-0.6,w:1.2,h:1.2,fill:{color:BLUE},line:{color:WHITE,width:3}});
s.addText('Staffing manager (non-technical)',{x:cx-0.6,y:cy-0.6,w:1.2,h:1.2,fontFace:F,fontSize:11,bold:true,color:WHITE,align:'center',valign:'middle',margin:0,isTextBox:true});
s.addShape(p.ShapeType.roundRect,{x:3.5,y:3.5,w:3,h:0.8,rectRadius:0.15,fill:{color:NAVY},line:{color:NAVY}});
s.addText('Matching people to projects is slow and opaque',{x:3.5,y:3.5,w:3,h:0.8,fontFace:F,fontSize:13,bold:true,color:WHITE,align:'center',valign:'middle',margin:0,isTextBox:true});
// 3 solution
s=p.addSlide();title(s,'The solution');
const INN=[['1 · Automated standardization','All existing and new data standardized automatically'],['2 · Complete profiles','Surveys fill preferences & risks; a 5-minute psychological test'],['3 · Plain-language prediction','Describe the need in plain words; the system asks for missing data and predicts the top team'],['4 · Explained decisions','Humans decide and add people; every match explained in natural language']];
[[0.5,1.1],[3.6,1.1],[0.5,3.25],[3.6,3.25]].forEach(([x,y],i)=>box(s,x,y,2.9,1.95,INN[i][0],INN[i][1]));
s.addShape(p.ShapeType.roundRect,{x:6.7,y:1.1,w:2.8,h:2.55,rectRadius:0.15,fill:{color:NAVY},line:{color:NAVY}});
s.addText('How it works',{x:6.85,y:1.2,w:2.5,h:0.35,fontFace:F,fontSize:14,bold:true,color:WHITE,margin:0,isTextBox:true});
s.addText('Standardized data + surveys (preferences & risks) + 5-min psychological test predict the top team. Plain-language input, human decides, explanations in natural language.',{x:6.85,y:1.6,w:2.5,h:1.9,fontFace:F,fontSize:14,color:WHITE,margin:0,valign:'top',isTextBox:true});
box(s,6.7,3.85,2.8,1.35,'Why it is perfect for [ user ]','[ one-line recap ]');
// 4 viability
s=p.addSlide();title(s,'Viability & impact');
s.addShape(p.ShapeType.roundRect,{x:0.5,y:1.1,w:4.4,h:4.1,rectRadius:0.15,fill:{color:LIGHT},line:{color:BLUE,width:1.25}});
s.addText('MVP cost',{x:0.7,y:1.2,w:4,h:0.4,fontFace:F,fontSize:20,bold:true,color:BLUE,margin:0,isTextBox:true});
[['Time','[ hours / weeks ]'],['Money','[ € ]'],['Resources','[ people / tools / data ]'],['Total','[ € + time ]']].forEach(([a,b],i)=>{
 const x=0.7+(i%2)*2.05,y=1.75+Math.floor(i/2)*1.7;
 s.addShape(p.ShapeType.roundRect,{x,y,w:1.9,h:1.5,rectRadius:0.12,fill:{color:WHITE},line:{color:BLUE,width:1}});
 s.addText(a,{x:x+0.1,y:y+0.1,w:1.7,h:0.3,fontFace:F,fontSize:14,bold:true,color:NAVY,margin:0,isTextBox:true});
 ph(s,b,{x:x+0.1,y:y+0.45,w:1.7,h:0.95,valign:'top',margin:0,fontSize:16});});
[['Revenue generation','[ € / year ]'],['Time savings','[ hours / year ]'],['Talent','[ productivity % ]']].forEach(([a,b],i)=>{
 const y=1.1+i*1.4;
 s.addShape(p.ShapeType.roundRect,{x:5.1,y,w:4.4,h:1.3,rectRadius:0.15,fill:{color:NAVY},line:{color:NAVY}});
 s.addText(a,{x:5.3,y:y+0.1,w:4,h:0.3,fontFace:F,fontSize:14,bold:true,color:'BFD9EE',margin:0,isTextBox:true});
 s.addText(b,{x:5.3,y:y+0.5,w:4,h:0.7,fontFace:F,fontSize:30,bold:true,italic:true,color:WHITE,margin:0,isTextBox:true});});
// 5 eval + scale
s=p.addSlide();title(s,'Evaluation & scalability');
s.addShape(p.ShapeType.roundRect,{x:0.5,y:1.1,w:4.5,h:4.1,rectRadius:0.15,fill:{color:LIGHT},line:{color:BLUE,width:1.25}});
s.addText('Dashboard',{x:0.7,y:1.2,w:4,h:0.4,fontFace:F,fontSize:20,bold:true,color:BLUE,margin:0,isTextBox:true});
[1,2,3].forEach(i=>{const x=0.7+(i-1)*1.4;
 s.addShape(p.ShapeType.roundRect,{x,y:1.75,w:1.3,h:1.2,rectRadius:0.1,fill:{color:WHITE},line:{color:BLUE,width:1}});
 s.addText('KPI '+i,{x:x+0.08,y:1.8,w:1.15,h:0.3,fontFace:F,fontSize:12,bold:true,color:NAVY,margin:0,isTextBox:true});
 ph(s,'[ value + unit ]',{x:x+0.08,y:2.15,w:1.15,h:0.7,fontSize:14,valign:'top',margin:0});});
s.addShape(p.ShapeType.roundRect,{x:0.7,y:3.15,w:4.1,h:1.9,rectRadius:0.1,fill:{color:WHITE},line:{color:BLUE,width:1,dashType:'dash'}});
ph(s,'[ dashboard screenshot / chart ]',{x:0.7,y:3.15,w:4.1,h:1.9,align:'center'});
s.addShape(p.ShapeType.roundRect,{x:5.2,y:1.1,w:4.3,h:4.1,rectRadius:0.15,fill:{color:NAVY},line:{color:NAVY}});
s.addText('How to scale',{x:5.4,y:1.2,w:4,h:0.4,fontFace:F,fontSize:20,bold:true,color:WHITE,margin:0,isTextBox:true});
[['1  Pilot','[ scope · KPI threshold ]'],['2  Expand','[ teams / countries ]'],['3  Enterprise','[ full rollout · APIs ]']].forEach(([a,b],i)=>{const y=1.75+i*1.1;
 s.addShape(p.ShapeType.roundRect,{x:5.4,y,w:3.9,h:0.95,rectRadius:0.12,fill:{color:BLUE},line:{color:BLUE}});
 s.addText(a,{x:5.55,y:y+0.08,w:3.6,h:0.3,fontFace:F,fontSize:14,bold:true,color:WHITE,margin:0,isTextBox:true});
 s.addText(b,{x:5.55,y:y+0.42,w:3.6,h:0.45,fontFace:F,fontSize:14,italic:true,color:'DCEBF7',margin:0,isTextBox:true});});
p.writeFile({fileName:'/mnt/project-files/pitch/NTTDATA_pitch_deck.pptx'}).then(()=>console.log('done'));
