# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-01-08 Secondary help text is readable: at least 12px and a contrast ratio of at least 4.5:1 against its background.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: Hint font-size=12px; color=rgb(156, 163, 175); background=rgb(255, 255, 255); contrast=2.539:1

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [active] [ref=f11e1]:
  - generic [ref=f11e3]:
    - banner [ref=f11e4]:
      - link "EShop" [ref=f11e5] [cursor=pointer]:
        - /url: /
      - navigation [ref=f11e6]:
        - link "Giỏ hàng" [ref=f11e7] [cursor=pointer]:
          - /url: /cart
        - link "Đăng nhập" [ref=f11e8] [cursor=pointer]:
          - /url: /login
        - link "Đăng ký" [ref=f11e9] [cursor=pointer]:
          - /url: /register
    - main [ref=f11e10]:
      - generic [ref=f11e11]:
        - heading "Đăng Ký Tài Khoản" [level=2] [ref=f11e12]
        - generic [ref=f11e13]:
          - generic [ref=f11e14]:
            - generic [ref=f11e15]: Họ Tên
            - textbox [ref=f11e16]
          - generic [ref=f11e17]:
            - generic [ref=f11e18]: Email
            - textbox [ref=f11e19]
          - generic [ref=f11e20]:
            - generic [ref=f11e21]: Mật khẩu
            - textbox [ref=f11e22]
            - paragraph [ref=f11e23]: "Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt."
          - button "Đăng Ký" [ref=f11e24] [cursor=pointer]
          - generic [ref=f11e25]:
            - text: Đã có tài khoản?
            - link "Đăng nhập" [ref=f11e26] [cursor=pointer]:
              - /url: /login
    - contentinfo [ref=f11e27]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f11e28]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/register
```