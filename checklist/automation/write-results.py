"""Write only Chrome/Notes/Screenshot cells; preserve other Checklist cells."""
import json, collections, datetime, pathlib, platform, sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
ROOT=pathlib.Path(__file__).resolve().parents[2]
BASE=ROOT/'checklist/automation'
wb_path=ROOT/'checklist/gui-checklist.xlsx'
w=openpyxl.load_workbook(wb_path);s=w['Checklist']
headers={c.value:c.column for c in s[1]}
items=json.loads((BASE/'items.json').read_text())
results=json.loads((BASE/'execution-results.json').read_text())
byid={r['id']:r for r in results}
assert len(items)==79 and len(byid)==79 and set(byid)=={i['ID'] for i in items},'Incomplete execution'
counts=collections.defaultdict(collections.Counter)
for row in range(2,s.max_row+1):
    id=s.cell(row,headers['ID']).value
    if not id:continue
    r=byid[id];result=r['result']
    assert result in {'Passed','Failed','N/A','MANUAL'}
    if result=='Failed':assert r['screenshot'] and (ROOT/r['screenshot']).is_file(),f'Missing evidence {id}'
    s.cell(row,headers['Chrome']).value=None if result=='MANUAL' else result
    s.cell(row,headers['Notes']).value=r['notes']
    s.cell(row,headers['Screenshot']).value=r['screenshot'] or None
    counts[r['ia']][result]+=1
if 'Summary' in w:del w['Summary']
t=w.create_sheet('Summary');t.append(['IA','Passed','Failed','N/A','MANUAL','Total'])
for ia,c in sorted(counts.items()):t.append([ia,c['Passed'],c['Failed'],c['N/A'],c['MANUAL'],sum(c.values())])
total=sum(counts.values(),collections.Counter());t.append(['TOTAL',total['Passed'],total['Failed'],total['N/A'],total['MANUAL'],sum(total.values())])
for cell in t[1]:cell.font=Font(bold=True,color='FFFFFF');cell.fill=PatternFill('solid',fgColor='2457A6')
for cell in t[t.max_row]:cell.font=Font(bold=True)
t.column_dimensions['A'].width=34
for name in ['B','C','D','E','F']:t.column_dimensions[name].width=14
t.freeze_panes='B2';t.auto_filter.ref=f'A1:F{t.max_row-1}'
w.save(wb_path)
# Compare with original snapshot: all non-result cells, styles, dimensions, validation rules.
original=pathlib.Path('/tmp/eshop-original-checklist.xlsx')
if original.exists():
    a=openpyxl.load_workbook(original)['Checklist'];b=openpyxl.load_workbook(wb_path)['Checklist']
    assert (a.max_row,a.max_column)==(b.max_row,b.max_column)
    for row in a:
        for old in row:
            new=b[old.coordinate]
            assert old._style==new._style,('Style changed',old.coordinate)
            if old.column not in [headers[x] for x in ['Chrome','Notes','Screenshot']]:
                assert old.value==new.value,('Value changed',old.coordinate)
                assert old.hyperlink==new.hyperlink,('Hyperlink changed',old.coordinate)
    assert str(a.data_validations)==str(b.data_validations),'Dropdown changed'
    assert str(a.merged_cells)==str(b.merged_cells)
    assert str(a.freeze_panes)==str(b.freeze_panes)
    for k in a.column_dimensions:assert dict(a.column_dimensions[k])==dict(b.column_dimensions[k])
    for k in a.row_dimensions:assert dict(a.row_dimensions[k])==dict(b.row_dimensions[k])
