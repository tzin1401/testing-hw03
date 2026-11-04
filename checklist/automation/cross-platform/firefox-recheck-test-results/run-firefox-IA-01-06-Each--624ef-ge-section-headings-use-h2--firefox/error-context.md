# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-01-06 Each page has exactly one `<h1>` describing the page; section headings use `<h2>`.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: /login: h1=[]; headings=["Đăng Ký"]
/register: h1=[]; headings=["Đăng Ký Tài Khoản"]
/forgot-password: h1=[]; headings=["Quên Mật Khẩu"]
/forgot-password#step2: h1=[]; headings=["Quên Mật Khẩu"]
/profile: h1=[]; headings=["Hồ sơ của bạn","Lịch sử đơn hàng"]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```