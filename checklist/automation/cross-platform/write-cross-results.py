"""Append cross-platform results; never rewrite Chrome artifacts or old Notes."""
from pathlib import Path
import json,collections,re,hashlib,datetime
import openpyxl
from openpyxl.styles import Font,PatternFill
ROOT=Path(__file__).resolve().parents[3];DIR=Path(__file__).resolve().parent
BOOK=ROOT/'checklist/gui-checklist.xlsx';SNAP=DIR/'input-checklist.xlsx'
platforms={'firefox':'Firefox','androidchrome':'Android Chrome'}
raw={k:json.loads((DIR/(k+'-results.json')).read_text()) for k in platforms}
by={k:{r['id']:r for r in rows} for k,rows in raw.items()}
w=openpyxl.load_workbook(BOOK);s=w['Checklist'];h={c.value:c.column for c in s[1]}
rows={s.cell(i,h['ID']).value:i for i in range(2,s.max_row+1) if s.cell(i,h['ID']).value}
assert len(rows)==79
for p in platforms:
 assert set(by[p])==set(rows),'Incomplete '+p
 for id,r in by[p].items():
  assert r['result'] in ['Passed','Failed','N/A','MANUAL']
  assert not r.get('incomplete'),('Incomplete execution',p,id)
  if r['result']=='Failed':assert r['screenshot'] and (ROOT/r['screenshot']).is_file(),('Missing screenshot',p,id)
 for name in ['login','register','forgot-step1','forgot-step2','profile']:assert (ROOT/f'screenshots/cross-platform/{p}_screen-{name}.png').is_file()
def short(r):
 t=r['notes'];id=r['id']
 if r['result']=='MANUAL':return t.split('\nQuan sát:')[0].split('\nCall log:')[0][:800]
 if id=='IA-01-13':
  matches=re.findall(r'([^\n]+?): greeting=(\{.*?\}); logout=(\{.*?\}); navRight=([\d.]+)',t)
  if matches:return '; '.join(f'{route}: greeting left/right={json.loads(a)["x"]:.2f}/{json.loads(a)["right"]:.2f}; logout left={json.loads(b)["x"]:.2f}; navRight={right}' for route,a,b,right in matches)
 if id=='IA-01-12' and 'Header/footer geometry across screens=' in t:
  a=json.loads(t.split('Header/footer geometry across screens=',1)[1]);return '; '.join(f'{x["r"]}: header y/h={x["s"][0]["y"]:.2f}/{x["s"][0]["h"]:.2f}; footer y/h={x["s"][2]["y"]:.2f}/{x["s"][2]["h"]:.2f}' for x in a)
 t=t.replace('\n',' | ')
 if len(t)>2200:t=t[:1500]+' … '+t[-450:]+' (đầy đủ trong JSON theo ID)'
 return t
chrome={id:s.cell(row,h['Chrome']).value or 'MANUAL' for id,row in rows.items()}
for id,row in rows.items():
 old=s.cell(row,h['Notes']).value or ''
 add=[]
 for p,label in platforms.items():
  r=by[p][id];result=r['result'];s.cell(row,h[label]).value=None if result=='MANUAL' else result
  if result in ['Failed','N/A','MANUAL'] or result!=chrome[id]:
   detail=short(r)
   if result!='MANUAL' and not detail.startswith('N/A:'):detail=result+': '+detail
   if r['screenshot']:detail+='; Ảnh: '+r['screenshot']
   line=f'[{label}] {detail}'
   if line not in old.splitlines():add.append(line)
 if add:s.cell(row,h['Notes']).value=old+('\n' if old else '')+'\n'.join(add)
 assert len(s.cell(row,h['Notes']).value or '')<=32767,(id,'Excel note limit')
# Preserve the existing Chrome summary in A:F; append four columns per new platform.
t=w['Summary'];start=7
counts={p:collections.defaultdict(collections.Counter) for p in platforms}
for p,records in raw.items():
 for r in records:counts[p][r['ia']][r['result']]+=1
