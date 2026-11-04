# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-04-11 Saving the profile gives visible confirmation and reflects the new values.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: Save feedback: inline/status=0; visible text contains success=false; dialogs=[{"type":"alert","text":"Cập nhật thành công!"}]; only alert is not toast/inline
After reload=["tia0411.1793773394149.0@test.local","Tên Đã Lưu","912345678","123 Đường thử nghiệm"]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [ref=f14e3]:
  - banner [ref=f14e4]:
    - link "EShop" [ref=f14e5] [cursor=pointer]:
      - /url: /
    - navigation [ref=f14e6]:
      - link "Giỏ hàng" [ref=f14e7] [cursor=pointer]:
        - /url: /cart
      - generic [ref=f14e8]:
        - link "Chào, Tên Đã Lưu" [ref=f14e9] [cursor=pointer]:
          - /url: /profile
        - button "Thoát" [ref=f14e10] [cursor=pointer]
  - main [ref=f14e11]:
    - generic [ref=f14e12]:
      - generic [ref=f14e13]:
        - heading "Hồ sơ của bạn" [level=2] [ref=f14e14]
        - generic [ref=f14e15]:
          - generic [ref=f14e16]:
            - generic [ref=f14e17]: Email (Không đổi)
            - textbox [disabled] [ref=f14e18]: tia0411.1793773394149.0@test.local
          - generic [ref=f14e19]:
            - generic [ref=f14e20]: Họ Tên
            - textbox [ref=f14e21]: Tên Đã Lưu
          - generic [ref=f14e22]:
            - generic [ref=f14e23]: Số điện thoại
            - 'textbox "VD: 0912345678" [ref=f14e24]': "912345678"
          - generic [ref=f14e25]:
            - generic [ref=f14e26]: Địa chỉ giao hàng
            - textbox "Nhập địa chỉ của bạn" [ref=f14e27]: 123 Đường thử nghiệm
          - button "Cập nhật" [ref=f14e28] [cursor=pointer]
      - generic [ref=f14e29]:
        - heading "Lịch sử đơn hàng" [level=2] [ref=f14e30]
        - paragraph [ref=f14e31]: Bạn chưa có đơn hàng nào.
  - contentinfo [ref=f14e32]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```