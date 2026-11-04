# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-02-03 Every email field uses `type="email"` and native HTML5 validation blocks malformed addresses.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: /login: before submit {"type":"text","typeMismatch":false,"message":"","value":"abc"}
/login: {"type":"text","typeMismatch":false,"message":"","value":"abc"}; requests=1
/register: before submit {"type":"text","typeMismatch":false,"message":"","value":"abc"}
/register: {"type":"text","typeMismatch":false,"message":"","value":"abc"}; requests=1
/forgot-password: before submit {"type":"text","typeMismatch":false,"message":"","value":"abc"}
/forgot-password: {"type":"text","typeMismatch":false,"message":"","value":"abc"}; requests=1

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
      - generic [ref=f5e8]:
        - link "Chào, Chrome Tester" [ref=f5e9] [cursor=pointer]:
          - /url: /profile
        - button "Thoát" [ref=f5e10] [cursor=pointer]
  - main [ref=f5e11]:
    - generic [ref=f5e12]:
      - heading "Quên Mật Khẩu" [level=2] [ref=f5e13]
      - generic [ref=f5e14]:
        - generic [ref=f5e15]: "Mã OTP của bạn là: 8326"
        - generic [ref=f5e16]:
          - generic [ref=f5e17]: Mã OTP (4 số)
          - textbox [ref=f5e18]
        - generic [ref=f5e19]:
          - generic [ref=f5e20]: Mật khẩu mới
          - textbox [ref=f5e21]
        - button "Đặt lại mật khẩu" [ref=f5e22] [cursor=pointer]
        - button "← Quay lại" [ref=f5e23] [cursor=pointer]
  - contentinfo [ref=f5e24]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```