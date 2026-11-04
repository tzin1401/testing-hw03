# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-03-07 The forgot-password link opens Forgot Password step 1.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: URL=http://localhost:5173/forgot-password; button=Lấy mã OTP; document navigation requests=1

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [active] [ref=f12e1]:
  - generic [ref=f12e3]:
    - banner [ref=f12e4]:
      - link "EShop" [ref=f12e5] [cursor=pointer]:
        - /url: /
      - navigation [ref=f12e6]:
        - link "Giỏ hàng" [ref=f12e7] [cursor=pointer]:
          - /url: /cart
        - link "Đăng nhập" [ref=f12e8] [cursor=pointer]:
          - /url: /login
        - link "Đăng ký" [ref=f12e9] [cursor=pointer]:
          - /url: /register
    - main [ref=f12e10]:
      - generic [ref=f12e11]:
        - heading "Quên Mật Khẩu" [level=2] [ref=f12e12]
        - generic [ref=f12e13]:
          - generic [ref=f12e14]:
            - generic [ref=f12e15]: Nhập Email của bạn
            - textbox [ref=f12e16]
          - button "Lấy mã OTP" [ref=f12e17] [cursor=pointer]
    - contentinfo [ref=f12e18]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f12e19]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/forgot-password
```