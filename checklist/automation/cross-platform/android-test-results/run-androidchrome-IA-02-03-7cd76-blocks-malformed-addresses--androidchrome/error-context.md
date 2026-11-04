# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-androidchrome.spec.js >> IA-02-03 Every email field uses `type="email"` and native HTML5 validation blocks malformed addresses.
- Location: checklist/automation/run-androidchrome-shared.cjs:24:2

# Error details

```
Error: /login: before submit {"type":"text","typeMismatch":false,"message":"","value":"abc"}
/login: {"type":"text","typeMismatch":false,"message":"","value":"abc"}; requests=1
/register: before submit {"type":"text","typeMismatch":false,"message":"","value":"abc"}
locator.click: Timeout 10000ms exceeded.
Call log:
  - waiting for locator('main form').first().locator('button[type=submit]')
    - locator resolved to <button type="submit" class="w-full bg-red-500 text-white py-2 rounded hover:bg-red-600">Đăng Ký</button>
  - attempting click action
    - waiting for element to be visible, enabled and stable
    - element is visible, enabled and stable
    - scrolling into view if needed
    - done scrolling
    - <label class="block text-gray-700 mb-2">Email</label> from <div>…</div> subtree intercepts pointer events
  - retrying click action
    - waiting for element to be visible, enabled and stable
    - element is visible, enabled and stable
    - scrolling into view if needed
    - done scrolling
    - <label class="block text-gray-700 mb-2">Mật khẩu</label> from <div>…</div> subtree intercepts pointer events
  - retrying click action
    - waiting 20ms
    - waiting for element to be visible, enabled and stable
    - element is visible, enabled and stable
    - scrolling into view if needed
    - done scrolling
    - <label class="block text-gray-700 mb-2">Họ Tên</label> from <div>…</div> subtree intercepts pointer events
  2 × retrying click action
      - waiting 100ms
      - waiting for element to be visible, enabled and stable
      - element is visible, enabled and stable
      - scrolling into view if needed
      - done scrolling
      - <h2 class="text-2xl font-bold mb-6 text-center">Đăng Ký Tài Khoản</h2> intercepts pointer events
  3 × retrying click action
      - waiting 500ms
      - waiting for element to be visible, enabled and stable
      - element is visible, enabled and stable
      - scrolling into view if needed
      - done scrolling
      - <p class="text-xs text-gray-400 mt-1">Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thườn…</p> from <div>…</div> subtree intercepts pointer events
    - retrying click action
      - waiting 500ms
      - waiting for element to be visible, enabled and stable
      - element is visible, enabled and stable
      - scrolling into view if needed
      - done scrolling
      - <input required="" type="text" value="Chrome Tester" class="w-full border p-2 rounded"/> from <div>…</div> subtree intercepts pointer events
    - retrying click action
      - waiting 500ms
      - waiting for element to be visible, enabled and stable
      - element is visible, enabled and stable
      - scrolling into view if needed
      - done scrolling
      - <h2 class="text-2xl font-bold mb-6 text-center">Đăng Ký Tài Khoản</h2> intercepts pointer events
    - retrying click action
      - waiting 500ms
      - waiting for element to be visible, enabled and stable
      - element is visible, enabled and stable
      - scrolling into view if needed
      - done scrolling
      - <h2 class="text-2xl font-bold mb-6 text-center">Đăng Ký Tài Khoản</h2> intercepts pointer events
  - retrying click action
    - waiting 500ms
    - waiting for element to be visible, enabled and stable
    - element is visible, enabled and stable
    - scrolling into view if needed
    - done scrolling
    - <p class="text-xs text-gray-400 mt-1">Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thườn…</p> from <div>…</div> subtree intercepts pointer events
  - retrying click action
    - waiting 500ms
    - waiting for element to be visible, enabled and stable
    - element is visible, enabled and stable
    - scrolling into view if needed
    - done scrolling
    - <input required="" type="text" value="Chrome Tester" class="w-full border p-2 rounded"/> from <div>…</div> subtree intercepts pointer events
  - retrying click action
    - waiting 500ms
    - waiting for element to be visible, enabled and stable
    - element is visible, enabled and stable
    - scrolling into view if needed
    - done scrolling
    - <h2 class="text-2xl font-bold mb-6 text-center">Đăng Ký Tài Khoản</h2> intercepts pointer events
  - retrying click action
    - waiting 500ms

    at /home/zinn/zinn/testing/hw03/checklist/automation/run-androidchrome-shared.cjs:85:589

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [ref=f4e3]:
  - banner [ref=f4e4]:
    - link "EShop" [ref=f4e5] [cursor=pointer]:
      - /url: /
    - navigation [ref=f4e6]:
      - link "Giỏ hàng" [ref=f4e7] [cursor=pointer]:
        - /url: /cart
      - generic [ref=f4e8]:
        - link "Chào, Chrome Tester" [ref=f4e9] [cursor=pointer]:
          - /url: /profile
        - button "Thoát" [ref=f4e10] [cursor=pointer]
  - main [ref=f4e11]:
    - generic [ref=f4e12]:
      - heading "Đăng Ký Tài Khoản" [level=2] [ref=f4e13]
      - generic [ref=f4e14]:
        - generic [ref=f4e15]:
          - generic [ref=f4e16]: Họ Tên
          - textbox [ref=f4e17]: Chrome Tester
        - generic [ref=f4e18]:
          - generic [ref=f4e19]: Email
          - textbox [ref=f4e20]: abc
        - generic [ref=f4e21]:
          - generic [ref=f4e22]: Mật khẩu
          - textbox [active] [ref=f4e23]: Abc12345
          - paragraph [ref=f4e24]: "Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt."
        - button "Đăng Ký" [ref=f4e25] [cursor=pointer]
        - generic [ref=f4e26]:
          - text: Đã có tài khoản?
          - link "Đăng nhập" [ref=f4e27] [cursor=pointer]:
            - /url: /login
  - contentinfo [ref=f4e28]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```