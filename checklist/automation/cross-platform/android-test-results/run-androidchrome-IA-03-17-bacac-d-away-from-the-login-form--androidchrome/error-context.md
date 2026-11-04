# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-03-17 An authenticated user visiting `/login` is redirected away from the login form.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: URL=http://localhost:5173/login; fields=2; header=EShop
Giỏ hàng
Chào, Chrome Tester
Thoát

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
        - generic [ref=f4e8]:
          - link "Chào, Chrome Tester" [ref=f4e9] [cursor=pointer]:
            - /url: /profile
          - button "Thoát" [ref=f4e10] [cursor=pointer]
    - main [ref=f4e11]:
      - generic [ref=f4e12]:
        - heading "Đăng Ký" [level=2] [ref=f4e13]
        - generic [ref=f4e14]:
          - generic [ref=f4e15]:
            - generic [ref=f4e16]: Username
            - textbox [ref=f4e17]
          - generic [ref=f4e18]:
            - generic [ref=f4e19]: Mật khẩu
            - textbox [ref=f4e20]
          - link "Quên mật khẩu?" [ref=f4e22] [cursor=pointer]:
            - /url: /forgot-password
          - button "Sign In" [ref=f4e23] [cursor=pointer]
          - generic [ref=f4e24]:
            - text: Chưa có tài khoản?
            - link "Đăng ký ngay" [ref=f4e25] [cursor=pointer]:
              - /url: /register
    - contentinfo [ref=f4e26]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f4e27]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/login
```