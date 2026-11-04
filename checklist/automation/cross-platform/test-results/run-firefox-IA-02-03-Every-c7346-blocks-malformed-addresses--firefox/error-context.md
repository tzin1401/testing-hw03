# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-03 Every email field uses `type="email"` and native HTML5 validation blocks malformed addresses.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: /login: before submit {"type":"text","typeMismatch":false,"message":"","value":"abc"}
/login: {"type":"text","typeMismatch":false,"message":"","value":"abc"}; requests=1
/register: before submit {"type":"text","typeMismatch":false,"message":"","value":"abc"}
/register: {"type":"text","typeMismatch":false,"message":"","value":"abc"}; requests=1
/forgot-password: before submit {"type":"text","typeMismatch":false,"message":"","value":"abc"}
/forgot-password: {"type":"text","typeMismatch":false,"message":"","value":"abc"}; requests=1

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```