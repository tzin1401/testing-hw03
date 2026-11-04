# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-04-20 After saving a new name, the header greeting updates without a reload.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Sau save: field="Tên Đã Cập Nhật"; greeting="Chào, Chrome Tester"; dialogs=[{"type":"alert","text":"Cập nhật thành công!"}]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```