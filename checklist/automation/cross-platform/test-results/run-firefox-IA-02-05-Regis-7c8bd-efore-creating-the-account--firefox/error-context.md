# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-05 Registration requires a confirmation-password field and rejects a mismatch before creating the account.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Labels=["Họ Tên","Email","Mật khẩu"]; confirmation field=false; không có trường để nhập mismatch/matching

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```