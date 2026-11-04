# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-02-12 The OTP is exactly 6 digits; the OTP input accepts 6 digits and rejects 5 or 7.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: Issued OTP=1041; digits=4; label=Mã OTP (4 số)
Input=12345; stored input=12345; dialog=Mã OTP không đúng hoặc có lỗi xảy ra.; input attributes={"type":"text","maxLength":-1,"minLength":-1,"pattern":""}
Input=1234567; stored input=1234567; dialog=Mã OTP không đúng hoặc có lỗi xảy ra.; input attributes={"type":"text","maxLength":-1,"minLength":-1,"pattern":""}

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```