# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-04-02 After repeated failures lock the account, the UI shows a lock message distinguishable from the wrong-password message, without revealing which credential is wrong.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Banner="Đăng nhập thất bại. Vui lòng kiểm tra lại."; login responses=[{"url":"http://localhost:3000/api/login","status":401,"data":{"error":"Invalid email or password"}},{"url":"http://localhost:3000/api/login","status":401,"data":{"error":"Invalid email or password"}},{"url":"http://localhost:3000/api/login","status":403,"data":{"error":"Tài khoản đã bị khóa. Vui lòng thử lại sau."}}]

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```