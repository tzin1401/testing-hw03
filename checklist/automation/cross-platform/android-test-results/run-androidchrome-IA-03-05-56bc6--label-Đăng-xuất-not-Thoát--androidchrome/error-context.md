# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-03-05 The logout control uses the label "Đăng xuất", not "Thoát".
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: Logout label="Thoát"

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [active] [ref=f4e1]:
  - generic [ref=f4e3]:
    - banner [ref=f4e4]:
      - link "EShop" [ref=f4e5] [cursor=pointer]:
        - /url: /
      - navigation [ref=f4e6]:
        - link "Giỏ hàng" [ref=f4e7] [cursor=pointer]:
          - /url: /cart
        - generic [ref=f4e8]:
          - link "Chào, Chrome Tester" [ref=f4e9] [cursor=pointer]:
            - /url: /profile
          - button "Thoát" [ref=f4e10] [cursor=pointer]
    - main [ref=f4e11]:
      - generic [ref=f4e12]:
        - generic [ref=f4e13]:
          - heading "Hồ sơ của bạn" [level=2] [ref=f4e14]
          - generic [ref=f4e15]:
            - generic [ref=f4e16]:
              - generic [ref=f4e17]: Email (Không đổi)
              - textbox [disabled] [ref=f4e18]: tia0305.1793773239908.0@test.local
            - generic [ref=f4e19]:
              - generic [ref=f4e20]: Họ Tên
              - textbox [ref=f4e21]: Chrome Tester
            - generic [ref=f4e22]:
              - generic [ref=f4e23]: Số điện thoại
              - 'textbox "VD: 0912345678" [ref=f4e24]'
            - generic [ref=f4e25]:
              - generic [ref=f4e26]: Địa chỉ giao hàng
              - textbox "Nhập địa chỉ của bạn" [ref=f4e27]
            - button "Cập nhật" [ref=f4e28] [cursor=pointer]
        - generic [ref=f4e29]:
          - heading "Lịch sử đơn hàng" [level=2] [ref=f4e30]
          - paragraph [ref=f4e31]: Bạn chưa có đơn hàng nào.
    - contentinfo [ref=f4e32]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f4e33]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/profile
```