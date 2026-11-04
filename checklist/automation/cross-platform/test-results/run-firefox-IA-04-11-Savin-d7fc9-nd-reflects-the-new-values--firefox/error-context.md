# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-04-11 Saving the profile gives visible confirmation and reflects the new values.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Save feedback: inline/status=0; visible text contains success=false; dialogs=[{"type":"alert","text":"Cập nhật thành công!"}]; only alert is not toast/inline
After reload=["tia0411.1793772907582.0@test.local","Tên Đã Lưu","912345678","123 Đường thử nghiệm"]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```