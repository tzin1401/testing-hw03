# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-22 A long email in the read-only field is fully readable.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: {"value":"tia0222.1793772775826.0.longemailsegmentlongemailsegment@test.local","length":67,"disabled":true,"clientWidth":253,"scrollWidth":541,"title":"","ariaLabel":null}

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```