# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-02-02 Each input has a visible, programmatically associated label; clicking the label focuses the input; no field relies on its placeholder as the only label.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: /login: [{"id":"","for":"","disabled":false,"label":"Username","clickFocused":false},{"id":"","for":"","disabled":false,"label":"Mật khẩu","clickFocused":false}]
/register: [{"id":"","for":"","disabled":false,"label":"Họ Tên","clickFocused":false},{"id":"","for":"","disabled":false,"label":"Email","clickFocused":false},{"id":"","for":"","disabled":false,"label":"Mật khẩu","clickFocused":false}]
/forgot-password: [{"id":"","for":"","disabled":false,"label":"Nhập Email của bạn","clickFocused":false}]
/forgot-password#step2: [{"id":"","for":"","disabled":false,"label":"Mã OTP (4 số)","clickFocused":false},{"id":"","for":"","disabled":false,"label":"Mật khẩu mới","clickFocused":false}]
/profile: [{"id":"","for":"","disabled":true,"label":"Email (Không đổi)"},{"id":"","for":"","disabled":false,"label":"Họ Tên","clickFocused":false},{"id":"","for":"","disabled":false,"label":"Số điện thoại","clickFocused":false},{"id":"","for":"","disabled":false,"label":"Địa chỉ giao hàng","clickFocused":false}]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [ref=f8e3]:
  - banner [ref=f8e4]:
    - link "EShop" [ref=f8e5] [cursor=pointer]:
      - /url: /
    - navigation [ref=f8e6]:
      - link "Giỏ hàng" [ref=f8e7] [cursor=pointer]:
        - /url: /cart
      - generic [ref=f8e8]:
        - link "Chào, Chrome Tester" [ref=f8e9] [cursor=pointer]:
          - /url: /profile
        - button "Thoát" [ref=f8e10] [cursor=pointer]
  - main [ref=f8e11]:
    - generic [ref=f8e12]:
      - generic [ref=f8e13]:
        - heading "Hồ sơ của bạn" [level=2] [ref=f8e14]
        - generic [ref=f8e15]:
          - generic [ref=f8e16]:
            - generic [ref=f8e17]: Email (Không đổi)
            - textbox [disabled] [ref=f8e18]: tia0202.1793773017748.0@test.local
          - generic [ref=f8e19]:
            - generic [ref=f8e20]: Họ Tên
            - textbox [ref=f8e21]: Chrome Tester
          - generic [ref=f8e22]:
            - generic [ref=f8e23]: Số điện thoại
            - 'textbox "VD: 0912345678" [ref=f8e24]'
          - generic [ref=f8e25]:
            - generic [ref=f8e26]: Địa chỉ giao hàng
            - textbox "Nhập địa chỉ của bạn" [ref=f8e27]
          - button "Cập nhật" [ref=f8e28] [cursor=pointer]
      - generic [ref=f8e29]:
        - heading "Lịch sử đơn hàng" [level=2] [ref=f8e30]
        - paragraph [ref=f8e31]: Bạn chưa có đơn hàng nào.
  - contentinfo [ref=f8e32]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```