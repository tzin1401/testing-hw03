# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-04-07 An unknown email produces a generic, non-enumerating message and does not use a blocking `alert()`.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: dialogs=[{"type":"alert","text":"Lỗi: User not found"}]; inline errors=0; API=[{"url":"http://localhost:3000/api/forgot-password","status":404,"data":{"error":"User not found"}}]

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
          - generic [ref=f3e14]:
            - generic [ref=f3e15]: Nhập Email của bạn
            - textbox [ref=f3e16]: tia0407.1793773369476.0@test.local.unknown
          - button "Lấy mã OTP" [ref=f3e17] [cursor=pointer]
    - contentinfo [ref=f3e18]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f3e19]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/forgot-password
```