# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-01-20 User-entered name is shown as plain text and never rendered as HTML.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Greeting="Chào, x"; b nodes=1

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```