# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-03-17 An authenticated user visiting `/login` is redirected away from the login form.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: URL=http://localhost:5173/login; fields=2; header=EShop
Giỏ hàng
Chào, Cross firefox Tester
Thoát

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```