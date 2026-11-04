# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-01-03 The page heading text describes the current screen, not another screen.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Heading="Đăng Ký"

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```