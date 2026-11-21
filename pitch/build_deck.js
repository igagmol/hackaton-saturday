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
const DT=['Lack of data standardization','Lack of crucial information to make the decision','Matching takes a lot of time: too much information','Reasons behind decisions are not clear'];
dims.forEach(([x,y],i)=>{s.addShape(p.ShapeType.roundRect,{x,y,w:2.9,h:1.3,rectRadius:0.15,fill:{color:LIGHT},line:{color:BLUE,width:1.25}});
s.addText(DT[i],{x:x+0.15,y:y+0.1,w:2.6,h:1.1,fontFace:F,fontSize:18,bold:true,color:BLUE,align:'center',valign:'middle',margin:0,isTextBox:true});});
s.addShape(p.ShapeType.ellipse,{x:cx-0.6,y:cy-0.6,w:1.2,h:1.2,fill:{color:BLUE},line:{color:WHITE,width:3}});
s.addText('Staffing manager (non-technical)',{x:cx-0.6,y:cy-0.6,w:1.2,h:1.2,fontFace:F,fontSize:11,bold:true,color:WHITE,align:'center',valign:'middle',margin:0,isTextBox:true});
s.addShape(p.ShapeType.roundRect,{x:3.5,y:3.5,w:3,h:0.8,rectRadius:0.15,fill:{color:NAVY},line:{color:NAVY}});
s.addText('Matching people to projects is slow and opaque',{x:3.5,y:3.5,w:3,h:0.8,fontFace:F,fontSize:13,bold:true,color:WHITE,align:'center',valign:'middle',margin:0,isTextBox:true});
// 3 solution
s=p.addSlide();title(s,'The solution');
const INN=[['1  Automated standardization',''],['2  Complete profiles','Existing data · Preferences and risks · Psychological features'],['3  Plain-language prediction',''],['4  Explained decisions','']];
[[0.5,1.1],[5.1,1.1],[0.5,3.25],[5.1,3.25]].forEach(([x,y],i)=>{s.addShape(p.ShapeType.roundRect,{x,y,w:4.4,h:1.95,rectRadius:0.15,fill:{color:LIGHT},line:{color:BLUE,width:1.25}});
 const runs=[{text:INN[i][0],options:{fontSize:26,bold:true,color:BLUE,align:'center',breakLine:!!INN[i][1]}}];
 if(INN[i][1])runs.push({text:INN[i][1],options:{fontSize:16,color:NAVY,align:'center'}});
 s.addText(runs,{x:x+0.2,y:y+0.1,w:4,h:1.75,fontFace:F,align:'center',valign:'middle',margin:0,isTextBox:true});});
// 4 viability
s=p.addSlide();title(s,'Viability & impact');
s.addShape(p.ShapeType.roundRect,{x:0.5,y:1.1,w:4.4,h:4.1,rectRadius:0.15,fill:{color:LIGHT},line:{color:BLUE,width:1.25}});
s.addText('MVP cost',{x:0.7,y:1.2,w:4,h:0.4,fontFace:F,fontSize:20,bold:true,color:BLUE,margin:0,isTextBox:true});
[['Time','6-month MVP',''],['Cost','€9,600','192 h × €50/h'],['Human Resources','2 people × 2 full days per month',''],['Payback','After 4 teams staffed','']].forEach(([a,b,c],i)=>{
 const x=0.7+(i%2)*2.05,y=1.75+Math.floor(i/2)*1.7;
 s.addShape(p.ShapeType.roundRect,{x,y,w:1.9,h:1.5,rectRadius:0.12,fill:{color:WHITE},line:{color:BLUE,width:1}});
 s.addText(a,{x:x+0.1,y:y+0.1,w:1.7,h:0.3,fontFace:F,fontSize:14,bold:true,color:NAVY,margin:0,isTextBox:true});
 s.addText(b,{x:x+0.1,y:y+0.45,w:1.7,h:0.6,fontFace:F,fontSize:c?24:14,bold:!!c,color:c?BLUE:NAVY,margin:0,valign:'top',isTextBox:true});
 if(c)s.addText(c,{x:x+0.1,y:y+0.95,w:1.7,h:0.25,fontFace:F,fontSize:12,color:NAVY,margin:0,isTextBox:true});
 s.addText('hypothesis',{x:x+0.1,y:y+1.2,w:1.7,h:0.25,fontFace:F,fontSize:10,italic:true,color:GREY,margin:0,isTextBox:true});});
