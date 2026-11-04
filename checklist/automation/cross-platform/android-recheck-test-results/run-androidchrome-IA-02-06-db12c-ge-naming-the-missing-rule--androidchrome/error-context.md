# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-02-06 Password-strength validation accepts a valid FR-01 password and rejects weak ones with a message naming the missing rule.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: Password="Abc12345!"; accepted=false; requests=0; error=["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."]
Password="abc12345"; accepted=false; requests=0; error=["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."]
Password="Abcdefgh"; accepted=false; requests=0; error=["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."]
Password="Abc12345"; accepted=false; requests=0; error=["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [ref=f6e3]:
  - banner [ref=f6e4]:
    - link "EShop" [ref=f6e5] [cursor=pointer]:
      - /url: /
    - navigation [ref=f6e6]:
      - link "Giỏ hàng" [ref=f6e7] [cursor=pointer]:
        - /url: /cart
      - link "Đăng nhập" [ref=f6e8] [cursor=pointer]:
        - /url: /login
      - link "Đăng ký" [ref=f6e9] [cursor=pointer]:
        - /url: /register
  - main [ref=f6e10]:
    - generic [ref=f6e11]:
      - heading "Đăng Ký Tài Khoản" [level=2] [ref=f6e12]
      - generic [ref=f6e13]: Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT.
      - generic [ref=f6e14]:
        - generic [ref=f6e15]:
          - generic [ref=f6e16]: Họ Tên
          - textbox [ref=f6e17]: Chrome Tester
        - generic [ref=f6e18]:
          - generic [ref=f6e19]: Email
          - textbox [ref=f6e20]: tIA0206.1793773594465@test.local
        - generic [ref=f6e21]:
          - generic [ref=f6e22]: Mật khẩu
          - textbox [ref=f6e23]: Abc12345
          - paragraph [ref=f6e24]: "Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt."
        - button "Đăng Ký" [active] [ref=f6e25] [cursor=pointer]
        - generic [ref=f6e26]:
          - text: Đã có tài khoản?
          - link "Đăng nhập" [ref=f6e27] [cursor=pointer]:
            - /url: /login
  - contentinfo [ref=f6e28]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```