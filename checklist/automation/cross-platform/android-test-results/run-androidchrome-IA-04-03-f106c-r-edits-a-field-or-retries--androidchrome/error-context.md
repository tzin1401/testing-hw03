# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-04-03 The previous login error is cleared or updated when the user edits a field or retries.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: After editing password, old banners=1; text=["Đăng nhập thất bại. Vui lòng kiểm tra lại."]
Retry URL=http://localhost:5173/; banners=0

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [active] [ref=f3e1]:
  - generic [ref=f3e3]:
    - banner [ref=f3e4]:
      - link "EShop" [ref=f3e5] [cursor=pointer]:
        - /url: /
      - navigation [ref=f3e6]:
        - link "Giỏ hàng" [ref=f3e7] [cursor=pointer]:
          - /url: /cart
        - generic [ref=f3e8]:
          - link "Chào, Chrome Tester" [ref=f3e9] [cursor=pointer]:
            - /url: /profile
          - button "Thoát" [ref=f3e10] [cursor=pointer]
    - main [ref=f3e11]:
      - generic [ref=f3e12]:
        - generic [ref=f3e13]:
          - heading "Danh sách sản phẩm" [level=1] [ref=f3e14]
          - generic [ref=f3e15]:
            - textbox "Tìm kiếm..." [ref=f3e16]
            - button "Tìm" [ref=f3e17] [cursor=pointer]
        - generic [ref=f3e18]:
          - generic [ref=f3e19]:
            - heading "iPhone 15 Pro Max" [level=2] [ref=f3e20]
            - paragraph [ref=f3e21]: 30,000,000 VND
            - generic [ref=f3e22]:
              - link "Xem chi tiết" [ref=f3e23] [cursor=pointer]:
                - /url: /product/1
              - button "Thêm vào giỏ" [ref=f3e24] [cursor=pointer]
          - generic [ref=f3e25]:
            - heading "Samsung Galaxy S24 Ultra" [level=2] [ref=f3e26]
            - paragraph [ref=f3e27]: 28,000,000 VND
            - generic [ref=f3e28]:
              - link "Xem chi tiết" [ref=f3e29] [cursor=pointer]:
                - /url: /product/2
              - button "Thêm vào giỏ" [ref=f3e30] [cursor=pointer]
          - generic [ref=f3e31]:
            - heading "MacBook Pro M3" [level=2] [ref=f3e32]
            - paragraph [ref=f3e33]: 45,000,000 VND
            - generic [ref=f3e34]:
              - link "Xem chi tiết" [ref=f3e35] [cursor=pointer]:
                - /url: /product/3
              - button "Thêm vào giỏ" [ref=f3e36] [cursor=pointer]
          - generic [ref=f3e37]:
            - heading "Tai nghe AirPods Pro 2" [level=2] [ref=f3e38]
            - paragraph [ref=f3e39]: 6,000,000 VND
            - generic [ref=f3e40]:
              - link "Xem chi tiết" [ref=f3e41] [cursor=pointer]:
                - /url: /product/4
              - button "Thêm vào giỏ" [ref=f3e42] [cursor=pointer]
          - generic [ref=f3e43]:
            - heading "Bàn phím cơ Keychron Q1" [level=2] [ref=f3e44]
            - paragraph [ref=f3e45]: 4,000,000 VND
            - generic [ref=f3e46]:
              - link "Xem chi tiết" [ref=f3e47] [cursor=pointer]:
                - /url: /product/5
              - button "Thêm vào giỏ" [ref=f3e48] [cursor=pointer]
        - heading "Hiển thị 5 sản phẩm" [level=1] [ref=f3e49]
    - contentinfo [ref=f3e50]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f3e51]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/login
```