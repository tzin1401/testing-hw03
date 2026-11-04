# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-04-13 The empty order history uses an icon/illustration plus a friendly message, per FR-24.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: {"text":"Lịch sử đơn hàngBạn chưa có đơn hàng nào.","media":0,"before":"none","after":"none"}

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```