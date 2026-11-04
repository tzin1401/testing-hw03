# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-04-12 Profile errors are specific and actionable.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Invalid phone dialog="Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."
Failed save message="Lỗi cập nhật"

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```