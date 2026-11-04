# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-01-15 Disabled fields are skipped and the remaining controls follow the visual order.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Tab=["field1","field2","field3","Cập nhật"]; return to submit=false; disabled email=true
TypeError: res.ok is not a function
    at Object.evidence (/home/zinn/zinn/testing/hw03/checklist/automation/cross-platform/cross-helpers.js:13:169)
    at processTicksAndRejections (node:internal/process/task_queues:103:5)
    at shot (/home/zinn/zinn/testing/hw03/checklist/automation/run-firefox-shared.cjs:32:65)
    at check (/home/zinn/zinn/testing/hw03/checklist/automation/run-firefox-shared.cjs:33:83)
    at /home/zinn/zinn/testing/hw03/checklist/automation/run-firefox-shared.cjs:74:502
    at /tmp/eshop-playwright/node_modules/playwright/lib/worker/workerProcessEntry.js:1654:9
    at /tmp/eshop-playwright/node_modules/playwright/lib/worker/workerProcessEntry.js:1134:11
    at TimeoutManager.withRunnable (/tmp/eshop-playwright/node_modules/playwright/lib/worker/workerProcessEntry.js:403:14)
    at TestInfoImpl._runWithTimeout (/tmp/eshop-playwright/node_modules/playwright/lib/worker/workerProcessEntry.js:1132:7)
    at /tmp/eshop-playwright/node_modules/playwright/lib/worker/workerProcessEntry.js:1652:7
    at WorkerMain._runTest (/tmp/eshop-playwright/node_modules/playwright/lib/worker/workerProcessEntry.js:1625:5)
    at WorkerMain.runTestGroup (/tmp/eshop-playwright/node_modules/playwright/lib/worker/workerProcessEntry.js:1520:9)
    at process.<anonymous> (/tmp/eshop-playwright/node_modules/playwright/lib/common/index.js:1955:25)

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Test source

