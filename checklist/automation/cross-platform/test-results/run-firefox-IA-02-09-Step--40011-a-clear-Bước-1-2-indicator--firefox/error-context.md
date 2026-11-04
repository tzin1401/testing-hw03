# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-09 Step 1 shows a clear "Bước 1 / 2" indicator.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Step 1: main text="Quên Mật Khẩu\nNhập Email của bạn\nLấy mã OTP"

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```