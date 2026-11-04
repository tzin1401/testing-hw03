# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-04-20 After saving a new name, the header greeting updates without a reload.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: Sau save: field="Tên Đã Cập Nhật"; greeting="Chào, Chrome Tester"; dialogs=[{"type":"alert","text":"Cập nhật thành công!"}]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [ref=f7e1]:
  - generic [ref=f7e3]:
    - banner [ref=f7e4]:
      - link "EShop" [ref=f7e5] [cursor=pointer]:
        - /url: /
      - navigation [ref=f7e6]:
        - link "Giỏ hàng" [ref=f7e7] [cursor=pointer]:
          - /url: /cart
        - generic [ref=f7e8]:
          - link "Chào, Chrome Tester" [ref=f7e9] [cursor=pointer]:
            - /url: /profile
          - button "Thoát" [ref=f7e10] [cursor=pointer]
    - main [ref=f7e11]:
      - generic [ref=f7e12]:
        - generic [ref=f7e13]:
          - heading "Hồ sơ của bạn" [level=2] [ref=f7e14]
          - generic [ref=f7e15]:
            - generic [ref=f7e16]:
              - generic [ref=f7e17]: Email (Không đổi)
              - textbox [disabled] [ref=f7e18]: tia0420.1793773499006.0@test.local
            - generic [ref=f7e19]:
              - generic [ref=f7e20]: Họ Tên
              - textbox [ref=f7e21]: Tên Đã Cập Nhật
            - generic [ref=f7e22]:
              - generic [ref=f7e23]: Số điện thoại
              - 'textbox "VD: 0912345678" [ref=f7e24]': "912345678"
            - generic [ref=f7e25]:
              - generic [ref=f7e26]: Địa chỉ giao hàng
              - textbox "Nhập địa chỉ của bạn" [ref=f7e27]: 123 Đường thử nghiệm
            - button "Cập nhật" [ref=f7e28] [cursor=pointer]
        - generic [ref=f7e29]:
          - heading "Lịch sử đơn hàng" [level=2] [ref=f7e30]
          - paragraph [ref=f7e31]: Bạn chưa có đơn hàng nào.
    - contentinfo [ref=f7e32]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f7e33]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/profile
```