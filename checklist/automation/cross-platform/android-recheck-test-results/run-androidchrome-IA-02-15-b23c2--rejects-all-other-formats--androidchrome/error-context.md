# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-02-15 Phone validation accepts a leading 0 with 10–11 digits and rejects all other formats.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: Phone=0912345678; expectedValid=true; requests=0; persisted=null; dialog=[{"type":"alert","text":"Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."}]
Phone=09123456789; expectedValid=true; requests=0; persisted=null; dialog=[{"type":"alert","text":"Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."}]
Phone=912345678; expectedValid=false; requests=1; persisted="912345678"; dialog=[{"type":"alert","text":"Cập nhật thành công!"}]
Phone=091234567; expectedValid=false; requests=0; persisted=null; dialog=[{"type":"alert","text":"Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."}]
Phone=091234567890; expectedValid=false; requests=0; persisted=null; dialog=[{"type":"alert","text":"Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."}]
Phone=abc; expectedValid=false; requests=0; persisted=null; dialog=[{"type":"alert","text":"Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."}]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [ref=f5e3]:
  - banner [ref=f5e4]:
    - link "EShop" [ref=f5e5] [cursor=pointer]:
      - /url: /
    - navigation [ref=f5e6]:
      - link "Giỏ hàng" [ref=f5e7] [cursor=pointer]:
        - /url: /cart
      - generic [ref=f5e8]:
        - link "Chào, Phone Tester" [ref=f5e9] [cursor=pointer]:
          - /url: /profile
        - button "Thoát" [ref=f5e10] [cursor=pointer]
  - main [ref=f5e11]:
    - generic [ref=f5e12]:
      - generic [ref=f5e13]:
        - heading "Hồ sơ của bạn" [level=2] [ref=f5e14]
        - generic [ref=f5e15]:
          - generic [ref=f5e16]:
            - generic [ref=f5e17]: Email (Không đổi)
            - textbox [disabled] [ref=f5e18]: tia0215.1793773604916.0@test.local
          - generic [ref=f5e19]:
            - generic [ref=f5e20]: Họ Tên
            - textbox [ref=f5e21]: Phone Tester
          - generic [ref=f5e22]:
            - generic [ref=f5e23]: Số điện thoại
            - 'textbox "VD: 0912345678" [ref=f5e24]': abc
          - generic [ref=f5e25]:
            - generic [ref=f5e26]: Địa chỉ giao hàng
            - textbox "Nhập địa chỉ của bạn" [ref=f5e27]
          - button "Cập nhật" [ref=f5e28] [cursor=pointer]
      - generic [ref=f5e29]:
        - heading "Lịch sử đơn hàng" [level=2] [ref=f5e30]
        - paragraph [ref=f5e31]: Bạn chưa có đơn hàng nào.
  - contentinfo [ref=f5e32]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```