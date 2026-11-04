# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-14 Step-2 OTP/password errors are shown inline above the submit button, not through a blocking `alert()`.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: dialogs=[{"type":"alert","text":"Mã OTP không đúng hoặc có lỗi xảy ra."}]; inline errors=0; main="Quên Mật Khẩu\nMã OTP của bạn là: 5326\nMã OTP (4 số)\nMật khẩu mới\nĐặt lại mật khẩu← Quay lại"

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```