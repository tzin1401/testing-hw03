# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-03-04 The cart link shows a badge with the number of items in the cart.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: After adding 1 product, Profile via SPA: cart link text="Giỏ hàng"; HTML=Giỏ hàng
Cart state after add: Giỏ Hàng
Sản phẩm	Giá	Số lượng	Thành tiền	Thao tác
iPhone 15 Pro Max	30,000,000 ₫	1	30,000,000 ₫	Xóa
Tổng tạm tính: 30,000,000 ₫
← Mua tiếp
Tiến hành thanh toán

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
        - link "Giỏ hàng" [active] [ref=f3e7] [cursor=pointer]:
          - /url: /cart
        - generic [ref=f3e8]:
          - link "Chào, Chrome Tester" [ref=f3e9] [cursor=pointer]:
            - /url: /profile
          - button "Thoát" [ref=f3e10] [cursor=pointer]
    - main [ref=f3e11]:
      - generic [ref=f3e12]:
        - heading "Giỏ Hàng" [level=2] [ref=f3e13]
        - table [ref=f3e14]:
          - rowgroup [ref=f3e15]:
            - row [ref=f3e16]:
              - columnheader "Sản phẩm" [ref=f3e17]
              - columnheader "Giá" [ref=f3e18]
              - columnheader "Số lượng" [ref=f3e19]
              - columnheader "Thành tiền" [ref=f3e20]
              - columnheader "Thao tác" [ref=f3e21]
          - rowgroup [ref=f3e22]:
            - row [ref=f3e23]:
              - cell "iPhone 15 Pro Max" [ref=f3e24]
              - cell "30,000,000 ₫" [ref=f3e25]
              - cell "1" [ref=f3e26]
              - cell "30,000,000 ₫" [ref=f3e27]
              - cell [ref=f3e28]:
                - button "Xóa" [ref=f3e29] [cursor=pointer]
        - generic [ref=f3e30]:
          - generic [ref=f3e31]:
            - text: "Tổng tạm tính:"
            - generic [ref=f3e32]: 30,000,000 ₫
          - generic [ref=f3e33]:
            - link "← Mua tiếp" [ref=f3e34] [cursor=pointer]:
              - /url: /
            - button "Tiến hành thanh toán" [ref=f3e35] [cursor=pointer]
    - contentinfo [ref=f3e36]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f3e37]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/profile
```