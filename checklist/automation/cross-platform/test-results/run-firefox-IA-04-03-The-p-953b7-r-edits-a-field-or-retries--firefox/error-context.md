# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-04-03 The previous login error is cleared or updated when the user edits a field or retries.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: After editing password, old banners=1; text=["Đăng nhập thất bại. Vui lòng kiểm tra lại."]
Retry URL=http://localhost:5173/; banners=0

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```