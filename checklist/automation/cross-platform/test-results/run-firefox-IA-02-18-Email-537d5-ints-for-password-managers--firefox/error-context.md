# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-18 Email and password fields expose correct `autocomplete` hints for password managers.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: /login: [{"i":0,"type":"text","autocomplete":null,"label":"Username"},{"i":1,"type":"text","autocomplete":null,"label":"Mật khẩu"}]
/register: [{"i":1,"type":"text","autocomplete":null,"label":"Email"},{"i":2,"type":"password","autocomplete":null,"label":"Mật khẩu"}]
/forgot-password: [{"i":0,"type":"text","autocomplete":null,"label":"Nhập Email của bạn"}]
/forgot-password#step2: [{"i":1,"type":"password","autocomplete":null,"label":"Mật khẩu mới"}]
/profile: [{"i":0,"type":"text","autocomplete":null,"label":"Email (Không đổi)"}]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```