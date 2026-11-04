# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-01 Every required field has a `*` immediately next to its label.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: /login: [{"label":"Username","required":true,"disabled":false},{"label":"Mật khẩu","required":true,"disabled":false}]
/register: [{"label":"Họ Tên","required":true,"disabled":false},{"label":"Email","required":true,"disabled":false},{"label":"Mật khẩu","required":true,"disabled":false}]
/forgot-password: [{"label":"Nhập Email của bạn","required":true,"disabled":false}]
/forgot-password#step2: [{"label":"Mã OTP (4 số)","required":true,"disabled":false},{"label":"Mật khẩu mới","required":true,"disabled":false}]
/profile: [{"label":"Email (Không đổi)","required":false,"disabled":true},{"label":"Họ Tên","required":true,"disabled":false},{"label":"Số điện thoại","required":false,"disabled":false},{"label":"Địa chỉ giao hàng","required":false,"disabled":false}]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```