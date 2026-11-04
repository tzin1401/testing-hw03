# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-04-16 Clicking submit immediately shows a loading/disabled state and prevents duplicate submissions.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: /login: pending after 150ms disabled=false, aria-busy=null, spinner=0, label="Sign In", requests=2
/register: pending after 150ms disabled=false, aria-busy=null, spinner=0, label="Đăng Ký", requests=2
fp1: pending after 150ms disabled=false, aria-busy=null, spinner=0, label="Lấy mã OTP", requests=2
fp2: pending after 150ms disabled=false, aria-busy=null, spinner=0, label="Đặt lại mật khẩu", requests=2
/profile: pending after 150ms disabled=false, aria-busy=null, spinner=0, label="Cập nhật", requests=2

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```