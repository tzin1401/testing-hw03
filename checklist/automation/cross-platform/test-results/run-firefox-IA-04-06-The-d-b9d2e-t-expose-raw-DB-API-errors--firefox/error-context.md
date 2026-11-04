# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-04-06 The duplicate-email error message is human-readable and does not expose raw DB/API errors.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: URL=http://localhost:5173/login; banner=[]; API=[{"url":"http://localhost:3000/api/register","status":200,"data":{"message":"User registered successfully","id":267}}]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```