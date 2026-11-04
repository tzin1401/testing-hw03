# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-20 The new-password rule is shown before the user types, consistent with Register.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Register hint="Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt."; step2 contains hint=false; step2="Quên Mật Khẩu\nMã OTP của bạn là: 7020\nMã OTP (4 số)\nMật khẩu mới\nĐặt lại mật khẩu← Quay lại"

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```