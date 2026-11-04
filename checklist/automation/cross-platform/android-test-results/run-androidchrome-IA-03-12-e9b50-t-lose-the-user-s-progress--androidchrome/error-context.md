# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-03-12 Refreshing the page on step 2 does not lose the user's progress.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: After refresh: fields=1; email/input=""; submit=Lấy mã OTP

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [active] [ref=f7e1]:
  - generic [ref=f7e3]:
    - banner [ref=f7e4]:
      - link "EShop" [ref=f7e5] [cursor=pointer]:
        - /url: /
      - navigation [ref=f7e6]:
        - link "Giỏ hàng" [ref=f7e7] [cursor=pointer]:
          - /url: /cart
        - link "Đăng nhập" [ref=f7e8] [cursor=pointer]:
          - /url: /login
        - link "Đăng ký" [ref=f7e9] [cursor=pointer]:
          - /url: /register
    - main [ref=f7e10]:
      - generic [ref=f7e11]:
        - heading "Quên Mật Khẩu" [level=2] [ref=f7e12]
        - generic [ref=f7e13]:
          - generic [ref=f7e14]:
            - generic [ref=f7e15]: Nhập Email của bạn
            - textbox [ref=f7e16]
          - button "Lấy mã OTP" [ref=f7e17] [cursor=pointer]
    - contentinfo [ref=f7e18]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f7e19]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/forgot-password
```