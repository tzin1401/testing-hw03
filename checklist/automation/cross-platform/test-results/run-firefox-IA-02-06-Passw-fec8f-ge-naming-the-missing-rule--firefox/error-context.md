# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-06 Password-strength validation accepts a valid FR-01 password and rejects weak ones with a message naming the missing rule.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

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