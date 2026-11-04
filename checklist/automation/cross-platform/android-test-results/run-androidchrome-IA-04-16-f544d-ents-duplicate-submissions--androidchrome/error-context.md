# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-04-16 Clicking submit immediately shows a loading/disabled state and prevents duplicate submissions.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: /login: pending after 150ms disabled=false, aria-busy=null, spinner=0, label="Sign In", requests=2
/register: pending after 150ms disabled=false, aria-busy=null, spinner=0, label="Đăng Ký", requests=2
fp1: pending after 150ms disabled=false, aria-busy=null, spinner=0, label="Lấy mã OTP", requests=2
fp2: pending after 150ms disabled=false, aria-busy=null, spinner=0, label="Đặt lại mật khẩu", requests=2
/profile: pending after 150ms disabled=false, aria-busy=null, spinner=0, label="Cập nhật", requests=2

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [ref=f9e3]:
  - banner [ref=f9e4]:
    - link "EShop" [ref=f9e5] [cursor=pointer]:
      - /url: /
    - navigation [ref=f9e6]:
      - link "Giỏ hàng" [ref=f9e7] [cursor=pointer]:
        - /url: /cart
      - generic [ref=f9e8]:
        - link "Chào, Chrome Tester" [ref=f9e9] [cursor=pointer]:
          - /url: /profile
        - button "Thoát" [ref=f9e10] [cursor=pointer]
  - main [ref=f9e11]:
    - generic [ref=f9e12]:
      - generic [ref=f9e13]:
        - heading "Hồ sơ của bạn" [level=2] [ref=f9e14]
        - generic [ref=f9e15]:
          - generic [ref=f9e16]:
            - generic [ref=f9e17]: Email (Không đổi)
            - textbox [disabled] [ref=f9e18]: tia0416.1793773424330.0@test.local
          - generic [ref=f9e19]:
            - generic [ref=f9e20]: Họ Tên
            - textbox [ref=f9e21]: Chrome Tester
          - generic [ref=f9e22]:
            - generic [ref=f9e23]: Số điện thoại
            - 'textbox "VD: 0912345678" [ref=f9e24]': "912345678"
          - generic [ref=f9e25]:
            - generic [ref=f9e26]: Địa chỉ giao hàng
            - textbox "Nhập địa chỉ của bạn" [ref=f9e27]
          - button "Cập nhật" [ref=f9e28] [cursor=pointer]
      - generic [ref=f9e29]:
        - heading "Lịch sử đơn hàng" [level=2] [ref=f9e30]
        - paragraph [ref=f9e31]: Bạn chưa có đơn hàng nào.
  - contentinfo [ref=f9e32]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```