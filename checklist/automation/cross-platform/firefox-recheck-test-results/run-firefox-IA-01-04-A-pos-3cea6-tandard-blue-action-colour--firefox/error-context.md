# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-01-04 A positive submit action uses the standard blue action colour.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Submit background=rgb(239, 68, 68); blue token=rgb(37, 99, 235)

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```