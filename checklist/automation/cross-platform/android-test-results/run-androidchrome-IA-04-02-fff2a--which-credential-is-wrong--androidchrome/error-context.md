# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-04-02 After repeated failures lock the account, the UI shows a lock message distinguishable from the wrong-password message, without revealing which credential is wrong.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: Banner="Đăng nhập thất bại. Vui lòng kiểm tra lại."; login responses=[{"url":"http://localhost:3000/api/login","status":401,"data":{"error":"Invalid email or password"}},{"url":"http://localhost:3000/api/login","status":401,"data":{"error":"Invalid email or password"}},{"url":"http://localhost:3000/api/login","status":403,"data":{"error":"Tài khoản đã bị khóa. Vui lòng thử lại sau."}}]

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
            - textbox [ref=f9e16]: tia0402.1793773330187.0@test.local
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