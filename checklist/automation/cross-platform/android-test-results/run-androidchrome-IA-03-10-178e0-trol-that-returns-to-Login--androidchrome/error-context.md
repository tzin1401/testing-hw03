# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-03-10 Step 1 provides a visible control that returns to Login.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: Controls matching Quay lại đăng nhập=0; URL=http://localhost:5173/forgot-password; visible actions=["Lấy mã OTP"]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [active] [ref=f9e1]:
  - generic [ref=f9e3]:
    - banner [ref=f9e4]:
      - link "EShop" [ref=f9e5] [cursor=pointer]:
        - /url: /
      - navigation [ref=f9e6]:
        - link "Giỏ hàng" [ref=f9e7] [cursor=pointer]:
          - /url: /cart
        - link "Đăng nhập" [ref=f9e8] [cursor=pointer]:
          - /url: /login
        - link "Đăng ký" [ref=f9e9] [cursor=pointer]:
          - /url: /register
    - main [ref=f9e10]:
      - generic [ref=f9e11]:
        - heading "Quên Mật Khẩu" [level=2] [ref=f9e12]
        - generic [ref=f9e13]:
          - generic [ref=f9e14]:
            - generic [ref=f9e15]: Nhập Email của bạn
            - textbox [ref=f9e16]
          - button "Lấy mã OTP" [ref=f9e17] [cursor=pointer]
    - contentinfo [ref=f9e18]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f9e19]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/forgot-password
```