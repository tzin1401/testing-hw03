# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-02-20 The new-password rule is shown before the user types, consistent with Register.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: Register hint="Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt."; step2 contains hint=false; step2="Quên Mật Khẩu\nMã OTP của bạn là: 2837\nMã OTP (4 số)\nMật khẩu mới\nĐặt lại mật khẩu← Quay lại"

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [active] [ref=f4e1]:
  - generic [ref=f4e3]:
    - banner [ref=f4e4]:
      - link "EShop" [ref=f4e5] [cursor=pointer]:
        - /url: /
      - navigation [ref=f4e6]:
        - link "Giỏ hàng" [ref=f4e7] [cursor=pointer]:
          - /url: /cart
        - link "Đăng nhập" [ref=f4e8] [cursor=pointer]:
          - /url: /login
        - link "Đăng ký" [ref=f4e9] [cursor=pointer]:
          - /url: /register
    - main [ref=f4e10]:
      - generic [ref=f4e11]:
        - heading "Quên Mật Khẩu" [level=2] [ref=f4e12]
        - generic [ref=f4e13]:
          - generic [ref=f4e14]: "Mã OTP của bạn là: 2837"
          - generic [ref=f4e15]:
            - generic [ref=f4e16]: Mã OTP (4 số)
            - textbox [ref=f4e17]
          - generic [ref=f4e18]:
            - generic [ref=f4e19]: Mật khẩu mới
            - textbox [ref=f4e20]
          - button "Đặt lại mật khẩu" [ref=f4e21] [cursor=pointer]
          - button "← Quay lại" [ref=f4e22] [cursor=pointer]
    - contentinfo [ref=f4e23]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f4e24]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/forgot-password
```