env=json.loads((BASE/'environment.json').read_text())
pw=json.loads((BASE/'playwright-results.json').read_text())
def clean(v):return str(v).replace('|','\\|').replace('\n','<br>').replace('\r','')
start=pw.get('stats',{}).get('startTime',min(r['executedAt'] for r in results))
end=max(r['executedAt'] for r in results)
lines=['# Thực thi GUI checklist — Google Chrome','',
       '- SUT: http://localhost:5173; API: http://localhost:3000. Không restart server, không sửa `eshop-sut/`.',
       '- OS: '+next(x.split('=',1)[1].strip('"') for x in env['platform'].splitlines() if x.startswith('PRETTY_NAME='))+'; '+env['os'],
       f"- Google Chrome: {env['chrome']}; Playwright: {env['playwright']}; Node.js v22.22.1; headed (`headless:false`), `channel: 'chrome'`.",
       f'- Thời gian: {start} → {end} (ISO UTC; giờ Việt Nam = UTC+07:00).',
       '- Viewport mặc định 1280×800; mô phỏng 200% bằng 640×400; reflow bằng 320×640. Clipboard read/write được cấp cho context.',
       '- Mỗi item có tài khoản riêng `t<ID>.<timestamp>.0@test.local`, tạo bằng POST /api/register. Không dùng seed cho sai mật khẩu/lockout. Chỉ các item duplicate/normalization dùng email seed như checklist.',
       '- Password đi tiếp luồng UI: `Abc12345 ` (có dấu cách cuối). Quan sát thực thi: `Abc12345!` bị UI từ chối, password có whitespace được nhận. Validator yêu cầu hoa/thường/số/whitespace và chỉ cho phép chữ, số, whitespace; khác FR-01. Reset dùng `Newpass123 `.',
       '- Contrast tính theo WCAG: sRGB tuyến tính hóa tại 0.04045; L=0.2126R+0.7152G+0.0722B; ratio=(Lmax+0.05)/(Lmin+0.05). Background trong suốt được lần lên ancestor có màu nền.',
       '- Loading: delay response 2 giây bằng route; request đếm bằng `page.on("request")`. Lỗi network được inject HTTP 503; lỗi save HTTP 500.',
       '- Ảnh chỉ dành cho Failed, fullPage, có overlay yêu cầu; lỗi DOM được outline đỏ. Với item có nhiều lỗi, ảnh ghi nhận lỗi đầu tiên, Notes ghi các phép kiểm tiếp theo. Native alert được handler ghi nguyên văn rồi đóng để tiếp tục; ảnh web chụp sau khi đóng dialog, nội dung alert có trong Notes/JSON, không giả lập dialog trong ảnh.',
       '- Không tạo GitHub Issue, không commit.','',
       f"Kết quả: **{total['Passed']} Passed / {total['Failed']} Failed / {total['N/A']} N/A / {total['MANUAL']} MANUAL**, tổng 79 item. MANUAL để trống Chrome trong Excel.",'',
       '## Chạy lại','',
       '```bash',
       'uv --cache-dir /tmp/eshop-uv-cache venv /tmp/eshop-chrome-venv',
       'uv --cache-dir /tmp/eshop-uv-cache pip install --python /tmp/eshop-chrome-venv/bin/python openpyxl',
       'npm install --prefix /tmp/eshop-playwright --cache /tmp/eshop-npm-cache @playwright/test@'+env['playwright'],
       'NODE_PATH=/tmp/eshop-playwright/node_modules /tmp/eshop-playwright/node_modules/.bin/playwright test -c checklist/automation/playwright.config.js > checklist/automation/run-chrome.log 2>&1',
       '# Playwright exit 1 là dự kiến khi có Failed; vẫn xuất báo cáo sau khi suite đã hoàn tất.',
       '/tmp/eshop-chrome-venv/bin/python checklist/automation/write-results.py','```','',
       'Chạy từ thư mục gốc repo; cần desktop/X DISPLAY và Chrome đã cài. `items.json` là bản trích nguyên văn workbook đầu vào; không thay đổi checklist. Script ghi JSON sau từng item và hỗ trợ chạy lại riêng bằng `--grep "IA-xx-yy "`; lần chạy riêng cập nhật đúng ID. Khi chạy lại toàn bộ, mọi ID được ghi đè bằng kết quả mới.','',
       '## Kết quả từng item','',
       '| ID | Result | Cách kiểm (1 dòng) | Actual |','|---|---|---|---|']
for i in items:
    r=byid[i['ID']]
    actual=r['notes']
    if r['screenshot']:actual+='\nẢnh: ['+r['screenshot']+'](../'+r['screenshot']+')'
    lines.append('| '+' | '.join(map(clean,[r['id'],r['result'],r['method'],actual]))+' |')
