# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-01-08 Secondary help text is readable: at least 12px and a contrast ratio of at least 4.5:1 against its background.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Hint font-size=12px; color=rgb(156, 163, 175); background=rgb(255, 255, 255); contrast=2.539:1

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```