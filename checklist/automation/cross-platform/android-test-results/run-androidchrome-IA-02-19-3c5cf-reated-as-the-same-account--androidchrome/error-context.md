# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-02-19 Emails that differ only in letter case or surrounding spaces are treated as the same account.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: Register Test@EShop.com[space]: URL=http://localhost:5173/login; banner=[]
Login exact [space]TEST@eshop.com with correct Test1234!: URL=http://localhost:5173/login; error=["Đăng nhập thất bại. Vui lòng kiểm tra lại."]; seed password untouched

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
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
      - heading "Đăng Ký" [level=2] [ref=f4e12]
      - generic [ref=f4e13]:
        - generic [ref=f4e14]:
          - generic [ref=f4e15]: Username
          - textbox [ref=f4e16]: TEST@eshop.com
        - generic [ref=f4e17]:
          - generic [ref=f4e18]: Mật khẩu
          - textbox [ref=f4e19]: Test1234!
        - link "Quên mật khẩu?" [ref=f4e21] [cursor=pointer]:
          - /url: /forgot-password
        - button "Sign In" [active] [ref=f4e22] [cursor=pointer]
        - generic [ref=f4e23]:
          - text: Chưa có tài khoản?
          - link "Đăng ký ngay" [ref=f4e24] [cursor=pointer]:
            - /url: /register
      - generic [ref=f4e25]: Đăng nhập thất bại. Vui lòng kiểm tra lại.
  - contentinfo [ref=f4e26]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```