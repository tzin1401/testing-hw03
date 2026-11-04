"""Replay first failing state in installed Firefox, never replace app HTML.
Runs one Selenium session; Chrome-context screenshots include real address bar.
"""
import json,time,urllib.request,sys,traceback
from pathlib import Path
from http.server import HTTPServer,BaseHTTPRequestHandler
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import selenium
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'screenshots/cross-platform';OUT.mkdir(exist_ok=True)
BASE='http://localhost:5173';PW='Abc12345 '
def api(route,data):
 q=urllib.request.Request('http://localhost:3000'+route,data=json.dumps(data).encode(),headers={'Content-Type':'application/json'})
 with urllib.request.urlopen(q) as r:return json.load(r)
common=Path.home()/'snap/firefox/common/eshop-cross-profile';common.mkdir(exist_ok=True)
o=webdriver.FirefoxOptions();o.binary_location='/snap/firefox/current/usr/lib/firefox/firefox';o.add_argument('--no-remote')
o.set_preference('browser.shell.checkDefaultBrowser',False);o.set_preference('signon.rememberSignons',False)
d=webdriver.Firefox(service=Service('/snap/bin/geckodriver',service_args=['--allow-system-access','--profile-root',str(common)],log_output=str(ROOT/'checklist/automation/cross-platform/geckodriver.log')),options=o)
d.set_page_load_timeout(20);d.set_script_timeout(10)
d.set_window_rect(width=1280,height=950)
a=d.execute_script('return {w:outerWidth-innerWidth,h:outerHeight-innerHeight}')
d.set_window_rect(width=1280+a['w'],height=800+a['h'])
meta={'browser':d.capabilities['browserVersion'],'selenium':selenium.__version__,'driver':d.capabilities['moz:geckodriverVersion'],'systemAccess':'geckodriver --allow-system-access (passes privileged flag internally)','viewport':d.execute_script('return {innerWidth,innerHeight,outerWidth,outerHeight}'),'started':time.strftime('%Y-%m-%dT%H:%M:%S%z')}
(ROOT/'checklist/automation/cross-platform/selenium-environment.json').write_text(json.dumps(meta,indent=2))
def dismiss():
 try:
  a=d.switch_to.alert;t=a.text;a.accept();return t
 except NoAlertPresentException:return None

def nav(url):d.get(url if url.startswith('http') else BASE+url);time.sleep(.12)
def fields():return d.find_elements(By.CSS_SELECTOR,'main form input,main form textarea')
def fill(e,v):
 if e.is_enabled():e.clear();e.send_keys(v)
def submit():d.find_element(By.CSS_SELECTOR,'main form button[type=submit]').click();time.sleep(.13);return dismiss()
def fill_snapshot(vals,oldemail,email):
 for e,v in zip(fields(),vals):
  if e.is_enabled():fill(e,v.replace(oldemail,email) if oldemail else v)