[['Revenue generation','+€0.7M–1.4M / year','per 1,000 people: 2–5 fewer bench days each (+1 to +2 pts utilization × €70k billing)'],['Time savings','€2,700 per team','40 h → 4 h of manager time, at €75/h (range €50–100)']].forEach(([a,b,c],i)=>{
 const y=1.1+i*2.1;
 s.addShape(p.ShapeType.roundRect,{x:5.1,y,w:4.4,h:1.95,rectRadius:0.15,fill:{color:NAVY},line:{color:NAVY}});
 s.addText(a,{x:5.3,y:y+0.15,w:4,h:0.35,fontFace:F,fontSize:16,bold:true,color:'BFD9EE',margin:0,isTextBox:true});
 s.addText(b,{x:5.3,y:y+0.6,w:4,h:0.7,fontFace:F,fontSize:30,bold:true,color:WHITE,margin:0,isTextBox:true});
 s.addText(c+' (hypothesis)',{x:5.3,y:y+1.35,w:4,h:0.5,fontFace:F,fontSize:12,italic:true,color:'BFD9EE',margin:0,valign:'top',isTextBox:true});});
// 5 eval + scale
s=p.addSlide();title(s,'Evaluation & scalability');
[['Synergy gap','<10 pts'],['Performance','+10%'],['Time to staff','−90%']].forEach(([k,v],i)=>{const y=1.1+i*1.4;
 s.addShape(p.ShapeType.roundRect,{x:0.5,y,w:4.5,h:1.3,rectRadius:0.15,fill:{color:LIGHT},line:{color:BLUE,width:1.25}});
 s.addText(k,{x:0.7,y:y+0.08,w:4.1,h:0.35,fontFace:F,fontSize:16,bold:true,color:NAVY,margin:0,isTextBox:true});
 s.addText(v,{x:0.7,y:y+0.45,w:4.1,h:0.6,fontFace:F,fontSize:36,bold:true,color:BLUE,margin:0,isTextBox:true});
 s.addText('target (hypothesis)',{x:0.7,y:y+1.02,w:4.1,h:0.25,fontFace:F,fontSize:11,italic:true,color:GREY,margin:0,isTextBox:true});});
s.addShape(p.ShapeType.roundRect,{x:5.2,y:1.1,w:4.3,h:4.1,rectRadius:0.15,fill:{color:NAVY},line:{color:NAVY}});
s.addText('How to scale',{x:5.4,y:1.2,w:4,h:0.4,fontFace:F,fontSize:20,bold:true,color:WHITE,margin:0,isTextBox:true});
[['1  Pilot','5 projects',1],['2  Expand','',1],['3  Next step','',2]].forEach(([a,b,n],i)=>{const y=1.75+i*1.1;
 s.addShape(p.ShapeType.roundRect,{x:5.4,y,w:3.9,h:0.95,rectRadius:0.12,fill:{color:BLUE},line:{color:BLUE}});
 s.addText(a,{x:5.55,y:y+0.08,w:3.6,h:0.3,fontFace:F,fontSize:16,bold:true,color:WHITE,margin:0,isTextBox:true});
 if(b)s.addText(b,{x:5.55,y:y+0.45,w:3.6,h:0.4,fontFace:F,fontSize:16,color:WHITE,margin:0,isTextBox:true});});
s.addText([{text:'Feedback refines the system',options:{bullet:true,breakLine:true}},{text:'Cost down, reach up',options:{bullet:true}}],{x:5.55,y:4.35,w:3.6,h:0.5,fontFace:F,fontSize:14,color:WHITE,margin:0,isTextBox:true,valign:'top'});
p.writeFile({fileName:'/mnt/project-files/pitch/NTTDATA_pitch_deck.pptx'}).then(()=>console.log('done'));
