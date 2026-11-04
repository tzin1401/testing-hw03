# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-02-14 Step-2 OTP/password errors are shown inline above the submit button, not through a blocking `alert()`.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: dialogs=[{"type":"alert","text":"Mã OTP không đúng hoặc có lỗi xảy ra."}]; inline errors=0; main="Quên Mật Khẩu\nMã OTP của bạn là: 5181\nMã OTP (4 số)\nMật khẩu mới\nĐặt lại mật khẩu← Quay lại"

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [ref=f3e1]:
  - generic [ref=f3e3]:
    - banner [ref=f3e4]:
      - link "EShop" [ref=f3e5] [cursor=pointer]:
        - /url: /
      - navigation [ref=f3e6]:
        - link "Giỏ hàng" [ref=f3e7] [cursor=pointer]:
          - /url: /cart
        - link "Đăng nhập" [ref=f3e8] [cursor=pointer]:
          - /url: /login
        - link "Đăng ký" [ref=f3e9] [cursor=pointer]:
          - /url: /register
    - main [ref=f3e10]:
      - generic [ref=f3e11]:
        - heading "Quên Mật Khẩu" [level=2] [ref=f3e12]
        - generic [ref=f3e13]:
          - generic [ref=f3e14]: "Mã OTP của bạn là: 5181"
          - generic [ref=f3e15]:
            - generic [ref=f3e16]: Mã OTP (4 số)
            - textbox [ref=f3e17]: "000000"
          - generic [ref=f3e18]:
            - generic [ref=f3e19]: Mật khẩu mới
            - textbox [ref=f3e20]: Newpass123
          - button "Đặt lại mật khẩu" [ref=f3e21] [cursor=pointer]
          - button "← Quay lại" [ref=f3e22] [cursor=pointer]
    - contentinfo [ref=f3e23]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f3e24]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/forgot-password
```