def capture(x):
 id=x['id'];snap=x['state'];url=snap['url'];oldemail=x.get('account',{}).get('email','')
 email=f'evidence.{id.lower()}.{time.time_ns()}@test.local'
 if id=='IA-02-22':email=email.replace('@','.longemailsegmentlongemailsegment@')
 name=x.get('account',{}).get('name','Cross Firefox Tester')
 if id=='IA-01-20':name='<b>x</b>'
 api('/api/register',{'name':name,'email':email,'password':PW})
 nav('/login');d.execute_script('localStorage.clear();sessionStorage.clear()')
 if snap.get('token'):
  token=api('/api/login',{'email':email,'password':PW})['token'];d.execute_script('localStorage.setItem("token",arguments[0])',token)
 # Match viewport used by first failure (normal 1280x800, or responsive dimensions).
 v=snap.get('viewport',{'width':1280,'height':800});a=d.execute_script('return {w:outerWidth-innerWidth,h:outerHeight-innerHeight}')
 d.set_window_rect(width=v['width']+a['w'],height=v['height']+a['h'])
 nav(url)
 vals=[e['value'] for e in snap.get('fields',[])]
 if snap.get('otp'):
  fill(fields()[0],email);submit();time.sleep(.12)
 fill_snapshot(vals,oldemail,email)
 alert=None;action='load URL, restore auth with independent API fixture, fill controls'
 if id in ['IA-02-08','IA-04-02','IA-04-03','IA-04-17']:
  es=fields();fill(es[0],email);fill(es[1],'Wrong123!');alert=submit()
  if id=='IA-04-02':submit();submit()
  if id=='IA-04-03':fill(fields()[1],PW)
  action+='; submit invalid login'+('; edit password' if id=='IA-04-03' else '')
 elif id in ['IA-02-06','IA-04-05']:
  alert=submit();action+='; submit spec-valid password rejected by UI'
 elif id in ['IA-02-14','IA-02-15','IA-02-21','IA-04-07','IA-04-11','IA-04-12','IA-01-18','IA-04-20']:
  alert=submit();action+='; submit form, capture dialog then dismiss'
 elif id=='IA-03-04':
  nav('/');d.find_elements(By.XPATH,"//main//button[contains(.,'Thêm vào giỏ')]")[0].click();d.find_element(By.CSS_SELECTOR,'header a[href="/profile"]').click();time.sleep(.15);action+='; add exactly 1 product and navigate via SPA to Profile'
 elif id=='IA-04-16':
  d.execute_script('const old=XMLHttpRequest.prototype.send;XMLHttpRequest.prototype.send=function(...a){setTimeout(()=>old.apply(this,a),2000)}')
  b=d.find_element(By.CSS_SELECTOR,'main form button[type=submit]');b.click();b.click();action+='; delay actual XHR send 2 seconds, click twice'
 elif id=='IA-04-18':
  d.set_context(d.CONTEXT_CHROME);d.execute_script('Services.io.offline=true');d.set_context(d.CONTEXT_CONTENT)
  alert=submit();action+='; offline API failure equivalent to 503'
 if x.get('selector'):
  d.execute_script('document.querySelectorAll(arguments[0]).forEach(e=>e.style.outline="3px solid red")',x['selector'])
 # Show address bar and relevant control; never synthesize the app's error text/DOM.
 d.execute_script('document.activeElement?.blur();window.scrollTo(0,arguments[0])',snap.get('scrollY',0))
 label='Firefox '+meta['browser']+' · Ubuntu'
 d.execute_script('document.getElementById("execution-evidence")?.remove();const e=document.createElement("div");e.id="execution-evidence";e.style.cssText="position:fixed;bottom:8px;right:8px;z-index:99999;background:#ff0;color:#000;padding:4px 8px;font:bold 13px sans-serif";e.textContent="23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · "+arguments[0]+" · "+location.href;document.body.append(e)',label)
 actual=d.execute_script('return {url:location.href,main:document.querySelector("main").innerText,fields:[...document.querySelectorAll("main form input,main form textarea")].map(e=>({value:e.value,type:e.type})),head:document.querySelector("header").innerText,viewport:{width:innerWidth,height:innerHeight}}')
 file=OUT/('firefox_'+id+'.png');mode='chrome context, real browser address bar'
 try:
  d.set_context(d.CONTEXT_CHROME);d.save_screenshot(str(file))
 except Exception as e:
  mode='page screenshot fallback: '+str(e);d.set_context(d.CONTEXT_CONTENT);d.save_screenshot(str(file))
 finally:
  d.set_context(d.CONTEXT_CONTENT)
  if id=='IA-04-18':
   d.set_context(d.CONTEXT_CHROME);d.execute_script('Services.io.offline=false');d.set_context(d.CONTEXT_CONTENT)
 return {'path':str(file.relative_to(ROOT)),'mode':mode,'action':action,'alert':alert,'actual':actual,'capturedAt':time.strftime('%Y-%m-%dT%H:%M:%S%z')}
class Handler(BaseHTTPRequestHandler):
 def do_POST(self):
  try:
   x=json.loads(self.rfile.read(int(self.headers['Content-Length'])));r=capture(x);code=200
  except Exception as e:
   try:d.set_context(d.CONTEXT_CONTENT);dismiss()
   except:pass
   r={'error':str(e),'trace':traceback.format_exc()};code=500
  self.send_response(code);self.send_header('Content-Type','application/json');self.end_headers();self.wfile.write(json.dumps(r).encode())
 def log_message(self,*a):print(*a,flush=True)
print('READY SELENIUM EVIDENCE 9333',meta,flush=True)
try:HTTPServer(('127.0.0.1',9333),Handler).serve_forever()
finally:d.quit()
