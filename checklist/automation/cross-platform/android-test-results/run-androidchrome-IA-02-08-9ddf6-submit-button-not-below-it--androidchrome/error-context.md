# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-02-08 Login errors are displayed above the submit button, not below it.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: Error y=482.2857360839844, bottom=530.2857055664062; submit y=390.2857360839844; error precedes submit=false; banner=Đăng nhập thất bại. Vui lòng kiểm tra lại.

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
        - heading "Đăng Ký" [level=2] [ref=f9e12]
        - generic [ref=f9e13]:
          - generic [ref=f9e14]:
            - generic [ref=f9e15]: Username
            - textbox [ref=f9e16]: tia0208.1793773085324.0@test.local
          - generic [ref=f9e17]:
            - generic [ref=f9e18]: Mật khẩu
            - textbox [ref=f9e19]: Wrong123!
          - link "Quên mật khẩu?" [ref=f9e21] [cursor=pointer]:
            - /url: /forgot-password
          - button "Sign In" [ref=f9e22] [cursor=pointer]
          - generic [ref=f9e23]:
            - text: Chưa có tài khoản?
            - link "Đăng ký ngay" [ref=f9e24] [cursor=pointer]:
              - /url: /register
        - generic [ref=f9e25]: Đăng nhập thất bại. Vui lòng kiểm tra lại.
    - contentinfo [ref=f9e26]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f9e27]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/login
```