# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-04 Every password field uses `type="password"` and masks typed characters.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: /login: password type=text
/register: password type=password
step2: password type=password

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```