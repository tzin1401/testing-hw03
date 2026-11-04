# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-01-20 User-entered name is shown as plain text and never rendered as HTML.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: Greeting="Chào, x"; b nodes=1

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [ref=f5e1]:
  - generic [ref=f5e3]:
    - banner [ref=f5e4]:
      - link "EShop" [ref=f5e5] [cursor=pointer]:
        - /url: /
      - navigation [ref=f5e6]:
        - link "Giỏ hàng" [ref=f5e7] [cursor=pointer]:
          - /url: /cart
        - generic [ref=f5e8]:
          - link "Chào, x" [ref=f5e9] [cursor=pointer]:
            - /url: /profile
          - button "Thoát" [ref=f5e11] [cursor=pointer]
    - main [ref=f5e12]:
      - generic [ref=f5e13]:
        - generic [ref=f5e14]:
          - heading "Hồ sơ của bạn" [level=2] [ref=f5e15]
          - generic [ref=f5e16]:
            - generic [ref=f5e17]:
              - generic [ref=f5e18]: Email (Không đổi)
              - textbox [disabled] [ref=f5e19]: tia0120.1793773560795.0@test.local
            - generic [ref=f5e20]:
              - generic [ref=f5e21]: Họ Tên
              - textbox [ref=f5e22]: <b>x</b>
            - generic [ref=f5e23]:
              - generic [ref=f5e24]: Số điện thoại
              - 'textbox "VD: 0912345678" [ref=f5e25]': "912345678"
            - generic [ref=f5e26]:
              - generic [ref=f5e27]: Địa chỉ giao hàng
              - textbox "Nhập địa chỉ của bạn" [ref=f5e28]: 123 Đường thử nghiệm
            - button "Cập nhật" [ref=f5e29] [cursor=pointer]
        - generic [ref=f5e30]:
          - heading "Lịch sử đơn hàng" [level=2] [ref=f5e31]
          - paragraph [ref=f5e32]: Bạn chưa có đơn hàng nào.
    - contentinfo [ref=f5e33]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f5e34]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/profile
```