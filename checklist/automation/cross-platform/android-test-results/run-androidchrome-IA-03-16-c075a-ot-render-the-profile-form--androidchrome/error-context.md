# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-03-16 An unauthenticated visit to `/profile` does not render the profile form.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: URL=http://localhost:5173/profile; forms=0; main="Vui lòng đăng nhập"

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [active] [ref=f13e1]:
  - generic [ref=f13e3]:
    - banner [ref=f13e4]:
      - link "EShop" [ref=f13e5] [cursor=pointer]:
        - /url: /
      - navigation [ref=f13e6]:
        - link "Giỏ hàng" [ref=f13e7] [cursor=pointer]:
          - /url: /cart
        - link "Đăng nhập" [ref=f13e8] [cursor=pointer]:
          - /url: /login
        - link "Đăng ký" [ref=f13e9] [cursor=pointer]:
          - /url: /register
    - main [ref=f13e10]:
      - generic [ref=f13e11]: Vui lòng đăng nhập
    - contentinfo [ref=f13e12]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
  - generic [ref=f13e13]: 23120190 · Nguyễn Lê Thế Vinh · 23120190@student.hcmus.edu.vn · Android Chrome 124.0.6367.219 · Pixel_9 Android 15 (emulator) · http://localhost:5173/profile
```