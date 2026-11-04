# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-11 Step 2 shows a clear "Bước 2 / 2" indicator.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Step 2: main text="Quên Mật Khẩu\nMã OTP của bạn là: 5744\nMã OTP (4 số)\nMật khẩu mới\nĐặt lại mật khẩu← Quay lại"

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```