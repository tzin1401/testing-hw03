const fs=require('fs'),path=require('path');const {execFileSync}=require('child_process');
const root=path.resolve(__dirname,'../../..');const out=path.join(root,'screenshots/cross-platform');
const ADB='/home/zinn/Android/Sdk/platform-tools/adb';
const wait=ms=>new Promise(r=>setTimeout(r,ms));
function adb(args){return execFileSync(ADB,['-s','emulator-5554',...args],{timeout:20000});}
async function overlay(page,label){await page.evaluate(label=>{document.getElementById('execution-evidence')?.remove();const e=document.createElement('div');e.id='execution-evidence';e.style.cssText='position:fixed;bottom:8px;right:8px;z-index:99999;background:#ff0;color:#000;padding:4px 8px;font:bold 13px sans-serif';e.textContent='23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · '+label+' · '+location.href;document.body.append(e);const v=visualViewport;if(v){e.style.maxWidth=Math.max(100,v.width-16)+'px';const b=e.getBoundingClientRect();const dx=Math.max(0,b.right-(v.offsetLeft+v.width-8)),dy=Math.max(0,b.bottom-(v.offsetTop+v.height-8));e.style.transform='translate('+(-dx)+'px,'+(-dy)+'px)';}},label);}
async function snapshot(page){return page.evaluate(()=>({url:location.href,token:localStorage.getItem('token'),fields:[...document.querySelectorAll('main form input,main form textarea')].map(e=>({value:e.value,type:e.type,disabled:e.disabled})),otp:/Mã OTP của bạn là:/.test(document.querySelector('main')?.innerText||''),main:document.querySelector('main')?.innerText,header:document.querySelector('header')?.innerText,viewport:{width:innerWidth,height:innerHeight},scrollY}));}
async function evidence(page,platform,id,account,selector){
 const state=await snapshot(page);const descriptor={id,state,account,selector};
 fs.writeFileSync(path.join(__dirname,`${platform}-state-${id}.json`),JSON.stringify(descriptor,null,2));
 let r;
 if(platform==='firefox'){
  const res=await fetch('http://127.0.0.1:9333',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(descriptor)});r=await res.json();if(!res.ok)throw Error('Selenium evidence: '+JSON.stringify(r));
 }else{
  if(selector)await page.locator(selector).evaluateAll(es=>es.forEach(e=>e.style.outline='3px solid red'));
  await page.evaluate(()=>{document.activeElement?.blur();window.scrollTo(0,0)});adb(['shell','input','keyevent','111']);
  await overlay(page,'Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator)');await wait(180);
  const filename=`androidchrome_${id}.png`;fs.writeFileSync(path.join(out,filename),adb(['exec-out','screencap','-p']));r={path:`screenshots/cross-platform/${filename}`,mode:'adb exec-out screencap -p, full device',state};
 }
 fs.writeFileSync(path.join(__dirname,`${platform}-evidence-${id}.json`),JSON.stringify(r,null,2));return r.path;
}
async function touchPoint(page,locator){
 await hideKeyboard(page);await locator.evaluate(e=>e.scrollIntoView({block:'center',inline:'nearest'}));await wait(160);
 const a=await locator.evaluate(e=>{const r=e.getBoundingClientRect(),x=r.x+r.width/2,y=r.y+r.height/2,h=document.elementFromPoint(x,y);return {x,y,w:r.width,h:r.height,hit:h===e||e.contains(h),obstacle:h?.outerHTML.slice(0,140),view:{w:innerWidth,h:innerHeight,offset:visualViewport.offsetTop}};});
 if(!a.hit)throw Error('Actual touch hit test failed: '+JSON.stringify(a));return a;
}
async function tap(page,locator){const a=await touchPoint(page,locator);const s=await page.context().newCDPSession(page);await s.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:a.x,y:a.y}]});await s.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});await s.detach();await wait(60);}
async function doubleTap(page,locator,delay=35){const a=await touchPoint(page,locator);const s=await page.context().newCDPSession(page);for(let i=0;i<2;i++){await s.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:a.x,y:a.y}]});await s.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});if(i===0)await wait(delay);}await s.detach();}

function uiNodes(){adb(['shell','uiautomator','dump','/sdcard/eshop-window.xml']);const xml=adb(['shell','cat','/sdcard/eshop-window.xml']).toString();fs.writeFileSync('/tmp/eshop-android-last-ui.xml',xml);return [...xml.matchAll(/<node\b([^>]+)>/g)].map(m=>Object.fromEntries([...m[1].matchAll(/([\w:-]+)="([^"]*)"/g)].map(x=>[x[1],x[2]])));}
function rect(node){const a=node.bounds.match(/\d+/g).map(Number);return {x:a[0],y:a[1],w:a[2]-a[0],h:a[3]-a[1]};}
function nativeTap(node){const r=rect(node);adb(['shell','input','tap',String(Math.round(r.x+r.w/2)),String(Math.round(r.y+r.h/2))]);}
async function copyOtpMobile(page){
 await page.evaluate(()=>{document.activeElement?.blur();window.scrollTo(0,0)});adb(['shell','input','keyevent','111']);await wait(150);
 const coords=await page.getByText('Mã OTP của bạn là:').evaluate(e=>{const n=e.firstChild,m=n.textContent.match(/\d+/),r=document.createRange();r.setStart(n,m.index);r.setEnd(n,m.index+m[0].length);const b=r.getBoundingClientRect();return{x:b.x+b.width/2,y:b.y+b.height/2,dpr:devicePixelRatio};});
 const nodes=uiNodes();const view=nodes.find(n=>n.class==='android.webkit.WebView');if(!view)throw Error('Native Chrome WebView bounds unavailable');const v=rect(view);const x=Math.round(v.x+coords.x*coords.dpr),y=Math.round(v.y+coords.y*coords.dpr);
 adb(['shell','input','swipe',String(x),String(y),String(x),String(y),'1100']);await wait(250);
 const menu=uiNodes();const copy=menu.find(n=>/^(copy|sao chép)$/i.test(n.text||n['content-desc']||''));if(!copy)throw Error('Native long-press Copy menu unavailable; no simulated clipboard copy');nativeTap(copy);await wait(120);await page.bringToFront();
 return page.evaluate(()=>navigator.clipboard.readText());
}
async function pasteMobile(page,field){
 await field.scrollIntoViewIfNeeded();await field.click();await wait(100);const r=await field.boundingBox(),nodes=uiNodes(),view=nodes.find(n=>n.class==='android.webkit.WebView');if(!view)throw Error('No native WebView');const v=rect(view),dpr=await page.evaluate(()=>devicePixelRatio);const x=Math.round(v.x+(r.x+r.width/2)*dpr),y=Math.round(v.y+(r.y+r.height/2)*dpr);
 adb(['shell','input','swipe',String(x),String(y),String(x),String(y),'1100']);await wait(200);const menu=uiNodes();const paste=menu.find(n=>/^(paste|dán)$/i.test(n.text||n['content-desc']||''));if(!paste)throw Error('Native Paste menu unavailable');nativeTap(paste);await wait(120);
}
async function hideKeyboard(page){await page.evaluate(()=>document.activeElement?.blur());adb(['shell','input','keyevent','111']);await wait(180);}
module.exports={tap,hideKeyboard,evidence,snapshot,overlay,doubleTap,copyOtpMobile,pasteMobile,adb};
