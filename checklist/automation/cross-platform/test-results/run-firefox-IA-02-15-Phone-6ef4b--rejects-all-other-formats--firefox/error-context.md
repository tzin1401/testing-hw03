# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-15 Phone validation accepts a leading 0 with 10–11 digits and rejects all other formats.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Phone=0912345678; expectedValid=true; requests=0; persisted=null; dialog=[{"type":"alert","text":"Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."}]
Phone=09123456789; expectedValid=true; requests=0; persisted=null; dialog=[{"type":"alert","text":"Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."}]
Phone=912345678; expectedValid=false; requests=1; persisted="912345678"; dialog=[{"type":"alert","text":"Cập nhật thành công!"}]
Phone=091234567; expectedValid=false; requests=0; persisted=null; dialog=[{"type":"alert","text":"Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."}]
Phone=091234567890; expectedValid=false; requests=0; persisted=null; dialog=[{"type":"alert","text":"Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."}]
Phone=abc; expectedValid=false; requests=0; persisted=null; dialog=[{"type":"alert","text":"Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."}]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```