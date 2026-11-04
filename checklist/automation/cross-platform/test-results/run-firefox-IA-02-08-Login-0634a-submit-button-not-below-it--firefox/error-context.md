# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-08 Login errors are displayed above the submit button, not below it.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Error y=517, bottom=565; submit y=425; error precedes submit=false; banner=Đăng nhập thất bại. Vui lòng kiểm tra lại.

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```