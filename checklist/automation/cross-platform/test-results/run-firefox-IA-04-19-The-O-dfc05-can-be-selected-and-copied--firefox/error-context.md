# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-04-19 The OTP in the info box can be selected and copied.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Issued=2997; clipboard=""; selected=2997

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```