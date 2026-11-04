# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-03-16 An unauthenticated visit to `/profile` does not render the profile form.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: URL=http://localhost:5173/profile; forms=0; main="Vui lòng đăng nhập"

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```