for p,label in platforms.items():
 for off,result in enumerate(['Passed','Failed','N/A','MANUAL']):
  c=t.cell(1,start+off,f'{label} {result}');c.font=Font(bold=True,color='FFFFFF');c.fill=PatternFill('solid',fgColor='2457A6')
  for row in range(2,t.max_row+1):
   ia=t.cell(row,1).value
   counter=sum(counts[p].values(),collections.Counter()) if ia=='TOTAL' else counts[p][ia]
   t.cell(row,start+off,counter[result]);t.column_dimensions[openpyxl.utils.get_column_letter(start+off)].width=25
 start+=4
w.save(BOOK)
# Verify preservation against the workbook received for this task.
a=openpyxl.load_workbook(SNAP);b=openpyxl.load_workbook(BOOK)
assert a.sheetnames==b.sheetnames
for name in a.sheetnames:
 aa,bb=a[name],b[name]
 if name=='Summary':
  for row in aa:
   for c in row:assert c.value==bb[c.coordinate].value and c._style==bb[c.coordinate]._style
  continue
 assert (aa.max_row,aa.max_column)==(bb.max_row,bb.max_column)
 for row in aa:
  for c in row:
   n=bb[c.coordinate];assert c._style==n._style and c.hyperlink==n.hyperlink,(name,c.coordinate,'format/link')
   if name!='Checklist' or c.column not in [h['Firefox'],h['Android Chrome'],h['Notes']]:assert c.value==n.value,(name,c.coordinate,'unauthorized change')
   elif c.column==h['Notes']:assert (n.value or '').startswith(c.value or ''),(c.coordinate,'old Notes lost')
 assert str(aa.data_validations)==str(bb.data_validations)
 assert str(aa.merged_cells)==str(bb.merged_cells)
 assert aa.freeze_panes==bb.freeze_panes
 for k in aa.column_dimensions:assert dict(aa.column_dimensions[k])==dict(bb.column_dimensions[k])
 for k in aa.row_dimensions:assert dict(aa.row_dimensions[k])==dict(bb.row_dimensions[k])
