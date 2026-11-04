# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-01-01 The account field label uses the Vietnamese term defined by the screen's requirement, not an English alternative.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Label="Username"

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```