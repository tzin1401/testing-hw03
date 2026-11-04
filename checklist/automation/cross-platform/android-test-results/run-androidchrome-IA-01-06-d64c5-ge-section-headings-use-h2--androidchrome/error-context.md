# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-01-06 Each page has exactly one `<h1>` describing the page; section headings use `<h2>`.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: /login: h1=[]; headings=["Đăng Ký"]
/register: h1=[]; headings=["Đăng Ký Tài Khoản"]
/forgot-password: h1=[]; headings=["Quên Mật Khẩu"]
/forgot-password#step2: h1=[]; headings=["Quên Mật Khẩu"]
/profile: h1=[]; headings=["Hồ sơ của bạn","Lịch sử đơn hàng"]

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
            - textbox [disabled] [ref=f8e18]: tia0106.1793772903026.0@test.local
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