hashes=json.loads((DIR/'chrome-artifacts-before.json').read_text())
for file,digest in hashes.items():assert hashlib.sha256((ROOT/file).read_bytes()).hexdigest()==digest,('Chrome artifact changed',file)
validation={'rows':79,'untouchedColumnsStylesLinksDropdowns':True,'oldNotesPreserved':True,'chromeArtifactsUnchanged':len(hashes),'counts':{p:dict(sum(x.values(),collections.Counter())) for p,x in counts.items()},'validatedAt':datetime.datetime.now().astimezone().isoformat()}
(DIR/'workbook-validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2))

def reason(p,id,r):
 if r['result']=='N/A':return r['notes']+' Khác phạm vi thao tác/viewport của thiết bị.'
 if r['result']=='MANUAL':
  if id in ['IA-01-16','IA-01-17','IA-01-19']:return 'Chrome đã được sinh viên kiểm tay và ghi Passed; chưa có kiểm tay tương ứng trên Firefox. Cần kiểm mắt riêng từng engine.'
  return 'Dự đoán: giới hạn điều khiển clipboard/focus native hoặc chưa hoàn tất automation; không đủ bằng chứng kết luận ứng dụng. '+short(r)
 if p=='androidchrome' and id=='IA-01-13':return 'Dự đoán: greeting chứa chuỗi 60 ký tự không ngắt dòng; flex navbar thiếu giới hạn chiều rộng trên màn hình 412 CSS px. '+short(r)
 if p=='androidchrome' and id=='IA-01-12':return 'Dự đoán: breakpoint md xếp Profile và lịch sử đơn hàng theo chiều dọc; chiều cao nội dung và chrome UI di động làm footer đổi vị trí. Expected yêu cầu cùng vị trí được áp dụng nguyên văn; cần review mức độ nghiêm trọng. '+short(r)
 if p=='androidchrome' and id=='IA-02-22':return 'Dự đoán: input Profile trên mobile rộng hơn desktop; độ dài chuỗi/font quyết định việc bị cắt. '+short(r)
 if id=='IA-01-15':return 'Dự đoán: khác biệt chuyển focus giữa nội dung trang và thanh trình duyệt. '+short(r)
 return 'Dự đoán: khác biệt layout/engine hoặc cách tương tác native; cần xem số đo và state cụ thể. '+short(r)
def esc(x):return str(x).replace('|','\\|').replace('\n','<br>')
meta={p:json.loads((DIR/(p+'-environment.json')).read_text()) for p in platforms};se=json.loads((DIR/'selenium-environment.json').read_text())
starts={p:json.loads((DIR/(('android' if p=='androidchrome' else p)+'-playwright.json')).read_text()).get('stats',{}).get('startTime','') for p in platforms}
ends={p:max(r['executedAt'] for r in rs) for p,rs in raw.items()}
lines=['# Thực thi lại GUI checklist — Firefox và Android Chrome','',
'- SUT: http://localhost:5173; API http://localhost:3000. Không restart hoặc sửa `eshop-sut/`. Không tạo issue/commit.',
'- Workbook đầu vào của lượt này có Chrome **28 Passed / 51 Failed**: ba item IA-01-16/17/19 đã được sinh viên kiểm tay và ghi Passed sau lượt automation Chrome. So sánh dùng cột Chrome hiện tại, giữ nguyên kết quả kiểm tay.',
'', '## Môi trường và cách chạy','',
f"- OS host: Ubuntu 26.04.1 LTS, Wayland; {meta['firefox']['os']}; Node.js v22.22.1; Playwright {meta['firefox']['playwright']}.",
f"- Firefox thực thi: **Playwright Firefox {meta['firefox']['browser']}**, bản Gecko riêng `firefox-1555` do Playwright tải, viewport 1280×800. Đây không phải binary Firefox snap. Clipboard testing preference `dom.events.testing.asyncClipboard=true`; không cấp permission Chromium cho Firefox.",
f"- Firefox bằng chứng: **Firefox snap {se['browser']}** (`/snap/firefox/current/usr/lib/firefox/firefox`), Selenium {se['selenium']}, geckodriver snap {se['driver']}. geckodriver `--allow-system-access` cấp quyền chrome context; truyền `--remote-allow-system-access` qua capabilities bị geckodriver 0.37.1 từ chối. Sau khi chuyển sang service flag, chụp chrome context thành công.",
f"- Android: emulator-5554, AVD Pixel_9, Android 15, 1080×2424 px vật lý; **Chrome 124.0.6367.219**. CDP trực tiếp localhost:9222, dùng context/page có sẵn. Viewport thực khoảng 412×790 CSS px, DPR 2.625; chiều cao có thể đổi khi thanh địa chỉ/bàn phím hiện/ẩn. Không gọi setViewportSize trên Android.",
f"- Thời gian Firefox: {starts['firefox']} → {ends['firefox']}; Android: {starts['androidchrome']} → {ends['androidchrome']} (ISO UTC, giờ Việt Nam = UTC+07:00).",
'- Dữ liệu: POST /api/register tạo tài khoản riêng cho từng test; password `Abc12345 `, reset `Newpass123 `, có dấu cách cuối theo validator UI hiện tại. Lockout/sai password luôn dùng tài khoản riêng. Không sửa tài khoản seed; duplicate/normalization giữ scenario của checklist.',
'- `load-suite.js` đọc nguyên file Chrome và chạy chung 79 test body qua adapter; file Chrome gốc không bị sửa. Adapter đổi fixtures, đường dẫn output, screenshot, clipboard và thao tác tương đương mobile; giữ Expected Result từ workbook.',
'- Sửa riêng cách thử Shift+Tab trong form để không gửi page keyboard vào thanh trình duyệt Firefox: đo đủ chuỗi focus bắt buộc, Shift+Tab từ submit về textarea rồi Tab lại submit. Android đóng bàn phím bằng blur/Escape trước bấm submit; tính tọa độ touch từ DOM và xác minh elementFromPoint trước khi gửi touch qua CDP, tránh lệch tọa độ trên Chrome 124. Double submit dùng hai touch event thật qua CDP.',
'- Firefox chụp bằng Selenium sau khi tái hiện state bằng UI thật và tài khoản bằng chứng độc lập, cùng URL và input tương đương; không dựng lại HTML của SUT. OTP và email trong ảnh replay có thể khác lượt Playwright. JSON `firefox-evidence-<ID>.json` ghi state, action, dialog, mode chụp. Ảnh pending dùng XHR send delay 2 giây; ảnh lỗi network dùng offline API tương đương unreachable.',
'- Android ảnh lấy trực tiếp `adb exec-out screencap -p`, gồm thanh địa chỉ, status bar và navigation bar. Overlay chứa danh tính, browser/device và URL trước mỗi lần chụp; giới hạn theo visualViewport để vẫn nhìn thấy khi trang tràn ngang. Lỗi DOM có outline đỏ. Native alert được ghi vào JSON/Notes rồi đóng; ảnh web chụp sau khi đóng dialog.',
'', '```bash',
'uv --cache-dir /tmp/eshop-uv-cache pip install --python /tmp/eshop-chrome-venv/bin/python selenium==4.52.0 openpyxl pillow==13.0.0',
'npm install --prefix /tmp/eshop-playwright --cache /tmp/eshop-npm-cache @playwright/test@1.64.1',
'NODE_PATH=/tmp/eshop-playwright/node_modules /tmp/eshop-playwright/node_modules/.bin/playwright install firefox',
'~/Android/Sdk/platform-tools/adb reverse tcp:5173 tcp:5173',
'~/Android/Sdk/platform-tools/adb reverse tcp:3000 tcp:3000',
'~/Android/Sdk/platform-tools/adb forward tcp:9222 localabstract:chrome_devtools_remote',
'# Terminal 1: giữ server Selenium chụp bằng chứng đang chạy',
'/tmp/eshop-chrome-venv/bin/python checklist/automation/cross-platform/firefox-evidence-server.py',
'# Terminal 2: chạy lần lượt; exit code 1 là dự kiến nếu có Failed',
'CROSS_PW_JSON=checklist/automation/cross-platform/firefox-playwright.json NODE_PATH=/tmp/eshop-playwright/node_modules /tmp/eshop-playwright/node_modules/.bin/playwright test -c checklist/automation/playwright.cross.config.js --project firefox',
'CROSS_PW_JSON=checklist/automation/cross-platform/android-playwright.json NODE_PATH=/tmp/eshop-playwright/node_modules /tmp/eshop-playwright/node_modules/.bin/playwright test -c checklist/automation/playwright.cross.config.js --project androidchrome',
'NODE_PATH=/tmp/eshop-playwright/node_modules node checklist/automation/cross-platform/make-overviews.js firefox',
'NODE_PATH=/tmp/eshop-playwright/node_modules node checklist/automation/cross-platform/make-overviews.js androidchrome',
'/tmp/eshop-chrome-venv/bin/python checklist/automation/cross-platform/validate-evidence.py',
'/tmp/eshop-chrome-venv/bin/python checklist/automation/cross-platform/write-cross-results.py',
'```','',
'Chạy từ gốc repo. Cần bản snapshot workbook trước lượt này tại `automation/cross-platform/input-checklist.xlsx` và manifest hash `automation/cross-platform/chrome-artifacts-before.json` để xác minh bảo toàn. Không chạy writer của lượt Chrome. Kết quả MANUAL để trống ô kết quả; N/A có lý do. Chạy lại riêng bằng `--grep "IA-xx-yy "` cập nhật JSON theo ID; native report của từng lượt được lưu riêng.','',
'## Tổng kết','', '| Platform | Passed | Failed | N/A | MANUAL | Tổng |','|---|---:|---:|---:|---:|---:|',
'| Chrome (baseline) | 28 | 51 | 0 | 0 | 79 |']
for p,label in platforms.items():
 c=sum(counts[p].values(),collections.Counter());lines.append(f'| {label} | {c["Passed"]} | {c["Failed"]} | {c["N/A"]} | {c["MANUAL"]} | 79 |')
lines+=['','## So sánh từng ID','','| ID | Chrome | Firefox | Android Chrome | Ghi chú khác biệt |','|---|---|---|---|---|']
diffs=[]
for id in rows:
 ds=[(p,by[p][id]) for p in platforms if by[p][id]['result']!=chrome[id]]
 note='; '.join(f'{platforms[p]}: '+reason(p,id,r) for p,r in ds) if ds else 'Cùng kết quả.'
 if ds:diffs.append((id,ds))
 lines.append('| '+' | '.join(esc(v) for v in [id,chrome[id],by['firefox'][id]['result'],by['androidchrome'][id]['result'],note])+' |')
lines+=['','## Item khác Chrome và nguyên nhân dự đoán','',f'Có {len(diffs)} ID có ít nhất một platform cho kết quả khác Chrome.','']
for id,ds in diffs:
 for p,r in ds:lines.append(f'- **{id} — {platforms[p]} {r["result"]} (Chrome {chrome[id]})**: '+reason(p,id,r))
lines+=['','## MANUAL và N/A','']
for p,label in platforms.items():
 for r in raw[p]:
  if r['result'] in ['MANUAL','N/A']:lines.append(f'- **{label} {r["id"]} — {r["result"]}**: '+short(r))
lines+=['','## Ảnh và actual result','',
'- Tổng quan: `screenshots/cross-platform/<platform>_screen-login.png`, `screen-register`, `screen-forgot-step1`, `screen-forgot-step2`, `screen-profile`. Toàn bộ **111 ảnh** đã xác minh PNG và overlay hiện trong ảnh: **55 ảnh Firefox chrome context** (50 lỗi + 5 tổng quan, không dùng fallback) và **56 ảnh Android screencap** (51 lỗi + 5 tổng quan), đúng 1080×2424 px thiết bị. Chi tiết: `automation/cross-platform/image-validation.json`.',
'- Mỗi Failed: `screenshots/cross-platform/<platform>_<ID>.png`; Notes nối đường dẫn, cột Screenshot cũ giữ nguyên.',
'- Actual đầy đủ: `automation/cross-platform/firefox-results.json` và `androidchrome-results.json`, gồm method, request/response, dialog và timestamp theo ID.',
'- Native Playwright JSON/log và JSON state/evidence cùng thư mục. `firefox-playwright.json`, `android-playwright.json` ghi lượt đầy đủ; `firefox-recheck-playwright.json` (13 item), `firefox-clipboard-playwright.json` (1 item), `android-recheck-playwright.json` (8 item) ghi các lượt sau khi sửa adapter; kết quả cuối lấy JSON theo ID. Không chuyển lỗi công cụ thành kết luận ứng dụng.',
'', '| ID | Platform | Result | Cách kiểm | Actual |','|---|---|---|---|---|']
for id in rows:
 for p,label in platforms.items():
  r=by[p][id];a=short(r)
  if r['screenshot']:a+='; [Ảnh](../'+r['screenshot']+')'
  lines.append('| '+' | '.join(esc(v) for v in [id,label,r['result'],r['method'],a])+' |')
lines+=['','## Bảo toàn dữ liệu','',
'- Chỉ cập nhật Firefox, Android Chrome và nối Notes trên Checklist. Giữ toàn bộ giá trị cột khác, style, dropdown, hyperlink, dòng/thứ tự dòng; sheet Review không đổi.',
'- Summary giữ các ô Chrome cũ A:F; thêm Firefox Passed/Failed/N/A/MANUAL và Android Chrome Passed/Failed/N/A/MANUAL theo IA và tổng.',
'- Đã so workbook trước/sau và hash toàn bộ file của lượt Chrome. Kết quả xác minh: `automation/cross-platform/workbook-validation.json`.','']
(ROOT/'checklist/execution-cross-platform.md').write_text('\n'.join(lines))
print(json.dumps(validation,ensure_ascii=False,indent=2))
