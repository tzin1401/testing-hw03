# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-02 Each input has a visible, programmatically associated label; clicking the label focuses the input; no field relies on its placeholder as the only label.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: /login: [{"id":"","for":"","disabled":false,"label":"Username","clickFocused":false},{"id":"","for":"","disabled":false,"label":"Mật khẩu","clickFocused":false}]
/register: [{"id":"","for":"","disabled":false,"label":"Họ Tên","clickFocused":false},{"id":"","for":"","disabled":false,"label":"Email","clickFocused":false},{"id":"","for":"","disabled":false,"label":"Mật khẩu","clickFocused":false}]
/forgot-password: [{"id":"","for":"","disabled":false,"label":"Nhập Email của bạn","clickFocused":false}]
/forgot-password#step2: [{"id":"","for":"","disabled":false,"label":"Mã OTP (4 số)","clickFocused":false},{"id":"","for":"","disabled":false,"label":"Mật khẩu mới","clickFocused":false}]
/profile: [{"id":"","for":"","disabled":true,"label":"Email (Không đổi)"},{"id":"","for":"","disabled":false,"label":"Họ Tên","clickFocused":false},{"id":"","for":"","disabled":false,"label":"Số điện thoại","clickFocused":false},{"id":"","for":"","disabled":false,"label":"Địa chỉ giao hàng","clickFocused":false}]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```