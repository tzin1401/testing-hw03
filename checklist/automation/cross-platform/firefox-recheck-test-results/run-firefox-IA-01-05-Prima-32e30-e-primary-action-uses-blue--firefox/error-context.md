# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-01-05 Primary and secondary actions are visually distinguishable; the positive primary action uses blue.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Primary=rgb(22, 163, 74); secondary=rgb(22, 163, 74)

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```