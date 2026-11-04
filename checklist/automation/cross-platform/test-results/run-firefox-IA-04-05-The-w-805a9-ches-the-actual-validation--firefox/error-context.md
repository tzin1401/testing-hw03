# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-04-05 The weak-password message accurately lists the rule that failed and matches the actual validation.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Password Abc12345! rejected; message="Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."; đã đủ hoa/thường/số/! nhưng validator báo yếu
Whitespace password "Abc12345 " accepted=true; old error before resubmit=1; UI requires whitespace, allows only letters/digits/whitespace.

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```