lines+=['','## Item MANUAL','']
manuals=[r for r in results if r['result']=='MANUAL']
lines += ['- '+r['id']+': '+r['notes'] for r in manuals] or ['Không có.']
lines+=['','## Diễn giải Expected Result','',
'- “All G1 screens/forms”: Login, Register, Forgot Password bước 1, bước 2 và Profile; header có đăng nhập được kiểm bằng tài khoản riêng. Mỗi item dừng kết luận Failed ngay khi có một điều kiện sai; không coi việc thiếu một trường bắt buộc là N/A.',
'- “Blue/design-token blue”: lấy blue-600 `rgb(37, 99, 235)` đang dùng ở nút Login/OTP bước 1; không tự thiết kế màu mới.',
'- “Same geometry/equal spacing/centred”: bounding box CSS px, dung sai nhỏ hơn 1 px; h1 tính trong main, header logo không được coi là heading trang.',
'- “Header/footer same position”: so vị trí trong viewport 1280×800 và không giao main; nội dung dài hơn viewport làm footer dịch được ghi rõ trong Actual nếu có.',
'- IA-01-13: tên 60 ký tự liên tục `N` để kiểm khả năng chứa chuỗi dài. IA-01-16: focus ring native/auto cần người kiểm mắt để biết độ phủ và màu kề, không đoán Passed từ computed outline.',
'- IA-01-17/19: chỉ đo DOM không đủ chứng minh mọi chữ/control đều nhìn rõ và thao tác được; nếu đo được overflow thì Failed có ảnh, nếu chưa thấy lỗi thì MANUAL để hoàn tất kiểm mắt.',
'- IA-02-17: trường required của form hiện có được kiểm thuộc tính, browser validation/focus và không gửi request; trường xác nhận bị thiếu được kiểm riêng IA-02-05/13. Phone/address không được spec gọi là bắt buộc.',
'- IA-02-22: email dài >40 ký tự; chấp nhận full address không bị scroll clipping hoặc có title/aria-label đầy đủ. Nếu disabled và bị clip, không có tooltip, ghi Failed.',
'- IA-03-07: “không full reload” = không có document navigation request khi click link; thay URL bằng SPA mới đạt.',
'- IA-04-10: coi “Đổi mật khẩu thành công!” tương đương nghĩa “Đặt lại mật khẩu thành công”; alert được chấp nhận riêng item này vì Expected chỉ nói visible message. IA-04-11 yêu cầu toast/inline nên chỉ alert là Failed.',
'- IA-04-21: kết quả ghi theo fast double click đã chạy và OTP hiển thị có reset thành công; không suy ra tính đúng trong mọi thứ tự trả response.',
'- Không phát hiện item nào thực sự N/A: các chức năng/trường được Expected yêu cầu nhưng thiếu được ghi Failed; MANUAL giữ Chrome trống.',
'', '## Artifacts và bảo toàn workbook','',
'- `automation/execution-results.json`: actual, request/response, dialog, email, timestamp theo ID.',
'- `automation/playwright-results.json`: kết quả native của lượt đầy đủ 79 test; `automation/playwright-recheck-results.json`: lượt chạy lại 7 item sau khi sửa selector/dữ liệu automation; `automation/playwright-clipboard-results.json`: 2 item clipboard được chạy lại với thao tác kéo chọn bằng chuột và Ctrl+C/Ctrl+V thật. Kết quả cuối cùng theo ID nằm trong `execution-results.json` và Excel; MANUAL tương ứng skipped. IA-03-14 Passed sau khi phân biệt form tìm kiếm Home với form Login. `automation/playwright-email-results.json`: IA-02-03 chạy lại để chụp type email trước submit, tránh đăng nhập thành công bằng dữ liệu abc đã được tạo trong lượt trước.',
'- `automation/run-chrome.log`, `automation/run-chrome-recheck.log`, `automation/run-chrome-clipboard.log`, `automation/run-chrome-email.log`: log thực thi; `automation/playwright.config.js`, `automation/run-chrome.spec.js`: cấu hình/script.',
'- Chỉ Chrome, Notes, Screenshot được ghi trên Checklist. Summary đếm theo IA và tổng. Đã so với bản đầu vào: giá trị các cột còn lại, style mọi ô, dropdown, số/thứ tự dòng, merge, row/column dimensions được giữ nguyên.',
]
(ROOT/'checklist/execution-chrome.md').write_text('\n'.join(lines)+'\n')
print(json.dumps(dict(total),ensure_ascii=False));print('Workbook preservation comparison: OK' if original.exists() else 'Original comparison snapshot unavailable on this rerun')
