# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-04-04 A successful registration shows a visible success message.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: After registration URL=http://localhost:5173/login; main="Đăng Ký\nUsername\nMật khẩu\nQuên mật khẩu?\nSign In\nChưa có tài khoản? Đăng ký ngay"; dialogs=[]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```