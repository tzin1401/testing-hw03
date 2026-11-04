# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-03-03 The navigation item for the current screen is visually highlighted.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: /login: active={"href":"/login","color":"rgb(255, 255, 255)","bg":"rgba(0, 0, 0, 0)","decoration":"none solid rgb(255, 255, 255)","fontWeight":"400","aria":null}; inactive={"href":"/login","color":"rgb(255, 255, 255)","bg":"rgba(0, 0, 0, 0)","decoration":"none solid rgb(255, 255, 255)","fontWeight":"400","aria":null}
/register: active={"href":"/register","color":"rgb(255, 255, 255)","bg":"rgba(0, 0, 0, 0)","decoration":"none solid rgb(255, 255, 255)","fontWeight":"400","aria":null}; inactive={"href":"/register","color":"rgb(255, 255, 255)","bg":"rgba(0, 0, 0, 0)","decoration":"none solid rgb(255, 255, 255)","fontWeight":"400","aria":null}
Profile active color=rgb(253, 224, 71), bg=rgba(0, 0, 0, 0); Home same link color=rgb(253, 224, 71), bg=rgba(0, 0, 0, 0)

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [ref=f16e3]:
  - banner [ref=f16e4]:
    - link "EShop" [ref=f16e5] [cursor=pointer]:
      - /url: /
    - navigation [ref=f16e6]:
      - link "Giỏ hàng" [ref=f16e7] [cursor=pointer]:
        - /url: /cart
      - generic [ref=f16e8]:
        - link "Chào, Chrome Tester" [ref=f16e9] [cursor=pointer]:
          - /url: /profile
        - button "Thoát" [ref=f16e10] [cursor=pointer]
  - main [ref=f16e11]:
    - generic [ref=f16e12]:
      - generic [ref=f16e13]:
        - heading "Danh sách sản phẩm" [level=1] [ref=f16e14]
        - generic [ref=f16e15]:
          - textbox "Tìm kiếm..." [ref=f16e16]
          - button "Tìm" [ref=f16e17] [cursor=pointer]
      - generic [ref=f16e18]:
        - generic [ref=f16e19]:
          - heading "iPhone 15 Pro Max" [level=2] [ref=f16e20]
          - paragraph [ref=f16e21]: 30,000,000 VND
          - generic [ref=f16e22]:
            - link "Xem chi tiết" [ref=f16e23] [cursor=pointer]:
              - /url: /product/1
            - button "Thêm vào giỏ" [ref=f16e24] [cursor=pointer]
        - generic [ref=f16e25]:
          - heading "Samsung Galaxy S24 Ultra" [level=2] [ref=f16e26]
          - paragraph [ref=f16e27]: 28,000,000 VND
          - generic [ref=f16e28]:
            - link "Xem chi tiết" [ref=f16e29] [cursor=pointer]:
              - /url: /product/2
            - button "Thêm vào giỏ" [ref=f16e30] [cursor=pointer]
        - generic [ref=f16e31]:
          - heading "MacBook Pro M3" [level=2] [ref=f16e32]
          - paragraph [ref=f16e33]: 45,000,000 VND
          - generic [ref=f16e34]:
            - link "Xem chi tiết" [ref=f16e35] [cursor=pointer]:
              - /url: /product/3
            - button "Thêm vào giỏ" [ref=f16e36] [cursor=pointer]
        - generic [ref=f16e37]:
          - heading "Tai nghe AirPods Pro 2" [level=2] [ref=f16e38]
          - paragraph [ref=f16e39]: 6,000,000 VND
          - generic [ref=f16e40]:
            - link "Xem chi tiết" [ref=f16e41] [cursor=pointer]:
              - /url: /product/4
            - button "Thêm vào giỏ" [ref=f16e42] [cursor=pointer]
        - generic [ref=f16e43]:
          - heading "Bàn phím cơ Keychron Q1" [level=2] [ref=f16e44]
          - paragraph [ref=f16e45]: 4,000,000 VND
          - generic [ref=f16e46]:
            - link "Xem chi tiết" [ref=f16e47] [cursor=pointer]:
              - /url: /product/5
            - button "Thêm vào giỏ" [ref=f16e48] [cursor=pointer]
      - heading "Hiển thị 5 sản phẩm" [level=1] [ref=f16e49]
  - contentinfo [ref=f16e50]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```