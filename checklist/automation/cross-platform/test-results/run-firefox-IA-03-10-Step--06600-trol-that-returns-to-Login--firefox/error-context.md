# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-03-10 Step 1 provides a visible control that returns to Login.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Controls matching Quay lại đăng nhập=0; URL=http://localhost:5173/forgot-password; visible actions=["Lấy mã OTP"]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```