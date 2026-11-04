# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-02-01 Every required field has a `*` immediately next to its label.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: /login: [{"label":"Username","required":true,"disabled":false},{"label":"Mật khẩu","required":true,"disabled":false}]
/register: [{"label":"Họ Tên","required":true,"disabled":false},{"label":"Email","required":true,"disabled":false},{"label":"Mật khẩu","required":true,"disabled":false}]
/forgot-password: [{"label":"Nhập Email của bạn","required":true,"disabled":false}]
/forgot-password#step2: [{"label":"Mã OTP (4 số)","required":true,"disabled":false},{"label":"Mật khẩu mới","required":true,"disabled":false}]
/profile: [{"label":"Email (Không đổi)","required":false,"disabled":true},{"label":"Họ Tên","required":true,"disabled":false},{"label":"Số điện thoại","required":false,"disabled":false},{"label":"Địa chỉ giao hàng","required":false,"disabled":false}]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [ref=f26e3]:
  - banner [ref=f26e4]:
    - link "EShop" [ref=f26e5] [cursor=pointer]:
      - /url: /
    - navigation [ref=f26e6]:
      - link "Giỏ hàng" [ref=f26e7] [cursor=pointer]:
        - /url: /cart
      - generic [ref=f26e8]:
        - link "Chào, Chrome Tester" [ref=f26e9] [cursor=pointer]:
          - /url: /profile
        - button "Thoát" [ref=f26e10] [cursor=pointer]
  - main [ref=f26e11]:
    - generic [ref=f26e12]:
      - generic [ref=f26e13]:
        - heading "Hồ sơ của bạn" [level=2] [ref=f26e14]
        - generic [ref=f26e15]:
          - generic [ref=f26e16]:
            - generic [ref=f26e17]: Email (Không đổi)
            - textbox [disabled] [ref=f26e18]: tia0201.1793773007250.0@test.local
          - generic [ref=f26e19]:
            - generic [ref=f26e20]: Họ Tên
            - textbox [ref=f26e21]: Chrome Tester
          - generic [ref=f26e22]:
            - generic [ref=f26e23]: Số điện thoại
            - 'textbox "VD: 0912345678" [ref=f26e24]'
          - generic [ref=f26e25]:
            - generic [ref=f26e26]: Địa chỉ giao hàng
            - textbox "Nhập địa chỉ của bạn" [ref=f26e27]
          - button "Cập nhật" [ref=f26e28] [cursor=pointer]
      - generic [ref=f26e29]:
        - heading "Lịch sử đơn hàng" [level=2] [ref=f26e30]
        - paragraph [ref=f26e31]: Bạn chưa có đơn hàng nào.
  - contentinfo [ref=f26e32]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```