```ts
  1  | const fs=require('fs'),path=require('path');const {execFileSync}=require('child_process');
  2  | const root=path.resolve(__dirname,'../../..');const out=path.join(root,'screenshots/cross-platform');
  3  | const ADB='/home/zinn/Android/Sdk/platform-tools/adb';
  4  | const wait=ms=>new Promise(r=>setTimeout(r,ms));
  5  | function adb(args){return execFileSync(ADB,['-s','emulator-5554',...args],{timeout:20000});}
  6  | async function overlay(page,label){await page.evaluate(label=>{document.getElementById('execution-evidence')?.remove();const e=document.createElement('div');e.id='execution-evidence';e.style.cssText='position:fixed;bottom:8px;right:8px;z-index:99999;background:#ff0;color:#000;padding:4px 8px;font:bold 13px sans-serif';e.textContent='23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · '+label+' · '+location.href;document.body.append(e);},label);}
  7  | async function snapshot(page){return page.evaluate(()=>({url:location.href,token:localStorage.getItem('token'),fields:[...document.querySelectorAll('main form input,main form textarea')].map(e=>({value:e.value,type:e.type,disabled:e.disabled})),otp:/Mã OTP của bạn là:/.test(document.querySelector('main')?.innerText||''),main:document.querySelector('main')?.innerText,header:document.querySelector('header')?.innerText,viewport:{width:innerWidth,height:innerHeight},scrollY}));}
  8  | async function evidence(page,platform,id,account,selector){
  9  |  const state=await snapshot(page);const descriptor={id,state,account,selector};
  10 |  fs.writeFileSync(path.join(__dirname,`${platform}-state-${id}.json`),JSON.stringify(descriptor,null,2));
  11 |  let r;
  12 |  if(platform==='firefox'){
> 13 |   const res=await fetch('http://127.0.0.1:9333',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(descriptor)});r=await res.json();if(!res.ok())throw Error('Selenium evidence: '+JSON.stringify(r));
     |                                                                                                                                                                         ^ Error: Tab=["field1","field2","field3","Cập nhật"]; return to submit=false; disabled email=true
  14 |  }else{
  15 |   if(selector)await page.locator(selector).evaluateAll(es=>es.forEach(e=>e.style.outline='3px solid red'));
  16 |   await page.evaluate(()=>{document.activeElement?.blur();window.scrollTo(0,0)});adb(['shell','input','keyevent','111']);
  17 |   await overlay(page,'Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator)');await wait(180);
  18 |   const filename=`androidchrome_${id}.png`;fs.writeFileSync(path.join(out,filename),adb(['exec-out','screencap','-p']));r={path:`screenshots/cross-platform/${filename}`,mode:'adb exec-out screencap -p, full device',state};
  19 |  }
  20 |  fs.writeFileSync(path.join(__dirname,`${platform}-evidence-${id}.json`),JSON.stringify(r,null,2));return r.path;
  21 | }
  22 | async function doubleTap(page,locator,delay=35){await locator.scrollIntoViewIfNeeded();const r=await locator.boundingBox();const s=await page.context().newCDPSession(page);for(let i=0;i<2;i++){await s.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:r.x+r.width/2,y:r.y+r.height/2}]});await s.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});if(i===0)await wait(delay);}await s.detach();}
  23 | function uiNodes(){adb(['shell','uiautomator','dump','/sdcard/eshop-window.xml']);const xml=adb(['shell','cat','/sdcard/eshop-window.xml']).toString();fs.writeFileSync('/tmp/eshop-android-last-ui.xml',xml);return [...xml.matchAll(/<node\b([^>]+)>/g)].map(m=>Object.fromEntries([...m[1].matchAll(/([\w:-]+)="([^"]*)"/g)].map(x=>[x[1],x[2]])));}
  24 | function rect(node){const a=node.bounds.match(/\d+/g).map(Number);return {x:a[0],y:a[1],w:a[2]-a[0],h:a[3]-a[1]};}
  25 | function nativeTap(node){const r=rect(node);adb(['shell','input','tap',String(Math.round(r.x+r.w/2)),String(Math.round(r.y+r.h/2))]);}
  26 | async function copyOtpMobile(page){
  27 |  await page.evaluate(()=>{document.activeElement?.blur();window.scrollTo(0,0)});adb(['shell','input','keyevent','111']);await wait(150);
  28 |  const coords=await page.getByText('Mã OTP của bạn là:').evaluate(e=>{const n=e.firstChild,m=n.textContent.match(/\d+/),r=document.createRange();r.setStart(n,m.index);r.setEnd(n,m.index+m[0].length);const b=r.getBoundingClientRect();return{x:b.x+b.width/2,y:b.y+b.height/2,dpr:devicePixelRatio};});
  29 |  const nodes=uiNodes();const view=nodes.find(n=>n.class==='android.webkit.WebView');if(!view)throw Error('Native Chrome WebView bounds unavailable');const v=rect(view);const x=Math.round(v.x+coords.x*coords.dpr),y=Math.round(v.y+coords.y*coords.dpr);
  30 |  adb(['shell','input','swipe',String(x),String(y),String(x),String(y),'1100']);await wait(250);
  31 |  const menu=uiNodes();const copy=menu.find(n=>/^(copy|sao chép)$/i.test(n.text||n['content-desc']||''));if(!copy)throw Error('Native long-press Copy menu unavailable; no simulated clipboard copy');nativeTap(copy);await wait(120);await page.bringToFront();
  32 |  return page.evaluate(()=>navigator.clipboard.readText());
  33 | }
  34 | async function pasteMobile(page,field){
  35 |  await field.scrollIntoViewIfNeeded();await field.click();await wait(100);const r=await field.boundingBox(),nodes=uiNodes(),view=nodes.find(n=>n.class==='android.webkit.WebView');if(!view)throw Error('No native WebView');const v=rect(view),dpr=await page.evaluate(()=>devicePixelRatio);const x=Math.round(v.x+(r.x+r.width/2)*dpr),y=Math.round(v.y+(r.y+r.height/2)*dpr);
  36 |  adb(['shell','input','swipe',String(x),String(y),String(x),String(y),'1100']);await wait(200);const menu=uiNodes();const paste=menu.find(n=>/^(paste|dán)$/i.test(n.text||n['content-desc']||''));if(!paste)throw Error('Native Paste menu unavailable');nativeTap(paste);await wait(120);
  37 | }
  38 | module.exports={evidence,snapshot,overlay,doubleTap,copyOtpMobile,pasteMobile,adb};
  39 | 
```