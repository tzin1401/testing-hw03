# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-02-04 Every password field uses `type="password"` and masks typed characters.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: /login: password type=text
/register: password type=password
step2: password type=password

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [ref=f5e3]:
  - banner [ref=f5e4]:
    - link "EShop" [ref=f5e5] [cursor=pointer]:
      - /url: /
    - navigation [ref=f5e6]:
      - link "Giỏ hàng" [ref=f5e7] [cursor=pointer]:
        - /url: /cart
      - link "Đăng nhập" [ref=f5e8] [cursor=pointer]:
        - /url: /login
      - link "Đăng ký" [ref=f5e9] [cursor=pointer]:
        - /url: /register
  - main [ref=f5e10]:
    - generic [ref=f5e11]:
      - heading "Quên Mật Khẩu" [level=2] [ref=f5e12]
      - generic [ref=f5e13]:
        - generic [ref=f5e14]: "Mã OTP của bạn là: 6202"
        - generic [ref=f5e15]:
          - generic [ref=f5e16]: Mã OTP (4 số)
          - textbox [ref=f5e17]
        - generic [ref=f5e18]:
          - generic [ref=f5e19]: Mật khẩu mới
          - textbox [active] [ref=f5e20]: Visible123!
        - button "Đặt lại mật khẩu" [ref=f5e21] [cursor=pointer]
        - button "← Quay lại" [ref=f5e22] [cursor=pointer]
  - contentinfo [ref=f5e23]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```