# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-04-17 Error and success messages are announced to assistive technology.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: Error={"text":"Đăng nhập thất bại. Vui lòng kiểm tra lại.","role":null,"live":null}
Success={"text":"Mã OTP của bạn là: 5824","role":null,"live":null}

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
      - heading "Quên Mật Khẩu" [level=2] [ref=f4e12]
      - generic [ref=f4e13]:
        - generic [ref=f4e14]: "Mã OTP của bạn là: 5824"
        - generic [ref=f4e15]:
          - generic [ref=f4e16]: Mã OTP (4 số)
          - textbox [ref=f4e17]
        - generic [ref=f4e18]:
          - generic [ref=f4e19]: Mật khẩu mới
          - textbox [ref=f4e20]
        - button "Đặt lại mật khẩu" [ref=f4e21] [cursor=pointer]
        - button "← Quay lại" [ref=f4e22] [cursor=pointer]
  - contentinfo [ref=f4e23]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```