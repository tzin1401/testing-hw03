# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-03-12 Refreshing the page on step 2 does not lose the user's progress.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: After refresh: fields=1; email/input=""; submit=Lấy mã OTP

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```