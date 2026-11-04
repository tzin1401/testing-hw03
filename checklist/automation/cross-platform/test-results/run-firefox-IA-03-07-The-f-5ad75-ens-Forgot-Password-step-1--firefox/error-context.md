# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-03-07 The forgot-password link opens Forgot Password step 1.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: URL=http://localhost:5173/forgot-password; button=Lấy mã OTP; document navigation requests=1

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```