# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-02-07 Registering with an already-used email is rejected with a clear error and does not create a duplicate account.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: URL=http://localhost:5173/login; banner=[]; API=[{"url":"http://localhost:3000/api/register","status":200,"data":{"message":"User registered successfully","id":416}}]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [active] [ref=f3e1]:
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
        - heading "Đăng Ký" [level=2] [ref=f3e12]
        - generic [ref=f3e13]:
          - generic [ref=f3e14]:
            - generic [ref=f3e15]: Username
            - textbox [ref=f3e16]
          - generic [ref=f3e17]:
            - generic [ref=f3e18]: Mật khẩu
            - textbox [ref=f3e19]
          - link "Quên mật khẩu?" [ref=f3e21] [cursor=pointer]:
            - /url: /forgot-password
          - button "Sign In" [ref=f3e22] [cursor=pointer]
          - generic [ref=f3e23]:
            - text: Chưa có tài khoản?
            - link "Đăng ký ngay" [ref=f3e24] [cursor=pointer]:
              - /url: /register
    - contentinfo [ref=f3e25]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f3e26]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/login
```