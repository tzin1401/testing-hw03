# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-03-05 The logout control uses the label "Đăng xuất", not "Thoát".
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Logout label="Thoát"

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```