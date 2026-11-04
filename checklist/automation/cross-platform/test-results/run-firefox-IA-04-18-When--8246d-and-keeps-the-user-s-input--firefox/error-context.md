# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-04-18 When the API is unreachable or returns 5xx, the form shows a human-readable failure and keeps the user's input.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: /login: HTTP503; values retained=true; retry enabled=true; dialogs=[]; errors=["Đăng nhập thất bại. Vui lòng kiểm tra lại."]
/register: HTTP503; values retained=true; retry enabled=true; dialogs=[]; errors=["Service unavailable"]
fp1: HTTP503; values retained=true; retry enabled=true; dialogs=[{"type":"alert","text":"Lỗi: Service unavailable"}]; errors=[]
fp2: HTTP503; values retained=true; retry enabled=true; dialogs=[{"type":"alert","text":"Mã OTP không đúng hoặc có lỗi xảy ra."}]; errors=[]
/profile: HTTP503; values retained=true; retry enabled=true; dialogs=[{"type":"alert","text":"Lỗi cập nhật"}]; errors=[]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```