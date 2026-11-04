# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-01-13 A long display name does not break the header layout.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: /login: greeting={"text":"Chào, NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN","color":"rgb(253, 224, 71)","bg":"rgba(0, 0, 0, 0)","effectiveBg":"rgb(37, 99, 235)","font":"ui-sans-serif, system-ui, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Noto Color Emoji\"","size":"16px","weight":"400","padding":"0px","maxWidth":"none","border":"0px solid rgb(229, 231, 235)","radius":"0px","outline":"rgb(253, 224, 71) none 0px","shadow":"none","x":136.10714721679688,"y":16,"w":684.8452758789062,"h":48,"right":820.9524230957031,"bottom":64}; logout={"text":"Thoát","color":"rgb(255, 255, 255)","bg":"rgb(239, 68, 68)","effectiveBg":"rgb(239, 68, 68)","font":"ui-sans-serif, system-ui, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Noto Color Emoji\"","size":"16px","weight":"400","padding":"4px 12px","maxWidth":"none","border":"0px solid rgb(229, 231, 235)","radius":"4px","outline":"rgb(255, 255, 255) none 0px","shadow":"none","x":836.952392578125,"y":24,"w":65.42262268066406,"h":32,"right":902.3750152587891,"bottom":56}; navRight=902.3750381469727
/register: greeting={"text":"Chào, NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN","color":"rgb(253, 224, 71)","bg":"rgba(0, 0, 0, 0)","effectiveBg":"rgb(37, 99, 235)","font":"ui-sans-serif, system-ui, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Noto Color Emoji\"","size":"16px","weight":"400","padding":"0px","maxWidth":"none","border":"0px solid rgb(229, 231, 235)","radius":"0px","outline":"rgb(253, 224, 71) none 0px","shadow":"none","x":136.10714721679688,"y":16,"w":684.8452758789062,"h":48,"right":820.9524230957031,"bottom":64}; logout={"text":"Thoát","color":"rgb(255, 255, 255)","bg":"rgb(239, 68, 68)","effectiveBg":"rgb(239, 68, 68)","font":"ui-sans-serif, system-ui, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Noto Color Emoji\"","size":"16px","weight":"400","padding":"4px 12px","maxWidth":"none","border":"0px solid rgb(229, 231, 235)","radius":"4px","outline":"rgb(255, 255, 255) none 0px","shadow":"none","x":836.952392578125,"y":24,"w":65.42262268066406,"h":32,"right":902.3750152587891,"bottom":56}; navRight=902.3750381469727
/forgot-password: greeting={"text":"Chào, NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN","color":"rgb(253, 224, 71)","bg":"rgba(0, 0, 0, 0)","effectiveBg":"rgb(37, 99, 235)","font":"ui-sans-serif, system-ui, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Noto Color Emoji\"","size":"16px","weight":"400","padding":"0px","maxWidth":"none","border":"0px solid rgb(229, 231, 235)","radius":"0px","outline":"rgb(253, 224, 71) none 0px","shadow":"none","x":136.10714721679688,"y":16,"w":684.8452758789062,"h":48,"right":820.9524230957031,"bottom":64}; logout={"text":"Thoát","color":"rgb(255, 255, 255)","bg":"rgb(239, 68, 68)","effectiveBg":"rgb(239, 68, 68)","font":"ui-sans-serif, system-ui, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Noto Color Emoji\"","size":"16px","weight":"400","padding":"4px 12px","maxWidth":"none","border":"0px solid rgb(229, 231, 235)","radius":"4px","outline":"rgb(255, 255, 255) none 0px","shadow":"none","x":836.952392578125,"y":24,"w":65.42262268066406,"h":32,"right":902.3750152587891,"bottom":56}; navRight=902.3750381469727
/forgot-password#step2: greeting={"text":"Chào, NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN","color":"rgb(253, 224, 71)","bg":"rgba(0, 0, 0, 0)","effectiveBg":"rgb(37, 99, 235)","font":"ui-sans-serif, system-ui, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Noto Color Emoji\"","size":"16px","weight":"400","padding":"0px","maxWidth":"none","border":"0px solid rgb(229, 231, 235)","radius":"0px","outline":"rgb(253, 224, 71) none 0px","shadow":"none","x":136.10714721679688,"y":16,"w":684.8452758789062,"h":48,"right":820.9524230957031,"bottom":64}; logout={"text":"Thoát","color":"rgb(255, 255, 255)","bg":"rgb(239, 68, 68)","effectiveBg":"rgb(239, 68, 68)","font":"ui-sans-serif, system-ui, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Noto Color Emoji\"","size":"16px","weight":"400","padding":"4px 12px","maxWidth":"none","border":"0px solid rgb(229, 231, 235)","radius":"4px","outline":"rgb(255, 255, 255) none 0px","shadow":"none","x":836.952392578125,"y":24,"w":65.42262268066406,"h":32,"right":902.3750152587891,"bottom":56}; navRight=902.3750381469727
/profile: greeting={"text":"Chào, NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN","color":"rgb(253, 224, 71)","bg":"rgba(0, 0, 0, 0)","effectiveBg":"rgb(37, 99, 235)","font":"ui-sans-serif, system-ui, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Noto Color Emoji\"","size":"16px","weight":"400","padding":"0px","maxWidth":"none","border":"0px solid rgb(229, 231, 235)","radius":"0px","outline":"rgb(253, 224, 71) none 0px","shadow":"none","x":136.10714721679688,"y":16,"w":684.8452758789062,"h":48,"right":820.9524230957031,"bottom":64}; logout={"text":"Thoát","color":"rgb(255, 255, 255)","bg":"rgb(239, 68, 68)","effectiveBg":"rgb(239, 68, 68)","font":"ui-sans-serif, system-ui, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Noto Color Emoji\"","size":"16px","weight":"400","padding":"4px 12px","maxWidth":"none","border":"0px solid rgb(229, 231, 235)","radius":"4px","outline":"rgb(255, 255, 255) none 0px","shadow":"none","x":836.952392578125,"y":24,"w":65.42262268066406,"h":32,"right":902.3750152587891,"bottom":56}; navRight=902.3750381469727

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [ref=f8e3]:
  - banner [ref=f8e4]:
    - link "EShop" [ref=f8e5] [cursor=pointer]:
      - /url: /
    - navigation [ref=f8e6]:
      - link "Giỏ hàng" [ref=f8e7] [cursor=pointer]:
        - /url: /cart
      - generic [ref=f8e8]:
        - link "Chào, NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN" [ref=f8e9] [cursor=pointer]:
          - /url: /profile
        - button "Thoát" [ref=f8e10] [cursor=pointer]
  - main [ref=f8e11]:
    - generic [ref=f8e12]:
      - generic [ref=f8e13]:
        - heading "Hồ sơ của bạn" [level=2] [ref=f8e14]
        - generic [ref=f8e15]:
          - generic [ref=f8e16]:
            - generic [ref=f8e17]: Email (Không đổi)
            - textbox [disabled] [ref=f8e18]: tia0113.1793772952893.0@test.local
          - generic [ref=f8e19]:
            - generic [ref=f8e20]: Họ Tên
            - textbox [ref=f8e21]: NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
          - generic [ref=f8e22]:
            - generic [ref=f8e23]: Số điện thoại
            - 'textbox "VD: 0912345678" [ref=f8e24]': "912345678"
          - generic [ref=f8e25]:
            - generic [ref=f8e26]: Địa chỉ giao hàng
            - textbox "Nhập địa chỉ của bạn" [ref=f8e27]
          - button "Cập nhật" [ref=f8e28] [cursor=pointer]
      - generic [ref=f8e29]:
        - heading "Lịch sử đơn hàng" [level=2] [ref=f8e30]
        - paragraph [ref=f8e31]: Bạn chưa có đơn hàng nào.
  - contentinfo [ref=f8e32]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```