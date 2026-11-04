# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-04-07 An unknown email produces a generic, non-enumerating message and does not use a blocking `alert()`.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: dialogs=[{"type":"alert","text":"Lỗi: User not found"}]; inline errors=0; API=[{"url":"http://localhost:3000/api/forgot-password","status":404,"data":{"error":"User not found"}}]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```