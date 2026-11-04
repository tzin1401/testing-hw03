# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-02-18 Email and password fields expose correct `autocomplete` hints for password managers.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: /login: [{"i":0,"type":"text","autocomplete":null,"label":"Username"},{"i":1,"type":"text","autocomplete":null,"label":"Mật khẩu"}]
/register: [{"i":1,"type":"text","autocomplete":null,"label":"Email"},{"i":2,"type":"password","autocomplete":null,"label":"Mật khẩu"}]
/forgot-password: [{"i":0,"type":"text","autocomplete":null,"label":"Nhập Email của bạn"}]
/forgot-password#step2: [{"i":1,"type":"password","autocomplete":null,"label":"Mật khẩu mới"}]
/profile: [{"i":0,"type":"text","autocomplete":null,"label":"Email (Không đổi)"}]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [ref=f24e3]:
  - banner [ref=f24e4]:
    - link "EShop" [ref=f24e5] [cursor=pointer]:
      - /url: /
    - navigation [ref=f24e6]:
      - link "Giỏ hàng" [ref=f24e7] [cursor=pointer]:
        - /url: /cart
      - generic [ref=f24e8]:
        - link "Chào, Chrome Tester" [ref=f24e9] [cursor=pointer]:
          - /url: /profile
        - button "Thoát" [ref=f24e10] [cursor=pointer]
  - main [ref=f24e11]:
    - generic [ref=f24e12]:
      - generic [ref=f24e13]:
        - heading "Hồ sơ của bạn" [level=2] [ref=f24e14]
        - generic [ref=f24e15]:
          - generic [ref=f24e16]:
            - generic [ref=f24e17]: Email (Không đổi)
            - textbox [disabled] [ref=f24e18]: tia0218.1793773165869.0@test.local
          - generic [ref=f24e19]:
            - generic [ref=f24e20]: Họ Tên
            - textbox [ref=f24e21]: Chrome Tester
          - generic [ref=f24e22]:
            - generic [ref=f24e23]: Số điện thoại
            - 'textbox "VD: 0912345678" [ref=f24e24]'
          - generic [ref=f24e25]:
            - generic [ref=f24e26]: Địa chỉ giao hàng
            - textbox "Nhập địa chỉ của bạn" [ref=f24e27]
          - button "Cập nhật" [ref=f24e28] [cursor=pointer]
      - generic [ref=f24e29]:
        - heading "Lịch sử đơn hàng" [level=2] [ref=f24e30]
        - paragraph [ref=f24e31]: Bạn chưa có đơn hàng nào.
  - contentinfo [ref=f24e32]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```