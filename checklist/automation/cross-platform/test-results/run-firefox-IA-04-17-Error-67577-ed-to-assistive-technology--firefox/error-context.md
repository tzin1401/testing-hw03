# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-04-17 Error and success messages are announced to assistive technology.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Error={"text":"Đăng nhập thất bại. Vui lòng kiểm tra lại.","role":null,"live":null}
Success={"text":"Mã OTP của bạn là: 7061","role":null,"live":null}

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```