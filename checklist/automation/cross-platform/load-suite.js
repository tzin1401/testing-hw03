/* Load and adapt the existing Chrome suite without changing Chrome artifacts.
 * Expectations and 79 test bodies come from run-chrome.spec.js at execution time.
 */
const fs=require('fs'),path=require('path'),Module=require('module');
module.exports=function(platform){
 const source=path.resolve(__dirname,'../run-chrome.spec.js');let s=fs.readFileSync(source,'utf8');
 s=s.replace("require('@playwright/test')","require('./cross-platform/cross-fixtures')");
 s=s.replace("const items=require('./items.json');",`const items=require('./items.json');\nconst platform=${JSON.stringify(platform)};\nconst hooks=require('./cross-platform/cross-helpers');`);
 s=s.replace("path.join(__dirname,'execution-results.json')",`path.join(__dirname,'cross-platform','${platform}-results.json')`);
 s=s.replace('await page.goto(route)','await page.goto(new URL(route,\'http://localhost:5173\').href)');

 const start=s.indexOf('  async function shot(selector){'),end=s.indexOf('  async function check(',start);
 s=s.slice(0,start)+`  async function shot(selector){if(screenshot)return;screenshot=await hooks.evidence(page,platform,id,account,selector);}\n`+s.slice(end);
 s=s.replace("let manual='';","let manual='';let notApplicable='';");
 const envStart=s.indexOf("   fs.writeFileSync(path.join(__dirname,'environment.json')"),envEnd=s.indexOf('\n   switch(id)',envStart);
 s=s.slice(0,envStart)+`   fs.writeFileSync(path.join(__dirname,'cross-platform',platform+'-environment.json'),JSON.stringify({os:os.type()+' '+os.release(),browser:browser.version(),playwright:require('@playwright/test/package.json').version,executedAt:new Date().toISOString(),viewport:await page.evaluate(()=>({width:innerWidth,height:innerHeight,dpr:devicePixelRatio})),platform},null,2));\n`+s.slice(envEnd);
 s=s.replace("manual='MANUAL: Cần kiểm mắt focus ring", "manual='MANUAL: Cần kiểm mắt focus ring").replace('computed outline auto/native của Chrome','computed outline auto/native của Firefox');
 // Firefox doesn't expose Chromium clipboard permission strings. Its browser prefs enable read/write for testing; actual copy uses mouse + Control+C.
 // Exercise reverse focus inside the form. Sending page keyboard events after Tab has
 // moved into Firefox browser chrome is not a reliable simulation of native Shift+Tab.
 const tabStart=s.indexOf("    case 'IA-01-15':"),tabEnd=s.indexOf("    case 'IA-01-16':",tabStart);
 let tabCase=s.slice(tabStart,tabEnd);
 tabCase=tabCase.replace("await page.keyboard.press('Tab');}await page.keyboard.press('Shift+Tab');","if(i<3)await page.keyboard.press('Tab');}await page.keyboard.press('Shift+Tab');await page.keyboard.press('Tab');");
 s=s.slice(0,tabStart)+tabCase+s.slice(tabEnd);
 if(platform==='firefox'){
  s=s.replace("throw Error('Mouse copy did not select exact OTP: '+JSON.stringify(copied))","throw Error('Clipboard Firefox chưa xác minh được: selected='+await page.evaluate(()=>getSelection().toString())+'; clipboard='+JSON.stringify(copied)+'; cần kiểm Copy/Paste native bằng tay')");
  const cs=s.indexOf("    case 'IA-04-19':"),ce=s.indexOf("    case 'IA-04-21':",cs);
  let c=s.slice(cs,ce);c=c.replace('const copied=await copyOtp();await check(',`const copied=await copyOtp();if(copied!==otp)throw Error('Firefox clipboard automation unavailable: selection='+await page.evaluate(()=>getSelection().toString())+' but clipboard='+JSON.stringify(copied)+'; cần kiểm Copy/Paste native bằng tay');await check(`);
  s=s.slice(0,cs)+c+s.slice(ce);
 }
 if(platform==='firefox')s=s.replace('await page.keyboard.press(\'Control+C\');','await page.bringToFront();await page.keyboard.press(\'Control+C\');');
 if(platform==='androidchrome'){
  s=s.replaceAll('submit().click()', 'hooks.tap(page,submit())');
  const prefix=`\n   const mobileNA={'IA-01-14':'Tab order phụ thuộc bàn phím vật lý; emulator dùng bàn phím cảm ứng.', 'IA-01-15':'Tab/Shift+Tab và focus trap theo bàn phím vật lý không áp dụng cho thao tác touch.', 'IA-01-16':'Focus ring khi Tab không áp dụng cho thiết bị touch không gắn bàn phím.', 'IA-01-17':'Zoom 200% bằng viewport desktop 640x400 không áp dụng cho màn hình Pixel_9 thật; không đổi viewport.', 'IA-01-19':'Phép kiểm đúng 320 CSS px không áp dụng cho viewport thật 412 CSS px; không resize hoặc giả lập viewport.'};\n   if(mobileNA[id]){notApplicable='N/A: '+mobileNA[id];notes.push(notApplicable);method='Đánh giá phạm vi trên Pixel_9 touch';}\n   else `;
  s=s.replace('   switch(id){',prefix+'switch(id){');
  s=s.replace('Math.abs(s.x+s.w/2-640)<1','Math.abs(s.x+s.w/2-(mobileWidth/2))<1');
  s=s.replace("case 'IA-01-09':{method=", "case 'IA-01-09':{const mobileWidth=await page.evaluate(()=>innerWidth);method=");
  s=s.replace("case 'IA-01-13':{method=", "case 'IA-01-13':{const mobileWidth=await page.evaluate(()=>innerWidth);method=").replace('n.right<=1280','n.right<=mobileWidth');
  s=s.replace('await submit().dblclick({delay:35})','await hooks.doubleTap(page,submit(),35)').replace('await submit().dblclick({delay:30})','await hooks.doubleTap(page,submit(),30)');
  s=s.replaceAll('const copied=await copyOtp()','const copied=await hooks.copyOtpMobile(page)');
  s=s.replace("await page.keyboard.press('Control+V')","await hooks.pasteMobile(page,fields().first())");
  s=s.replace("method='Clipboard copy code; Ctrl+V với spaces rồi reset'","method='Long-press Copy OTP; native Paste với spaces rồi reset'");
  s=s.replace("method='Kéo chọn chữ số OTP bằng mouse; Ctrl+C; đọc clipboard thật'","method='Long-press số OTP; toolbar Copy Android; đọc clipboard thật'");
  s=s.replace("method='Fast double-click OTP;", "method='Fast double-tap OTP;");
 }
 s=s.replace("const result=failed?'Failed':manual?'MANUAL':'Passed';","const result=failed?'Failed':notApplicable?'N/A':manual?'MANUAL':'Passed';");
 s=s.replace("screenshot,email:account.email", "platform,incomplete:!!manual&&failed,screenshot,email:account.email");
 // Compile as a sibling module so every existing relative import keeps working.
 const filename=path.join(path.dirname(source),'run-'+platform+'-shared.cjs');const m=new Module(filename,module);m.filename=filename;m.paths=Module._nodeModulePaths(path.dirname(source));m._compile(s,filename);
};
