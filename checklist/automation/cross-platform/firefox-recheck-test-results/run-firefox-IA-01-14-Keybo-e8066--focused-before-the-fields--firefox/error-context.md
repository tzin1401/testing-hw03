# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-01-14 Keyboard Tab order follows the visual top-to-bottom, left-to-right order; the submit button is not focused before the fields.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Initial Tab={"tag":"BUTTON","text":"Sign In","tabIndex":1}; from Email=["input0","input1","Quên mật khẩu?","Đăng ký ngay","Đăng ký ngay"]; submit tabIndex=1

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```