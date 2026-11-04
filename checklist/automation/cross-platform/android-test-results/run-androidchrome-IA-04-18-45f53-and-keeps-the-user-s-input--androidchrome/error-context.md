# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-04-18 When the API is unreachable or returns 5xx, the form shows a human-readable failure and keeps the user's input.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: /login: HTTP503; values retained=true; retry enabled=true; dialogs=[]; errors=["Đăng nhập thất bại. Vui lòng kiểm tra lại."]
/register: HTTP503; values retained=true; retry enabled=true; dialogs=[]; errors=["Service unavailable"]
fp1: HTTP503; values retained=true; retry enabled=true; dialogs=[{"type":"alert","text":"Lỗi: Service unavailable"}]; errors=[]
fp2: HTTP503; values retained=true; retry enabled=true; dialogs=[{"type":"alert","text":"Mã OTP không đúng hoặc có lỗi xảy ra."}]; errors=[]
/profile: HTTP503; values retained=true; retry enabled=true; dialogs=[{"type":"alert","text":"Lỗi cập nhật"}]; errors=[]

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
            - textbox [disabled] [ref=f8e18]: tia0418.1793773469533.0@test.local
          - generic [ref=f8e19]:
            - generic [ref=f8e20]: Họ Tên
            - textbox [ref=f8e21]: Chrome Tester
          - generic [ref=f8e22]:
            - generic [ref=f8e23]: Số điện thoại
            - 'textbox "VD: 0912345678" [ref=f8e24]': "912345678"
          - generic [ref=f8e25]:
            - generic [ref=f8e26]: Địa chỉ giao hàng
            - textbox "Nhập địa chỉ của bạn" [ref=f8e27]
          - button "Cập nhật" [ref=f8e28] [cursor=pointer]
      - generic [ref=f8e29]:
        - heading "Lịch sử đơn hàng" [level=2] [ref=f8e30]
        - paragraph [ref=f8e31]: Bạn chưa có đơn hàng nào.
  - contentinfo [ref=f8e32]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```