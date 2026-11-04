const base=require('@playwright/test');
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
const test=base.test.extend({
 browser:[async({playwright,browserName,launchOptions,channel},use,workerInfo)=>{
  let b;
  if(workerInfo.project.name==='androidchrome')b=await chromium.connectOverCDP('http://localhost:9222');
  else b=await playwright.firefox.launch({...launchOptions,headless:false,firefoxUserPrefs:{'dom.events.testing.asyncClipboard':true}});
  await use(b);await b.close();
 },{scope:'worker'}],
 context:async({browser},use,testInfo)=>{
  const mobile=testInfo.project.name==='androidchrome';
  const c=mobile?browser.contexts()[0]:await browser.newContext({viewport:{width:1280,height:800}});
  if(mobile)await c.grantPermissions(['clipboard-read','clipboard-write'],{origin:'http://localhost:5173'});
  await use(c);if(!mobile)await c.close();
 },
 page:async({context},use,testInfo)=>{
  const mobile=testInfo.project.name==='androidchrome';
  const p=mobile?(context.pages()[0]||await context.newPage()):await context.newPage();
  if(mobile){await p.unrouteAll({behavior:'ignoreErrors'});p.removeAllListeners('dialog');p.removeAllListeners('request');p.removeAllListeners('response');await p.goto('http://localhost:5173/login');await p.evaluate(()=>{localStorage.clear();sessionStorage.clear()});await context.clearCookies();await p.reload();}
  let proto,originalClick;if(mobile){proto=Object.getPrototypeOf(p.locator('body'));originalClick=proto.click;proto.click=async function(){return require('./cross-helpers').tap(this.page(),this);};}
  await p.bringToFront();await use(p);if(mobile)proto.click=originalClick;
  if(mobile){await p.unrouteAll({behavior:'ignoreErrors'});p.removeAllListeners('dialog');p.removeAllListeners('request');p.removeAllListeners('response');}else await p.close();
 }
});
module.exports={test,expect:base.expect};
