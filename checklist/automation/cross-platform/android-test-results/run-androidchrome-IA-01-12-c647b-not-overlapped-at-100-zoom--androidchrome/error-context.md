# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-01-12 Header/footer keep a consistent height and position; the main content is not overlapped at 100% zoom.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: /login: [{"tag":"HEADER","y":0,"b":64,"h":64,"x":0,"w":412.19049072265625},{"tag":"MAIN","y":64,"b":758.0952758789062,"h":694.0952758789062,"x":0,"w":412.19049072265625},{"tag":"FOOTER","y":790.0952758789062,"b":846.0952758789062,"h":56,"x":0,"w":412.19049072265625}]
/register: [{"tag":"HEADER","y":0,"b":64,"h":64,"x":0,"w":412.19049072265625},{"tag":"MAIN","y":64,"b":758.0952758789062,"h":694.0952758789062,"x":0,"w":412.19049072265625},{"tag":"FOOTER","y":790.0952758789062,"b":846.0952758789062,"h":56,"x":0,"w":412.19049072265625}]
/forgot-password: [{"tag":"HEADER","y":0,"b":64,"h":64,"x":0,"w":412.19049072265625},{"tag":"MAIN","y":64,"b":758.0952758789062,"h":694.0952758789062,"x":0,"w":412.19049072265625},{"tag":"FOOTER","y":790.0952758789062,"b":846.0952758789062,"h":56,"x":0,"w":412.19049072265625}]
/forgot-password#step2: [{"tag":"HEADER","y":0,"b":64,"h":64,"x":0,"w":412.19049072265625},{"tag":"MAIN","y":64,"b":758.0952758789062,"h":694.0952758789062,"x":0,"w":412.19049072265625},{"tag":"FOOTER","y":790.0952758789062,"b":846.0952758789062,"h":56,"x":0,"w":412.19049072265625}]
/profile: [{"tag":"HEADER","y":0,"b":64,"h":64,"x":0,"w":412.19049072265625},{"tag":"MAIN","y":64,"b":790.4761962890625,"h":726.4761962890625,"x":0,"w":412.19049072265625},{"tag":"FOOTER","y":822.4761962890625,"b":878.4761962890625,"h":56,"x":0,"w":412.19049072265625}]
Header/footer geometry across screens=[{"r":"/login","s":[{"tag":"HEADER","y":0,"b":64,"h":64,"x":0,"w":412.19049072265625},{"tag":"MAIN","y":64,"b":758.0952758789062,"h":694.0952758789062,"x":0,"w":412.19049072265625},{"tag":"FOOTER","y":790.0952758789062,"b":846.0952758789062,"h":56,"x":0,"w":412.19049072265625}]},{"r":"/register","s":[{"tag":"HEADER","y":0,"b":64,"h":64,"x":0,"w":412.19049072265625},{"tag":"MAIN","y":64,"b":758.0952758789062,"h":694.0952758789062,"x":0,"w":412.19049072265625},{"tag":"FOOTER","y":790.0952758789062,"b":846.0952758789062,"h":56,"x":0,"w":412.19049072265625}]},{"r":"/forgot-password","s":[{"tag":"HEADER","y":0,"b":64,"h":64,"x":0,"w":412.19049072265625},{"tag":"MAIN","y":64,"b":758.0952758789062,"h":694.0952758789062,"x":0,"w":412.19049072265625},{"tag":"FOOTER","y":790.0952758789062,"b":846.0952758789062,"h":56,"x":0,"w":412.19049072265625}]},{"r":"/forgot-password#step2","s":[{"tag":"HEADER","y":0,"b":64,"h":64,"x":0,"w":412.19049072265625},{"tag":"MAIN","y":64,"b":758.0952758789062,"h":694.0952758789062,"x":0,"w":412.19049072265625},{"tag":"FOOTER","y":790.0952758789062,"b":846.0952758789062,"h":56,"x":0,"w":412.19049072265625}]},{"r":"/profile","s":[{"tag":"HEADER","y":0,"b":64,"h":64,"x":0,"w":412.19049072265625},{"tag":"MAIN","y":64,"b":790.4761962890625,"h":726.4761962890625,"x":0,"w":412.19049072265625},{"tag":"FOOTER","y":822.4761962890625,"b":878.4761962890625,"h":56,"x":0,"w":412.19049072265625}]}]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [active] [ref=f21e1]:
  - generic [ref=f21e3]:
    - banner [ref=f21e4]:
      - link "EShop" [ref=f21e5] [cursor=pointer]:
        - /url: /
      - navigation [ref=f21e6]:
        - link "Giỏ hàng" [ref=f21e7] [cursor=pointer]:
          - /url: /cart
        - generic [ref=f21e8]:
          - link "Chào, Chrome Tester" [ref=f21e9] [cursor=pointer]:
            - /url: /profile
          - button "Thoát" [ref=f21e10] [cursor=pointer]
    - main [ref=f21e11]:
      - generic [ref=f21e12]:
        - generic [ref=f21e13]:
          - heading "Hồ sơ của bạn" [level=2] [ref=f21e14]
          - generic [ref=f21e15]:
            - generic [ref=f21e16]:
              - generic [ref=f21e17]: Email (Không đổi)
              - textbox [disabled] [ref=f21e18]: tia0112.1793772942335.0@test.local
            - generic [ref=f21e19]:
              - generic [ref=f21e20]: Họ Tên
              - textbox [ref=f21e21]: Chrome Tester
            - generic [ref=f21e22]:
              - generic [ref=f21e23]: Số điện thoại
              - 'textbox "VD: 0912345678" [ref=f21e24]'
            - generic [ref=f21e25]:
              - generic [ref=f21e26]: Địa chỉ giao hàng
              - textbox "Nhập địa chỉ của bạn" [ref=f21e27]
            - button "Cập nhật" [ref=f21e28] [cursor=pointer]
        - generic [ref=f21e29]:
          - heading "Lịch sử đơn hàng" [level=2] [ref=f21e30]
          - paragraph [ref=f21e31]: Bạn chưa có đơn hàng nào.
    - contentinfo [ref=f21e32]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f21e33]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/profile
```