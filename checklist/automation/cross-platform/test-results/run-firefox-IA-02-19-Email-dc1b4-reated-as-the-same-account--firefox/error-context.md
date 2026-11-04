# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-19 Emails that differ only in letter case or surrounding spaces are treated as the same account.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Register Test@EShop.com[space]: URL=http://localhost:5173/login; banner=[]
Login exact [space]TEST@eshop.com with correct Test1234!: URL=http://localhost:5173/login; error=["Đăng nhập thất bại. Vui lòng kiểm tra lại."]; seed password untouched

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```