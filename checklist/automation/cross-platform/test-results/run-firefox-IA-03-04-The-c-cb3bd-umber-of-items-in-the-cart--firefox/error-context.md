# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-03-04 The cart link shows a badge with the number of items in the cart.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: After adding 1 product, Profile via SPA: cart link text="Giỏ hàng"; HTML=Giỏ hàng
Cart state after add: Giỏ Hàng
Sản phẩm	Giá	Số lượng	Thành tiền	Thao tác
iPhone 15 Pro Max	30,000,000 ₫	1	30,000,000 ₫	Xóa
Tổng tạm tính: 30,000,000 ₫
← Mua tiếp
Tiến hành thanh toán

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```