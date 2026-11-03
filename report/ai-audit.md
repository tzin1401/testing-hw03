# AI Audit Report — HW03 GUI & Usability

- Sinh viên: Nguyễn Lê Thế Vinh — 23120190
- Bài: HW03-AI — GUI & Usability (SUT: EShop)

**Declaration:** I use AI tools for the following tasks.

| # | Bước | Công cụ AI | Ngày giờ | Link |
|---|---|---|---|---|
| 1 | P01 — UI inventory (account screens) | OpenCode — DeepSeek V4.1 Flash Free | 04/11/2026 00:54 | [#1](#1) |
| 2 | P02 — Checklist IA-01 | OpenCode — DeepSeek V4.1 Flash Free | 04/11/2026 01:19 | [#2](#2) |
| 3 | P03 — Checklist IA-02 | OpenCode — DeepSeek V4.1 Flash Free | 04/11/2026 01:23 | [#3](#3) |
| 4 | P04 — Checklist IA-03 | OpenCode — DeepSeek V4.1 Flash Free | 04/11/2026 01:27 | [#4](#4) |
| 5 | P05 — Checklist IA-04 | OpenCode — DeepSeek V4.1 Flash Free | 04/11/2026 01:29 | [#5](#5) |
| 6 | P05b — Review checklist (trùng / measurable / IA) | OpenCode — DeepSeek V4.1 Flash Free | 04/11/2026 01:43 | [#6](#6) |

---

### 1
- **Công cụ AI:** OpenCode — DeepSeek V4.1 Flash Free
- **Ngày giờ:** 04/11/2026 00:54
- **Bước:** P01 — UI inventory (account screens)
- **File đã tạo/sửa:** checklist/inventory.md

**Prompt:**
```text
@screenshots/input/ Bạn hỗ trợ tôi làm GUI testing cho "EShop", một e-commerce demo app bằng tiếng Việt.
Tôi test các screen về account: Register, Login (primary); Forgot Password 2 bước, Profile (secondary).
Đính kèm: spec FR-01..FR-04 và screenshot của từng screen ở các state.

Chỉ làm step 1, CHƯA viết checklist.
Lập bảng UI inventory cho mỗi screen:
| Screen | Element | Type (button/input/link/label/toast/...) | Purpose | States (default/hover/focus/disabled/error/loading/empty) |
Chỉ liệt kê những gì thấy trong screenshot hoặc đọc được trong spec. Chỗ nào đoán thì ghi "(assumed)". Ghi vào log

Attached directory: /home/zinn/zinn/testing/hw03/screenshots/input/

forgot-step1.png
forgot-step2.png
login-empty.png
login-error.png
login-locked.png
profile.png
register-empty.png
register-error.png
spec-FR01-04.md
```

**AI output:**
```text
Step 1 only — UI inventory for the five account screens. No checklist items yet. Draft saved to `checklist/inventory.md`. Everything below is limited to the 8 screenshots + spec; dynamic states that cannot be seen in a static screenshot are marked `(assumed)`.

# UI Inventory — EShop Account Screens (P01)

- **Scope:** Register, Login (primary); Forgot Password step 1/2, Profile (secondary).
- **Evidence:** 8 screenshots in `screenshots/input/` and `screenshots/input/spec-FR01-04.md` (FR-01 → FR-04).
- **Rule:** Only elements visible in the screenshots or stated in the spec are listed. Dynamic states that cannot be seen in a static screenshot are marked **(assumed)**.
- **Status:** Draft for human review — inventory only, no checklist items or Passed/Failed verdicts yet.

## Shared chrome (all screens)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| All screens | "EShop" logo | Link | Return to Home | Default (observed); hover/focus (assumed) |
| All screens | "Giỏ hàng" nav item | Link | Open the shopping cart | Default (observed); hover/focus (assumed); active/current-page highlight (assumed — FR-23 requires it, not visible in screenshots) |
| All screens | Cart item-count badge | Badge | Show number of items in cart (FR-23) | Not visible in any screenshot; 0 / N>0 (assumed) |
| All screens | "Đăng nhập" nav item | Link | Open Login | Default (observed); hover/focus (assumed); active/current-page highlight (assumed) |
| All screens | "Đăng ký" nav item | Link | Open Register | Default (observed); hover/focus (assumed); active/current-page highlight (assumed) |
| Profile (logged in) | "Chào, Test User" | Link | Open the current user's Profile | Default (observed, yellow); hover/focus (assumed); long-name overflow (assumed) |
| Profile (logged in) | "Thoát" | Button | Log out | Default (observed, red); hover/focus (assumed); label is "Thoát", while FR-23 requires "Đăng xuất" |
| All screens | Footer copyright text | Text | Show ownership/purpose notice | Static (observed) |

## Login

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Login | Page heading "Đăng Ký" | Heading | Identify the page | Static (observed); text is wrong for Login — expected "Đăng nhập" (FR-02) |
| Login | "Username" label | Label | Describe the account field | Static (observed); wording differs from the Email field named in FR-02 |
| Login | Username input | Input (text) | Enter email/username | Empty (observed); filled (observed in `login-error.png`); focus (assumed); field-level error (not observed); disabled (assumed) |
| Login | "Mật khẩu" label | Label | Describe the password field | Static (observed) |
| Login | Password input | Input (text; shows password in clear text) | Enter password | Empty (observed); filled and readable as plain text (observed in `login-error.png` and `login-locked.png`); focus (assumed); field-level error (not observed); disabled (assumed) |
| Login | "Quên mật khẩu?" | Link | Go to Forgot Password step 1 | Default (observed); hover/focus/visited (assumed) |
| Login | "Sign In" | Button (submit) | Submit credentials | Default (observed); hover/focus/active (assumed); loading/disabled (not observed) |
| Login | Login-failure message "Đăng nhập thất bại. Vui lòng kiểm tra lại." | Inline alert (red banner) | Report an unsuccessful login | Hidden by default (observed in `login-empty.png`); visible after a wrong password (observed in `login-error.png`); visible while locked (observed in `login-locked.png`); positioned below the submit button; no field-level errors |
| Login | Lockout notice / remaining-time countdown | Inline message | Tell the user the account is locked and when it will reopen (FR-02) | Not present in `login-locked.png`; expected visible while locked (assumed from FR-02) |
| Login | "Chưa có tài khoản? Đăng ký ngay" | Text + link | Go to Register | Default (observed); hover/focus (assumed) |
| Login | Required-field marker `*` | Label marker | Mark required fields (FR-22) | Not visible (observed); expected next to required labels (assumed from FR-22) |
| Login | Show/hide-password control | Icon/button | Toggle password visibility | Not present in screenshots; optional (assumed) |
| Login | Submitting/loading state | Button/state | Indicate that login is in progress and prevent double submit | Not visible (assumed) |

## Register

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Register | Page heading "Đăng Ký Tài Khoản" | Heading | Identify the page | Static (observed) |
| Register | "Họ Tên" label | Label | Describe the full-name field | Static (observed); no required marker `*` (observed) |
| Register | Họ Tên input | Input (text) | Enter the user's full name | Empty (observed in `register-empty.png`); filled (observed in `register-error.png`); focus (assumed); field-level error (not observed); disabled (assumed) |
| Register | "Email" label | Label | Describe the email field | Static (observed); no required marker `*` (observed) |
| Register | Email input | Input (text) | Enter the account email | Empty (observed); filled (observed); focus (assumed); field-level error (not observed); HTML `type` not visible (assumed text) |
| Register | "Mật khẩu" label | Label | Describe the password field | Static (observed); no required marker `*` (observed) |
| Register | Password input | Input (password) | Create a password | Empty (observed); filled and masked (observed in `register-error.png`); focus (assumed); error shown only as a form-level banner; disabled (assumed) |
| Register | Password-rules help text "Yêu cầu: Tối thiểu 8 ký tự..." | Help text | Explain the password policy (FR-01) | Default visible (observed); small, low-contrast text; error state unchanged (observed); hidden (assumed) |
| Register | "Đăng Ký" | Button (submit; red) | Create the account | Default (observed); hover/focus/active (assumed); loading/disabled (not observed) |
| Register | "Đã có tài khoản? Đăng nhập" | Text + link | Go to Login | Default (observed); hover/focus (assumed); post-success redirect to Login (assumed from FR-01) |
| Register | Form-level error banner "Mật khẩu quá yếu!..." | Inline alert (red banner) | Report weak password or registration failure | Hidden by default (observed in `register-empty.png`); visible after weak password (observed in `register-error.png`); sits above the fields, not next to the password field |
| Register | "Xác nhận mật khẩu" | Input (password) + label | Confirm the password (FR-01) | Not present in any screenshot; expected empty/filled/mismatch-error states (assumed from FR-01) |
| Register | Duplicate-email / invalid-email message | Inline alert | Report uniqueness/format errors (FR-01) | Not visible in screenshots; expected after submit (assumed from FR-01) |
| Register | Required-field marker `*` | Label marker | Mark required fields (FR-22) | Not visible (observed); expected next to required labels (assumed from FR-22) |
| Register | Show/hide-password control | Icon/button | Toggle password visibility | Not present in screenshots; optional (assumed) |
| Register | Submitting/loading state | Button/state | Indicate registration is in progress and prevent double submit | Not visible (assumed) |

## Forgot Password — Step 1

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Forgot Password — Step 1 | Page heading "Quên Mật Khẩu" | Heading | Identify the page | Static (observed) |
| Forgot Password — Step 1 | "Nhập Email của bạn" label | Label | Describe the email field | Static (observed); no required marker `*` (observed) |
| Forgot Password — Step 1 | Email input | Input (text) | Enter the registered email | Empty (observed in `forgot-step1.png`); filled (assumed); focus (assumed); field-level error (not observed); HTML `type` not visible (assumed text) |
| Forgot Password — Step 1 | "Lấy mã OTP" | Button (submit) | Request an OTP | Default (observed, blue); hover/focus/active (assumed); loading/disabled (not observed) |
| Forgot Password — Step 1 | Step indicator "Bước 1 / 2" | Label/stepper | Show progress (FR-03) | Not present in the screenshot; expected visible (assumed from FR-03) |
| Forgot Password — Step 1 | "Quay lại đăng nhập" | Link/button | Return to Login (FR-03) | Not present in the screenshot; expected visible (assumed from FR-03) |
| Forgot Password — Step 1 | Unknown-email / request error | Alert or inline message | Report that the email is not registered | Not visible in the screenshot; browser `alert()` behavior (assumed) |
| Forgot Password — Step 1 | OTP delivery confirmation | Inline message | Confirm the OTP was generated and show it in demo mode (FR-03) | Not on this step; shown on Step 2 (observed in `forgot-step2.png`) |

## Forgot Password — Step 2

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Forgot Password — Step 2 | Page heading "Quên Mật Khẩu" | Heading | Identify the page | Static (observed) |
| Forgot Password — Step 2 | OTP info box "Mã OTP của bạn là: 4452" | Inline success/info box (green) | Show the demo OTP on screen (FR-03) | Visible after requesting an OTP (observed in `forgot-step2.png`); hidden before the request (assumed); displays 4 digits, while FR-03 requires 6 |
| Forgot Password — Step 2 | "Mã OTP (4 số)" label | Label | Describe the OTP field | Static (observed); wording confirms 4 digits, contrary to FR-03 |
| Forgot Password — Step 2 | OTP input | Input (text) | Enter the OTP | Empty (observed); filled (assumed); focus (assumed); field-level error (not observed); paste behavior (assumed) |
| Forgot Password — Step 2 | "Mật khẩu mới" label | Label | Describe the new-password field | Static (observed) |
| Forgot Password — Step 2 | New-password input | Input (password) | Enter the new password | Empty (observed); filled and masked (assumed); focus (assumed); error via alert (assumed) |
| Forgot Password — Step 2 | "Đặt lại mật khẩu" | Button (submit; green) | Submit OTP + new password | Default (observed); hover/focus/active (assumed); loading/disabled (not observed) |
| Forgot Password — Step 2 | "← Quay lại" | Button (green) | Go back to Step 1 | Default (observed); hover/focus (assumed); shares the same green style as the primary button; label/destination wording not "Quay lại đăng nhập" (destination assumed Step 1) |
| Forgot Password — Step 2 | "Xác nhận mật khẩu mới" | Input (password) + label | Confirm the new password (FR-03) | Not present in the screenshot; expected empty/filled/mismatch-error states (assumed from FR-03) |
| Forgot Password — Step 2 | Step indicator "Bước 2 / 2" | Label/stepper | Show progress (FR-03) | Not present in the screenshot; expected visible (assumed from FR-03) |
| Forgot Password — Step 2 | New-password rules help text | Help text | Explain FR-01 password rules before typing | Not present in the screenshot; expected (assumed from FR-03) |
| Forgot Password — Step 2 | Reset success / wrong-OTP feedback | Alert or inline message | Confirm success or report an invalid/expired OTP | Not visible in the screenshot; browser `alert()` behavior (assumed) |
| Forgot Password — Step 2 | OTP expiry / single-use indicator | Text | Show that the OTP expires and cannot be reused (SEC-07) | Not present in the screenshot; expected (assumed) |

## Profile

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Profile | "Chào, Test User" | Link | Open the current user's Profile | Default (observed, yellow); hover/focus (assumed); long-name overflow (assumed) |
| Profile | "Thoát" | Button | Log out | Default (observed, red); hover/focus (assumed); label differs from FR-23's "Đăng xuất" |
| Profile | Page heading "Hồ sơ của bạn" | Heading | Identify the profile section | Static (observed) |
| Profile | "Email (Không đổi)" label | Label | Explain that email is read-only (FR-04) | Static (observed) |
| Profile | Email input | Input (disabled/read-only) | Display the account email | Disabled/read-only with gray background (observed); value `test@eshop.com` (observed); editable (not observed) |
| Profile | "Họ Tên" label | Label | Describe the name field | Static (observed); no required marker `*` (observed) |
| Profile | Họ Tên input | Input (text) | Edit the full name | Filled "Test User" (observed); empty (assumed); focus (assumed); field-level error (not observed); disabled (assumed) |
| Profile | "Số điện thoại" label | Label | Describe the phone field | Static (observed); no required marker `*` (observed) |
| Profile | Số điện thoại input | Input (text) | Edit the phone number (FR-04) | Empty with placeholder "VD: 0912345678" (observed); filled (assumed); focus (assumed); error via alert (assumed); validation message not visible |
| Profile | "Địa chỉ giao hàng" label | Label | Describe the address field | Static (observed); no required marker `*` (observed) |
| Profile | Địa chỉ giao hàng textarea | Textarea | Edit the default shipping address (FR-04) | Empty with placeholder "Nhập địa chỉ của bạn" (observed); resizable (observed via resize handle); filled/focus (assumed); error (not observed) |
| Profile | "Cập nhật" | Button (submit) | Save profile changes | Default (observed, blue); hover/focus/active (assumed); loading/disabled (not observed) |
| Profile | Update-success feedback | Toast/alert/inline message | Confirm the profile was saved | Not visible in the screenshot; browser `alert()` behavior (assumed) |
| Profile | "Lịch sử đơn hàng" heading | Heading | Identify the order-history section (FR-11) | Static (observed) |
| Profile | Empty-order message "Bạn chưa có đơn hàng nào." | Empty state (text only) | Explain that the user has no orders | Empty (observed); loading (assumed); error/retry (assumed); no icon/illustration observed |
| Profile | Orders table (Mã ĐH, Ngày đặt, Tổng tiền, Trạng thái, Thao tác) | Table | Show order history (FR-11) | Not rendered in the empty state (observed); populated rows (assumed); loading/error (assumed) |
| Profile | Required-field marker `*` | Label marker | Mark required fields (FR-22) | Not visible (observed); expected next to required labels (assumed from FR-22) |

## Inventory notes (observations, not checklist verdicts)

- Login shows the heading "Đăng Ký", the label "Username", the button "Sign In", and renders the password in clear text.
- The locked state (`login-locked.png`) looks identical to the wrong-password state: the same generic red banner, no lock reason and no remaining-time countdown.
- Register has no "Xác nhận mật khẩu" field; its error banner is placed above the fields; the password-rules help text is very small and low-contrast.
- Forgot Password Step 1 has no step indicator and no "Quay lại đăng nhập"; Step 2 shows a 4-digit OTP, has no step indicator and no confirm-password field, and both action buttons are green.
- Profile marks email as "Không đổi" and disables the field; the order-history area currently shows only a text empty state; success feedback is not visible in the screenshot.

📝 Đã ghi log #1 vào report/ai-audit.md
```

### 2
- **Công cụ AI:** OpenCode — DeepSeek V4.1 Flash Free
- **Ngày giờ:** 04/11/2026 01:19
- **Bước:** P02 — Checklist IA-01
- **File đã tạo/sửa:** checklist/ia-01.md

**Prompt:**
```text
@screenshots/input/spec-G1.md @checklist/inventory.md Dựa trên UI inventory đã review bên dưới, tạo các checklist item CHỈ cho IA-01 General UI standards.
Bám theo các nhóm checklist trong slide bài giảng: <dán tiêu đề các mục trong slide>.
Rules:
- Mỗi item là MỘT check verify được, có expected result rõ ràng.
- Gắn với một screen và một element cụ thể.
- Không lặp giữa các screen, trừ khi expected result khác nhau.
- Item nào xuất phát từ FR-01..FR-04 thì ghi vào cột "Req".
Bảng: | ID (<IA>-NN) | Screen | Element | Check | Expected Result | Req |
Khoảng 12–18 item.

UI inventory:
<dán nội dung checklist/inventory.md> Ghi vào log 

Attached file: screenshots/input/spec-G1.md

### FR-01: Đăng ký tài khoản

- Người dùng phải cung cấp: **Họ Tên**, **Email**, **Mật khẩu**.
- Email phải có định dạng hợp lệ (`user@domain.com`) và là duy nhất trong hệ thống.
- **Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`).
- Phải có trường **Xác nhận mật khẩu** — hệ thống từ chối nếu hai trường không khớp.
- Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.

### FR-02: Đăng nhập & Khóa tài khoản

- Người dùng nhập Email và Mật khẩu.
- Sau mỗi lần đăng nhập sai, hệ thống tăng bộ đếm lên **đúng 1 đơn vị**.
- Nếu đăng nhập sai từ **3 lần trở lên** liên tiếp, tài khoản bị tạm khóa **30 giây** (môi trường demo). Hệ thống trả về thông báo lỗi phù hợp; không để lộ chi tiết nguyên nhân.
- Đăng nhập thành công trả về JWT Token. Token được lưu phía client và gửi kèm tất cả các yêu cầu có xác thực qua header `Authorization: Bearer <token>`.
- Trường email phải dùng `type="email"` (có validate HTML5 format).

### FR-03: Quên mật khẩu & Đặt lại mật khẩu (2 bước)

**Bước 1 — Lấy mã OTP:**

- Người dùng nhập địa chỉ Email đã đăng ký.
- Hệ thống sinh mã OTP **6 chữ số ngẫu nhiên** và gửi qua Email (trong môi trường demo: hiển thị trực tiếp trên màn hình).
- Giao diện phải hiển thị **chỉ báo bước (Step Indicator)** — ví dụ: "Bước 1 / 2".
- Có nút **Quay lại đăng nhập**.

**Bước 2 — Đặt lại mật khẩu:**

- Người dùng nhập OTP, Mật khẩu mới, và **Xác nhận mật khẩu mới**.
- Mật khẩu mới phải tuân thủ điều kiện như FR-01.
- Hai trường mật khẩu phải khớp nhau.
- OTP chỉ hợp lệ cho email đã yêu cầu, không thể dùng cho email khác.

### FR-04: Quản lý hồ sơ cá nhân

- Người dùng đã đăng nhập có thể cập nhật: **Họ Tên**, **Số điện thoại**, **Địa chỉ giao hàng mặc định**.
- **Số điện thoại hợp lệ**: bắt đầu bằng số `0`, từ 10–11 chữ số.
- Email không được phép thay đổi qua giao diện.
- Người dùng chỉ có thể cập nhật hồ sơ của chính mình; không thể tự thay đổi thuộc tính `role`.

---

## 8. Yêu cầu Giao diện (GUI Requirements)

### FR-21: Tiêu chuẩn Giao diện Chung

- **Nhất quán ngôn ngữ**: Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn).
- **Nhất quán màu sắc**: Các nút hành động tích cực (Submit, Mua hàng) dùng màu xanh dương. Các nút nguy hiểm/hủy bỏ dùng màu đỏ.
- **Nhất quán đơn vị tiền**: Luôn dùng ký hiệu `₫` với định dạng phân cách hàng nghìn.
- **Tiêu đề trang**: Mỗi trang có đúng 1 thẻ `<h1>` mô tả nội dung trang.
- **Tab Order**: Thứ tự focus theo Tab phải đi từ trên xuống dưới, trái sang phải.

### FR-22: Form Requirements

- Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn.
- Trường Email phải dùng `type="email"`.
- Trường Mật khẩu phải dùng `type="password"` (không hiển thị rõ).
- Thông báo lỗi phải xuất hiện **trên** nút submit, không phải bên dưới.
- Các form có từ 2 bước trở lên phải có **Step Indicator** rõ ràng.

### FR-23: Navigation Requirements

- Thanh điều hướng (Navbar) phải **highlight** trang đang được chọn.
- Link "Giỏ hàng" phải hiển thị **badge số lượng** sản phẩm trong giỏ.
- Nút Đăng xuất phải nhãn là "Đăng xuất" (không phải "Thoát").
- Breadcrumb bắt buộc có ở các trang con (Giỏ hàng, Thanh toán, Chi tiết sản phẩm).

### FR-24: Feedback & State Requirements

- Sau khi bấm "Thêm vào giỏ", phải có phản hồi trực quan (toast/badge).
- Khi xóa item khỏi giỏ phải có dialog xác nhận.
- Trang trống (Empty State) phải có icon/hình minh họa và message thân thiện.
- Tất cả ảnh sản phẩm phải có thuộc tính `alt` mô tả nội dung ảnh (không để rỗng).

---

## 9. Yêu cầu Bảo mật (Security Requirements — Tham khảo)

| ID     | Yêu cầu                                                                                                         |
| ------ | --------------------------------------------------------------------------------------------------------------- |
| SEC-01 | Mật khẩu **không** được lưu dưới dạng plaintext.                                                                |
| SEC-02 | Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ.                                                          |
| SEC-03 | API Admin phải kiểm tra `role = 'admin'` trong Token, không chỉ kiểm tra sự tồn tại của Token.                  |
| SEC-04 | Mọi dữ liệu từ user nhập vào khi hiển thị trên UI phải được escape đúng cách, không dùng `innerHTML` trực tiếp. |
| SEC-05 | Truy vấn CSDL phải dùng Parameterized Query, không nối chuỗi trực tiếp.                                         |
| SEC-06 | API cập nhật hồ sơ không được cho phép thay đổi trường `role` từ client.                                        |
| SEC-07 | OTP đặt lại mật khẩu phải đủ entropy (tối thiểu 6 chữ số), có thời hạn và vô hiệu hóa sau khi dùng.             |

---



Attached file: checklist/inventory.md

# UI Inventory — EShop Account Screens (G1)

- **Scope:** Register, Login (primary); Forgot Password step 1/2, Profile (secondary).
- **Evidence:** 8 screenshot trong `screenshots/input/`, spec `spec-G1.md` (FR-01..04, FR-21..24, SEC), kiểm tra thêm bằng DevTools.
- **Status:** Đã review. Bản AI gốc (P01, AI log #1) được sửa theo `checklist/inventory-review.md` (R1–R9 + mục 3).
- **Tag trong cột States:** `observed` = thấy trong screenshot · `DevTools` = không thấy trong ảnh, hiện lấy từ source code, **cần tự xác nhận bằng DevTools** (F12 → Elements) · `assumed` = chưa kiểm chứng.

## Shared header & footer

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| All | "EShop" logo | Link | Về Home | default (observed); hover/focus (assumed) |
| All | "Giỏ hàng" | Link | Mở Cart | default (observed); hover underline (assumed) |
| All (logged out) | "Đăng nhập" | Link | Mở Login | default (observed); không có active highlight khi đang ở `/login` (observed) |
| All (logged out) | "Đăng ký" | Link | Mở Register | default (observed); không có active highlight khi đang ở `/register` (observed) |
| All (logged in) | "Chào, {name}" | Link (text vàng) | Mở Profile | default "Chào, Test User" (observed); name dài / name chứa HTML (assumed) |
| All (logged in) | "Thoát" | Button (đỏ) | Logout | default (observed); hover/focus (assumed) |
| All | Footer "© 2026 EShop SUT…" | Text | Thông tin bản quyền | static (observed) |

## Login (`/login`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Login | Heading "Đăng Ký" | Heading (`<h2>`) | Tiêu đề trang | static (observed); tag `<h2>`, không có `<h1>` (DevTools) |
| Login | Label "Username" | Label | Nhãn cho field email | static (observed) |
| Login | Field email | Input `type="text"` | Nhập email | empty (observed `login-empty`); filled (observed `login-error`); focus (assumed) |
| Login | Label "Mật khẩu" | Label | Nhãn cho field password | static (observed) |
| Login | Field password | Input `type="text"` | Nhập password | empty (observed); filled, hiện plain text (observed `login-locked`); focus (assumed) |
| Login | "Quên mật khẩu?" | Link | Mở Forgot Password | default (observed); hover (assumed) |
| Login | "Sign In" | Button (submit, xanh dương) | Gửi form login | default (observed); `tabIndex=1` (DevTools); không thấy loading/disabled (observed) |
| Login | "Chưa có tài khoản? Đăng ký ngay" | Text + link | Mở Register | default (observed) |
| Login | Error banner "Đăng nhập thất bại. Vui lòng kiểm tra lại." | Inline alert (đỏ) | Báo login thất bại | hidden (observed `login-empty`); visible khi sai password (observed `login-error`); visible, cùng nội dung, khi bị lock (observed `login-locked`); nằm dưới button submit (observed) |

## Register (`/register`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Register | Heading "Đăng Ký Tài Khoản" | Heading (`<h2>`) | Tiêu đề trang | static (observed); không có `<h1>` (DevTools) |
| Register | Error banner "Mật khẩu quá yếu!…" | Inline alert (đỏ) | Báo lỗi đăng ký | hidden (observed `register-empty`); visible sau khi submit password bị từ chối (observed `register-error`); nằm trên các field (observed) |
| Register | Label + field "Họ Tên" | Label + Input `type="text"` | Nhập họ tên | empty (observed); filled (observed); focus (assumed) |
| Register | Label + field "Email" | Label + Input `type="text"` | Nhập email | empty (observed); filled (observed); `type="text"` (DevTools) |
| Register | Label + field "Mật khẩu" | Label + Input `type="password"` | Tạo password | empty (observed); filled, masked (observed) |
| Register | Hint "Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt." | Help text (chữ nhỏ, xám nhạt) | Giải thích password rule | luôn hiện (observed); không đổi khi lỗi (observed) |
| Register | "Đăng Ký" | Button (submit, đỏ) | Tạo tài khoản | default (observed); không thấy loading/disabled (observed) |
| Register | "Đã có tài khoản? Đăng nhập" | Text + link | Mở Login | default (observed) |

## Forgot Password — Step 1 (`/forgot-password`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| FP step 1 | Heading "Quên Mật Khẩu" | Heading (`<h2>`) | Tiêu đề trang | static (observed); không có `<h1>` (DevTools) |
| FP step 1 | Label + field "Nhập Email của bạn" | Label + Input `type="text"` | Nhập email đã đăng ký | empty (observed `forgot-step1`); filled/focus (assumed) |
| FP step 1 | "Lấy mã OTP" | Button (submit, xanh dương) | Request OTP, sang step 2 | default (observed) |
| FP step 1 | Thông báo email không tồn tại | (chưa xác định) | Báo lỗi request | chưa kiểm chứng (assumed) |

## Forgot Password — Step 2 (cùng URL `/forgot-password`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| FP step 2 | Heading "Quên Mật Khẩu" | Heading (`<h2>`) | Tiêu đề trang | static (observed) |
| FP step 2 | Info box "Mã OTP của bạn là: 4452" | Inline info (xanh lá) | Hiện OTP (demo) | visible sau khi request (observed `forgot-step2`); OTP 4 chữ số (observed) |
| FP step 2 | Label + field "Mã OTP (4 số)" | Label + Input `type="text"` | Nhập OTP | empty (observed); paste (assumed) |
| FP step 2 | Label + field "Mật khẩu mới" | Label + Input `type="password"` | Nhập password mới | empty (observed) |
| FP step 2 | "Đặt lại mật khẩu" | Button (submit, xanh lá) | Gửi OTP + password mới | default (observed) |
| FP step 2 | "← Quay lại" | Button (xanh lá, cùng style với submit) | Quay về step 1 | default (observed) |
| FP step 2 | Kết quả reset (thành công / OTP sai / password yếu) | (chưa xác định) | Báo kết quả | chưa kiểm chứng (assumed) |

## Profile (`/profile`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Profile | Heading "Hồ sơ của bạn" | Heading (`<h2>`) | Tiêu đề khối hồ sơ | static (observed); không có `<h1>` (DevTools) |
| Profile | Label + field "Email (Không đổi)" | Label + Input disabled | Hiện email, read-only | disabled, nền xám, value `test@eshop.com` (observed) |
| Profile | Label + field "Họ Tên" | Label + Input `type="text"` | Sửa họ tên | filled "Test User" (observed) |
| Profile | Label + field "Số điện thoại" | Label + Input `type="text"` | Sửa SĐT | empty, placeholder "VD: 0912345678" (observed) |
| Profile | Label + textarea "Địa chỉ giao hàng" | Label + Textarea (resize được) | Sửa địa chỉ | empty, placeholder "Nhập địa chỉ của bạn" (observed) |
| Profile | "Cập nhật" | Button (submit, xanh dương) | Lưu hồ sơ | default (observed) |
| Profile | Thông báo lưu thành công / lỗi | (chưa xác định) | Báo kết quả lưu | chưa kiểm chứng (assumed) |
| Profile | Heading "Lịch sử đơn hàng" + text "Bạn chưa có đơn hàng nào." | Heading + empty state (chỉ có text) | Order history (FR-11, ngoài G1) | empty (observed) |

## Expected by spec but absent

Các element spec yêu cầu nhưng **không có** trong screenshot. Đây là input cho checklist, chưa phải verdict.

| Screen | Element spec yêu cầu | Requirement |
|---|---|---|
| All | Mỗi trang có đúng 1 `<h1>` | FR-21 |
| Header | Navbar highlight trang hiện tại | FR-23 |
| Header | Badge số lượng trên "Giỏ hàng" | FR-23 |
| Header | Nút logout ghi "Đăng xuất" (thay vì "Thoát") | FR-23 |
| Login, Register, FP, Profile | Dấu `*` cạnh label của field bắt buộc | FR-22 |
| Login | Field email `type="email"`, field password `type="password"` | FR-02, FR-22 |
| Register | Field "Xác nhận mật khẩu" | FR-01 |
| Register, FP step 1 | Field email `type="email"` | FR-22 |
| FP step 1, 2 | Step indicator "Bước 1 / 2", "Bước 2 / 2" | FR-03, FR-22 |
| FP step 1 | Button "Quay lại đăng nhập" | FR-03 |
| FP step 2 | Field "Xác nhận mật khẩu mới" | FR-03 |
| FP step 2 | OTP 6 chữ số | FR-03, SEC-07 |

## Inventory notes (quan sát để dùng ở P02–P05, chưa phải Passed/Failed)

- Ngôn ngữ không nhất quán: Login có "Username", "Sign In" giữa UI tiếng Việt (FR-21).
- Màu button: "Đăng Ký" là submit nhưng màu đỏ; ở FP step 2 cả submit và "← Quay lại" đều xanh lá (FR-21).
- Login: heading ghi "Đăng Ký"; error banner nằm dưới button submit (FR-22 yêu cầu ở trên).
- Login locked và wrong-password giống hệt nhau (FR-02: không lộ nguyên nhân). Việc không có thời gian unlock là vấn đề usability, không phải vi phạm FR-02.
- `tabIndex=1` trên "Sign In" làm Tab nhảy vào button trước các field (FR-21 Tab Order).
- Header render "Chào, {name}" bằng HTML; name chứa thẻ HTML có thể chạy được (SEC-04).
- Step 1 và step 2 của Forgot Password dùng chung URL, reload trang thì mất step 2.
- Ngoài screenshot, cần tự kiểm bằng DevTools: thẻ heading, `type` của input, tab order, `autocomplete`.
```

**AI output:**
```text
Đây là 17 item IA-01 dựa trên inventory đã review. Bản nháp đã lưu vào `checklist/ia-01.md`. Bạn chưa dán tiêu đề các mục trong slide nên mình nhóm theo thứ tự: ngôn ngữ/thuật ngữ → màu sắc/ngữ nghĩa hành động → typography/heading → layout/căn chỉnh → tab order/focus → nhất quán/khả năng truy cập. Chưa chạy Passed/Failed.

# IA-01 — General UI Standards Checklist (G1 Account Screens)

- **Scope:** Login, Register, Forgot Password step 1/2, Profile, shared header/footer.
- **Input:** reviewed `checklist/inventory.md` + `screenshots/input/spec-G1.md`.
- **Slide note:** The lecture slide headings were not pasted in the prompt, so the items are grouped by the usual IA-01 sub-areas: language/terminology, colour semantics, typography/headings, layout/alignment, tab order/focus, consistency/accessibility. Re-map IDs if the slide uses a different order.
- **Status:** Draft for human review — no Passed/Failed execution yet.
- **Req column:** FR-21..24 are the GUI requirement sources; "—" means the item is a general UI/accessibility heuristic not tied to a single FR.

| ID | Screen | Element | Check | Expected Result | Req |
|---|---|---|---|---|---|
| IA-01-01 | Login | Label "Username" | The account field label uses the Vietnamese term defined by the screen's requirement, not an English alternative. | Label reads "Email"; "Username" is not displayed. | FR-21 |
| IA-01-02 | Login | Button "Sign In" | The submit button uses a Vietnamese action label consistent with the rest of the interface. | Button reads "Đăng nhập"; "Sign In" is not displayed. | FR-21 |
| IA-01-03 | Login | Page heading "Đăng Ký" | The page heading text describes the current screen, not another screen. | Heading reads "Đăng nhập"; it does not say "Đăng Ký". | FR-21 |
| IA-01-04 | Register | Submit button "Đăng Ký" | A positive submit action uses the standard blue action colour. | Button background is blue (design-token blue), not red. | FR-21 |
| IA-01-05 | Forgot Password — Step 2 | Primary "Đặt lại mật khẩu" and secondary "← Quay lại" buttons | Primary and secondary actions are visually distinguishable; the positive primary action uses blue. | "Đặt lại mật khẩu" is blue; "← Quay lại" is neutral/outline or otherwise clearly secondary; the two are not both green. | FR-21 |
| IA-01-06 | All G1 screens | Page headings | Each page has exactly one `<h1>` describing the page; section headings use `<h2>`. | Every screen has exactly one `<h1>` (no page with zero or multiple `<h1>`), and its text matches the screen. | FR-21 |
| IA-01-07 | All G1 screens | Body text and headings | Typography is consistent across the flow: same font family, same size/weight for headings at the same level, body text at least 14px. | Computed `font-family` matches; same-level headings have equal `font-size`/`font-weight`; body text is at least 14px. | — |
| IA-01-08 | Register | Password-rules hint "Yêu cầu: Tối thiểu 8 ký tự..." | Secondary help text is readable: at least 12px and a contrast ratio of at least 4.5:1 against its background. | Computed font-size is at least 12px; DevTools contrast ratio is at least 4.5:1; the text is not light grey on white. | — |
| IA-01-09 | Login, Register, Forgot Password | Form card container | The authentication cards share the same width, horizontal centring, and padding. | All auth cards have the same max-width (for example 448px), are horizontally centred, and use the same inner padding. | — |
| IA-01-10 | Register | Labels and input fields | Form fields are aligned consistently: labels above inputs, inputs the same width, equal vertical spacing. | Labels sit above their inputs and are left-aligned; all inputs share the same width; vertical gaps between fields are equal. | — |
| IA-01-11 | Profile | Email field "Email (Không đổi)" | The read-only email is visually distinguishable from editable fields while keeping the same form geometry. | Email field is disabled, has a grey background, cannot be edited, and has the same height/border/radius as the editable fields. | FR-04 |
| IA-01-12 | All G1 screens | Header and footer | Header/footer keep a consistent height and position; the main content is not overlapped at 100% zoom. | Header and footer have the same height/position on every screen; no content is hidden behind them. | — |
| IA-01-13 | Profile | Header greeting "Chào, {name}" | A long display name does not break the header layout. | A 60-character name wraps or truncates inside the greeting area; it does not overlap "Thoát" or push the nav off-screen. | — |
| IA-01-14 | Login | Tab order from the first field | Keyboard Tab order follows the visual top-to-bottom, left-to-right order; the submit button is not focused before the fields. | Tab sequence is Email → Password → "Quên mật khẩu?" → "Sign In" → "Đăng ký ngay"; no `tabIndex` jump to "Sign In" first. | FR-21 |
| IA-01-15 | Profile | Tab order through the profile form | Disabled fields are skipped and the remaining controls follow the visual order. | Tab sequence is Họ Tên → Số điện thoại → Địa chỉ giao hàng → Cập nhật; the disabled email is skipped; focus is never trapped. | FR-21 |
| IA-01-16 | All G1 screens | Links, buttons, and inputs | Every interactive element shows a visible focus indicator when reached by keyboard. | Each focused element has a visible outline/ring/box-shadow with at least 3:1 contrast against adjacent colours; focus is never lost. | — |
| IA-01-17 | All G1 screens | Whole page at 200% zoom | The layout remains usable when the browser is zoomed to 200%. | No horizontal scrollbar; no text or control is clipped; forms and buttons remain visible and operable. | — |

📝 Đã ghi log #2 vào report/ai-audit.md
```

### 3
- **Công cụ AI:** OpenCode — DeepSeek V4.1 Flash Free
- **Ngày giờ:** 04/11/2026 01:23
- **Bước:** P03 — Checklist IA-02
- **File đã tạo/sửa:** checklist/ia-02.md

**Prompt:**
```text
@screenshots/input/spec-G1.md @checklist/inventory.md Dựa trên UI inventory đã review bên dưới, tạo các checklist item CHỈ cho IA-02 Forms.
Bám theo các nhóm checklist trong slide bài giảng: <dán tiêu đề các mục trong slide>.
Rules:
- Mỗi item là MỘT check verify được, có expected result rõ ràng.
- Gắn với một screen và một element cụ thể.
- Không lặp giữa các screen, trừ khi expected result khác nhau.
- Item nào xuất phát từ FR-01..FR-04 thì ghi vào cột "Req".
Bảng: | ID (<IA>-NN) | Screen | Element | Check | Expected Result | Req |
Khoảng 12–18 item.

UI inventory:
<dán nội dung checklist/inventory.md>  Ghi vào log 

Attached file: screenshots/input/spec-G1.md

### FR-01: Đăng ký tài khoản

- Người dùng phải cung cấp: **Họ Tên**, **Email**, **Mật khẩu**.
- Email phải có định dạng hợp lệ (`user@domain.com`) và là duy nhất trong hệ thống.
- **Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`).
- Phải có trường **Xác nhận mật khẩu** — hệ thống từ chối nếu hai trường không khớp.
- Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.

### FR-02: Đăng nhập & Khóa tài khoản

- Người dùng nhập Email và Mật khẩu.
- Sau mỗi lần đăng nhập sai, hệ thống tăng bộ đếm lên **đúng 1 đơn vị**.
- Nếu đăng nhập sai từ **3 lần trở lên** liên tiếp, tài khoản bị tạm khóa **30 giây** (môi trường demo). Hệ thống trả về thông báo lỗi phù hợp; không để lộ chi tiết nguyên nhân.
- Đăng nhập thành công trả về JWT Token. Token được lưu phía client và gửi kèm tất cả các yêu cầu có xác thực qua header `Authorization: Bearer <token>`.
- Trường email phải dùng `type="email"` (có validate HTML5 format).

### FR-03: Quên mật khẩu & Đặt lại mật khẩu (2 bước)

**Bước 1 — Lấy mã OTP:**

- Người dùng nhập địa chỉ Email đã đăng ký.
- Hệ thống sinh mã OTP **6 chữ số ngẫu nhiên** và gửi qua Email (trong môi trường demo: hiển thị trực tiếp trên màn hình).
- Giao diện phải hiển thị **chỉ báo bước (Step Indicator)** — ví dụ: "Bước 1 / 2".
- Có nút **Quay lại đăng nhập**.

**Bước 2 — Đặt lại mật khẩu:**

- Người dùng nhập OTP, Mật khẩu mới, và **Xác nhận mật khẩu mới**.
- Mật khẩu mới phải tuân thủ điều kiện như FR-01.
- Hai trường mật khẩu phải khớp nhau.
- OTP chỉ hợp lệ cho email đã yêu cầu, không thể dùng cho email khác.

### FR-04: Quản lý hồ sơ cá nhân

- Người dùng đã đăng nhập có thể cập nhật: **Họ Tên**, **Số điện thoại**, **Địa chỉ giao hàng mặc định**.
- **Số điện thoại hợp lệ**: bắt đầu bằng số `0`, từ 10–11 chữ số.
- Email không được phép thay đổi qua giao diện.
- Người dùng chỉ có thể cập nhật hồ sơ của chính mình; không thể tự thay đổi thuộc tính `role`.

---

## 8. Yêu cầu Giao diện (GUI Requirements)

### FR-21: Tiêu chuẩn Giao diện Chung

- **Nhất quán ngôn ngữ**: Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn).
- **Nhất quán màu sắc**: Các nút hành động tích cực (Submit, Mua hàng) dùng màu xanh dương. Các nút nguy hiểm/hủy bỏ dùng màu đỏ.
- **Nhất quán đơn vị tiền**: Luôn dùng ký hiệu `₫` với định dạng phân cách hàng nghìn.
- **Tiêu đề trang**: Mỗi trang có đúng 1 thẻ `<h1>` mô tả nội dung trang.
- **Tab Order**: Thứ tự focus theo Tab phải đi từ trên xuống dưới, trái sang phải.

### FR-22: Form Requirements

- Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn.
- Trường Email phải dùng `type="email"`.
- Trường Mật khẩu phải dùng `type="password"` (không hiển thị rõ).
- Thông báo lỗi phải xuất hiện **trên** nút submit, không phải bên dưới.
- Các form có từ 2 bước trở lên phải có **Step Indicator** rõ ràng.

### FR-23: Navigation Requirements

- Thanh điều hướng (Navbar) phải **highlight** trang đang được chọn.
- Link "Giỏ hàng" phải hiển thị **badge số lượng** sản phẩm trong giỏ.
- Nút Đăng xuất phải nhãn là "Đăng xuất" (không phải "Thoát").
- Breadcrumb bắt buộc có ở các trang con (Giỏ hàng, Thanh toán, Chi tiết sản phẩm).

### FR-24: Feedback & State Requirements

- Sau khi bấm "Thêm vào giỏ", phải có phản hồi trực quan (toast/badge).
- Khi xóa item khỏi giỏ phải có dialog xác nhận.
- Trang trống (Empty State) phải có icon/hình minh họa và message thân thiện.
- Tất cả ảnh sản phẩm phải có thuộc tính `alt` mô tả nội dung ảnh (không để rỗng).

---

## 9. Yêu cầu Bảo mật (Security Requirements — Tham khảo)

| ID     | Yêu cầu                                                                                                         |
| ------ | --------------------------------------------------------------------------------------------------------------- |
| SEC-01 | Mật khẩu **không** được lưu dưới dạng plaintext.                                                                |
| SEC-02 | Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ.                                                          |
| SEC-03 | API Admin phải kiểm tra `role = 'admin'` trong Token, không chỉ kiểm tra sự tồn tại của Token.                  |
| SEC-04 | Mọi dữ liệu từ user nhập vào khi hiển thị trên UI phải được escape đúng cách, không dùng `innerHTML` trực tiếp. |
| SEC-05 | Truy vấn CSDL phải dùng Parameterized Query, không nối chuỗi trực tiếp.                                         |
| SEC-06 | API cập nhật hồ sơ không được cho phép thay đổi trường `role` từ client.                                        |
| SEC-07 | OTP đặt lại mật khẩu phải đủ entropy (tối thiểu 6 chữ số), có thời hạn và vô hiệu hóa sau khi dùng.             |

---



Attached file: checklist/inventory.md

# UI Inventory — EShop Account Screens (G1)

- **Scope:** Register, Login (primary); Forgot Password step 1/2, Profile (secondary).
- **Evidence:** 8 screenshot trong `screenshots/input/`, spec `spec-G1.md` (FR-01..04, FR-21..24, SEC), kiểm tra thêm bằng DevTools.
- **Status:** Đã review. Bản AI gốc (P01, AI log #1) được sửa theo `checklist/inventory-review.md` (R1–R9 + mục 3).
- **Tag trong cột States:** `observed` = thấy trong screenshot · `DevTools` = không thấy trong ảnh, hiện lấy từ source code, **cần tự xác nhận bằng DevTools** (F12 → Elements) · `assumed` = chưa kiểm chứng.

## Shared header & footer

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| All | "EShop" logo | Link | Về Home | default (observed); hover/focus (assumed) |
| All | "Giỏ hàng" | Link | Mở Cart | default (observed); hover underline (assumed) |
| All (logged out) | "Đăng nhập" | Link | Mở Login | default (observed); không có active highlight khi đang ở `/login` (observed) |
| All (logged out) | "Đăng ký" | Link | Mở Register | default (observed); không có active highlight khi đang ở `/register` (observed) |
| All (logged in) | "Chào, {name}" | Link (text vàng) | Mở Profile | default "Chào, Test User" (observed); name dài / name chứa HTML (assumed) |
| All (logged in) | "Thoát" | Button (đỏ) | Logout | default (observed); hover/focus (assumed) |
| All | Footer "© 2026 EShop SUT…" | Text | Thông tin bản quyền | static (observed) |

## Login (`/login`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Login | Heading "Đăng Ký" | Heading (`<h2>`) | Tiêu đề trang | static (observed); tag `<h2>`, không có `<h1>` (DevTools) |
| Login | Label "Username" | Label | Nhãn cho field email | static (observed) |
| Login | Field email | Input `type="text"` | Nhập email | empty (observed `login-empty`); filled (observed `login-error`); focus (assumed) |
| Login | Label "Mật khẩu" | Label | Nhãn cho field password | static (observed) |
| Login | Field password | Input `type="text"` | Nhập password | empty (observed); filled, hiện plain text (observed `login-locked`); focus (assumed) |
| Login | "Quên mật khẩu?" | Link | Mở Forgot Password | default (observed); hover (assumed) |
| Login | "Sign In" | Button (submit, xanh dương) | Gửi form login | default (observed); `tabIndex=1` (DevTools); không thấy loading/disabled (observed) |
| Login | "Chưa có tài khoản? Đăng ký ngay" | Text + link | Mở Register | default (observed) |
| Login | Error banner "Đăng nhập thất bại. Vui lòng kiểm tra lại." | Inline alert (đỏ) | Báo login thất bại | hidden (observed `login-empty`); visible khi sai password (observed `login-error`); visible, cùng nội dung, khi bị lock (observed `login-locked`); nằm dưới button submit (observed) |

## Register (`/register`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Register | Heading "Đăng Ký Tài Khoản" | Heading (`<h2>`) | Tiêu đề trang | static (observed); không có `<h1>` (DevTools) |
| Register | Error banner "Mật khẩu quá yếu!…" | Inline alert (đỏ) | Báo lỗi đăng ký | hidden (observed `register-empty`); visible sau khi submit password bị từ chối (observed `register-error`); nằm trên các field (observed) |
| Register | Label + field "Họ Tên" | Label + Input `type="text"` | Nhập họ tên | empty (observed); filled (observed); focus (assumed) |
| Register | Label + field "Email" | Label + Input `type="text"` | Nhập email | empty (observed); filled (observed); `type="text"` (DevTools) |
| Register | Label + field "Mật khẩu" | Label + Input `type="password"` | Tạo password | empty (observed); filled, masked (observed) |
| Register | Hint "Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt." | Help text (chữ nhỏ, xám nhạt) | Giải thích password rule | luôn hiện (observed); không đổi khi lỗi (observed) |
| Register | "Đăng Ký" | Button (submit, đỏ) | Tạo tài khoản | default (observed); không thấy loading/disabled (observed) |
| Register | "Đã có tài khoản? Đăng nhập" | Text + link | Mở Login | default (observed) |

## Forgot Password — Step 1 (`/forgot-password`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| FP step 1 | Heading "Quên Mật Khẩu" | Heading (`<h2>`) | Tiêu đề trang | static (observed); không có `<h1>` (DevTools) |
| FP step 1 | Label + field "Nhập Email của bạn" | Label + Input `type="text"` | Nhập email đã đăng ký | empty (observed `forgot-step1`); filled/focus (assumed) |
| FP step 1 | "Lấy mã OTP" | Button (submit, xanh dương) | Request OTP, sang step 2 | default (observed) |
| FP step 1 | Thông báo email không tồn tại | (chưa xác định) | Báo lỗi request | chưa kiểm chứng (assumed) |

## Forgot Password — Step 2 (cùng URL `/forgot-password`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| FP step 2 | Heading "Quên Mật Khẩu" | Heading (`<h2>`) | Tiêu đề trang | static (observed) |
| FP step 2 | Info box "Mã OTP của bạn là: 4452" | Inline info (xanh lá) | Hiện OTP (demo) | visible sau khi request (observed `forgot-step2`); OTP 4 chữ số (observed) |
| FP step 2 | Label + field "Mã OTP (4 số)" | Label + Input `type="text"` | Nhập OTP | empty (observed); paste (assumed) |
| FP step 2 | Label + field "Mật khẩu mới" | Label + Input `type="password"` | Nhập password mới | empty (observed) |
| FP step 2 | "Đặt lại mật khẩu" | Button (submit, xanh lá) | Gửi OTP + password mới | default (observed) |
| FP step 2 | "← Quay lại" | Button (xanh lá, cùng style với submit) | Quay về step 1 | default (observed) |
| FP step 2 | Kết quả reset (thành công / OTP sai / password yếu) | (chưa xác định) | Báo kết quả | chưa kiểm chứng (assumed) |

## Profile (`/profile`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Profile | Heading "Hồ sơ của bạn" | Heading (`<h2>`) | Tiêu đề khối hồ sơ | static (observed); không có `<h1>` (DevTools) |
| Profile | Label + field "Email (Không đổi)" | Label + Input disabled | Hiện email, read-only | disabled, nền xám, value `test@eshop.com` (observed) |
| Profile | Label + field "Họ Tên" | Label + Input `type="text"` | Sửa họ tên | filled "Test User" (observed) |
| Profile | Label + field "Số điện thoại" | Label + Input `type="text"` | Sửa SĐT | empty, placeholder "VD: 0912345678" (observed) |
| Profile | Label + textarea "Địa chỉ giao hàng" | Label + Textarea (resize được) | Sửa địa chỉ | empty, placeholder "Nhập địa chỉ của bạn" (observed) |
| Profile | "Cập nhật" | Button (submit, xanh dương) | Lưu hồ sơ | default (observed) |
| Profile | Thông báo lưu thành công / lỗi | (chưa xác định) | Báo kết quả lưu | chưa kiểm chứng (assumed) |
| Profile | Heading "Lịch sử đơn hàng" + text "Bạn chưa có đơn hàng nào." | Heading + empty state (chỉ có text) | Order history (FR-11, ngoài G1) | empty (observed) |

## Expected by spec but absent

Các element spec yêu cầu nhưng **không có** trong screenshot. Đây là input cho checklist, chưa phải verdict.

| Screen | Element spec yêu cầu | Requirement |
|---|---|---|
| All | Mỗi trang có đúng 1 `<h1>` | FR-21 |
| Header | Navbar highlight trang hiện tại | FR-23 |
| Header | Badge số lượng trên "Giỏ hàng" | FR-23 |
| Header | Nút logout ghi "Đăng xuất" (thay vì "Thoát") | FR-23 |
| Login, Register, FP, Profile | Dấu `*` cạnh label của field bắt buộc | FR-22 |
| Login | Field email `type="email"`, field password `type="password"` | FR-02, FR-22 |
| Register | Field "Xác nhận mật khẩu" | FR-01 |
| Register, FP step 1 | Field email `type="email"` | FR-22 |
| FP step 1, 2 | Step indicator "Bước 1 / 2", "Bước 2 / 2" | FR-03, FR-22 |
| FP step 1 | Button "Quay lại đăng nhập" | FR-03 |
| FP step 2 | Field "Xác nhận mật khẩu mới" | FR-03 |
| FP step 2 | OTP 6 chữ số | FR-03, SEC-07 |

## Inventory notes (quan sát để dùng ở P02–P05, chưa phải Passed/Failed)

- Ngôn ngữ không nhất quán: Login có "Username", "Sign In" giữa UI tiếng Việt (FR-21).
- Màu button: "Đăng Ký" là submit nhưng màu đỏ; ở FP step 2 cả submit và "← Quay lại" đều xanh lá (FR-21).
- Login: heading ghi "Đăng Ký"; error banner nằm dưới button submit (FR-22 yêu cầu ở trên).
- Login locked và wrong-password giống hệt nhau (FR-02: không lộ nguyên nhân). Việc không có thời gian unlock là vấn đề usability, không phải vi phạm FR-02.
- `tabIndex=1` trên "Sign In" làm Tab nhảy vào button trước các field (FR-21 Tab Order).
- Header render "Chào, {name}" bằng HTML; name chứa thẻ HTML có thể chạy được (SEC-04).
- Step 1 và step 2 của Forgot Password dùng chung URL, reload trang thì mất step 2.
- Ngoài screenshot, cần tự kiểm bằng DevTools: thẻ heading, `type` của input, tab order, `autocomplete`.
```

**AI output:**
```text
Đây là 18 item IA-02 dựa trên inventory đã review. Bản nháp đã lưu vào `checklist/ia-02.md`. Bạn chưa dán tiêu đề các mục trong slide nên mình nhóm theo thứ tự: label/required field → input type/HTML validation → password/confirmation → validation message/error placement → multi-step form → form accessibility. Chưa chạy Passed/Failed.

# IA-02 — Forms Checklist (G1 Account Screens)

- **Scope:** Login, Register, Forgot Password step 1/2, Profile, shared form controls.
- **Input:** reviewed `checklist/inventory.md` + `screenshots/input/spec-G1.md`.
- **Slide note:** The lecture slide headings were not pasted in the prompt, so the items are grouped by the usual IA-02 sub-areas: labels/required fields, input types/HTML validation, password creation/confirmation, validation messages/error placement, multi-step forms, and form accessibility. Re-map IDs if the slide uses a different order.
- **Status:** Draft for human review — no Passed/Failed execution yet.
- **Req column:** FR-21..24 are the GUI requirement sources; "—" means the item is a general form/accessibility heuristic not tied to a single FR.

| ID | Screen | Element | Check | Expected Result | Req |
|---|---|---|---|---|---|
| IA-02-01 | All G1 forms | Required-field labels | Every required field has a `*` immediately next to its label. | On Login, Register, FP step 1/2, and Profile, every required label shows `*`; optional fields do not. | FR-22 |
| IA-02-02 | All G1 forms | Labels and inputs | Each input has a visible, programmatically associated label; clicking the label focuses the input; no field relies on its placeholder as the only label. | Every input has a `<label for="...">` matching its `id`; clicking the label moves focus; placeholders are supplementary only. | — |
| IA-02-03 | Login, Register, Forgot Password — Step 1 | Email inputs | Every email field uses `type="email"` and native HTML5 validation blocks malformed addresses. | DOM `type="email"` on all three fields; entering `abc` and submitting shows the browser's email-format validation; no request is sent. | FR-02, FR-22 |
| IA-02-04 | Login, Register, Forgot Password — Step 2 | Password inputs | Every password field uses `type="password"` and masks typed characters. | DOM `type="password"` on Login, Register, and FP step 2; characters are masked in all states. | FR-22 |
| IA-02-05 | Register | "Xác nhận mật khẩu" field | Registration requires a confirmation-password field and rejects a mismatch before creating the account. | Field exists; mismatched values show an error and no account is created; matching values allow submit. | FR-01 |
| IA-02-06 | Register | "Mật khẩu" field | Password-strength validation accepts a valid FR-01 password and rejects weak ones with a message naming the missing rule. | `Abc12345!` is accepted; `abc12345`, `Abcdefgh`, `Abc12345` are rejected; the message names the missing uppercase/lowercase/digit/special requirement. | FR-01 |
| IA-02-07 | Register | Email input + submit | Registering with an already-used email is rejected with a clear error and does not create a duplicate account. | Submit `test@eshop.com`; an error appears above submit; the user count is unchanged; there is no redirect to Login. | FR-01 |
| IA-02-08 | Login | Error banner | Login errors are displayed above the submit button, not below it. | Error banner is above "Sign In" in the DOM and visually; it is not rendered after the button/link. | FR-22 |
| IA-02-09 | Forgot Password — Step 1 | Step indicator | Step 1 shows a clear "Bước 1 / 2" indicator. | "Bước 1 / 2" (or equivalent) is visible before submitting. | FR-03, FR-22 |
| IA-02-10 | Forgot Password — Step 1 | "Quay lại đăng nhập" control | Step 1 provides a visible control that returns to Login. | A link/button "Quay lại đăng nhập" is visible and navigates to `/login`. | FR-03 |
| IA-02-11 | Forgot Password — Step 2 | Step indicator | Step 2 shows a clear "Bước 2 / 2" indicator. | "Bước 2 / 2" (or equivalent) is visible. | FR-03, FR-22 |
| IA-02-12 | Forgot Password — Step 2 | OTP info box + OTP input | The OTP is exactly 6 digits; the input accepts 6 digits and rejects 5 or 7. | Info box shows a 6-digit OTP; input accepts exactly 6 digits; 5-digit and 7-digit values show an error. | FR-03, SEC-07 |
| IA-02-13 | Forgot Password — Step 2 | "Xác nhận mật khẩu mới" field | The reset form requires a confirmation-password field and rejects a mismatch before changing the password. | Field exists; mismatch shows an error and the password is unchanged; matching values allow reset. | FR-03 |
| IA-02-14 | Forgot Password — Step 2 | Validation feedback | OTP/password errors are shown inline above the submit button, not through a blocking `alert()`. | Wrong OTP or weak password shows an inline message above "Đặt lại mật khẩu"; no `window.alert` dialog. | FR-22 |
| IA-02-15 | Profile | "Số điện thoại" field | Phone validation accepts a leading 0 with 10–11 digits and rejects all other formats. | `0912345678` and `09123456789` are accepted; `912345678`, `091234567`, `091234567890`, `abc` are rejected with a message; valid value persists after save. | FR-04 |
| IA-02-16 | Profile | "Email (Không đổi)" field | Email is read-only and cannot be changed through the profile form. | Field is disabled; no edit is possible; after changing other fields, saving, and reloading, email remains the original. | FR-04 |
| IA-02-17 | All G1 forms | Required inputs | Empty required fields trigger native HTML5 validation and block submission. | Every required input has the `required` attribute; submitting empty focuses the first invalid field and sends no request. | FR-22 |
| IA-02-18 | All G1 forms | Email/password inputs | Email and password fields expose correct `autocomplete` hints for password managers. | Email fields use `autocomplete="email"`; Login password uses `current-password`; Register/FP new passwords use `new-password`; the browser offers save/fill. | — |

📝 Đã ghi log #3 vào report/ai-audit.md
```

### 4
- **Công cụ AI:** OpenCode — DeepSeek V4.1 Flash Free
- **Ngày giờ:** 04/11/2026 01:27
- **Bước:** P04 — Checklist IA-03
- **File đã tạo/sửa:** checklist/ia-03.md

**Prompt:**
```text
@screenshots/input/spec-G1.md @checklist/inventory.md Dựa trên UI inventory đã review bên dưới, tạo các checklist item CHỈ choIA-03 Navigation.
Bám theo các nhóm checklist trong slide bài giảng: <dán tiêu đề các mục trong slide>.
Rules:
- Mỗi item là MỘT check verify được, có expected result rõ ràng.
- Gắn với một screen và một element cụ thể.
- Không lặp giữa các screen, trừ khi expected result khác nhau.
- Item nào xuất phát từ FR-01..FR-04 thì ghi vào cột "Req".
Bảng: | ID (<IA>-NN) | Screen | Element | Check | Expected Result | Req |
Khoảng 12–18 item.

UI inventory:
<dán nội dung checklist/inventory.md>  Ghi vào log 

Attached file: screenshots/input/spec-G1.md

### FR-01: Đăng ký tài khoản

- Người dùng phải cung cấp: **Họ Tên**, **Email**, **Mật khẩu**.
- Email phải có định dạng hợp lệ (`user@domain.com`) và là duy nhất trong hệ thống.
- **Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`).
- Phải có trường **Xác nhận mật khẩu** — hệ thống từ chối nếu hai trường không khớp.
- Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.

### FR-02: Đăng nhập & Khóa tài khoản

- Người dùng nhập Email và Mật khẩu.
- Sau mỗi lần đăng nhập sai, hệ thống tăng bộ đếm lên **đúng 1 đơn vị**.
- Nếu đăng nhập sai từ **3 lần trở lên** liên tiếp, tài khoản bị tạm khóa **30 giây** (môi trường demo). Hệ thống trả về thông báo lỗi phù hợp; không để lộ chi tiết nguyên nhân.
- Đăng nhập thành công trả về JWT Token. Token được lưu phía client và gửi kèm tất cả các yêu cầu có xác thực qua header `Authorization: Bearer <token>`.
- Trường email phải dùng `type="email"` (có validate HTML5 format).

### FR-03: Quên mật khẩu & Đặt lại mật khẩu (2 bước)

**Bước 1 — Lấy mã OTP:**

- Người dùng nhập địa chỉ Email đã đăng ký.
- Hệ thống sinh mã OTP **6 chữ số ngẫu nhiên** và gửi qua Email (trong môi trường demo: hiển thị trực tiếp trên màn hình).
- Giao diện phải hiển thị **chỉ báo bước (Step Indicator)** — ví dụ: "Bước 1 / 2".
- Có nút **Quay lại đăng nhập**.

**Bước 2 — Đặt lại mật khẩu:**

- Người dùng nhập OTP, Mật khẩu mới, và **Xác nhận mật khẩu mới**.
- Mật khẩu mới phải tuân thủ điều kiện như FR-01.
- Hai trường mật khẩu phải khớp nhau.
- OTP chỉ hợp lệ cho email đã yêu cầu, không thể dùng cho email khác.

### FR-04: Quản lý hồ sơ cá nhân

- Người dùng đã đăng nhập có thể cập nhật: **Họ Tên**, **Số điện thoại**, **Địa chỉ giao hàng mặc định**.
- **Số điện thoại hợp lệ**: bắt đầu bằng số `0`, từ 10–11 chữ số.
- Email không được phép thay đổi qua giao diện.
- Người dùng chỉ có thể cập nhật hồ sơ của chính mình; không thể tự thay đổi thuộc tính `role`.

---

## 8. Yêu cầu Giao diện (GUI Requirements)

### FR-21: Tiêu chuẩn Giao diện Chung

- **Nhất quán ngôn ngữ**: Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn).
- **Nhất quán màu sắc**: Các nút hành động tích cực (Submit, Mua hàng) dùng màu xanh dương. Các nút nguy hiểm/hủy bỏ dùng màu đỏ.
- **Nhất quán đơn vị tiền**: Luôn dùng ký hiệu `₫` với định dạng phân cách hàng nghìn.
- **Tiêu đề trang**: Mỗi trang có đúng 1 thẻ `<h1>` mô tả nội dung trang.
- **Tab Order**: Thứ tự focus theo Tab phải đi từ trên xuống dưới, trái sang phải.

### FR-22: Form Requirements

- Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn.
- Trường Email phải dùng `type="email"`.
- Trường Mật khẩu phải dùng `type="password"` (không hiển thị rõ).
- Thông báo lỗi phải xuất hiện **trên** nút submit, không phải bên dưới.
- Các form có từ 2 bước trở lên phải có **Step Indicator** rõ ràng.

### FR-23: Navigation Requirements

- Thanh điều hướng (Navbar) phải **highlight** trang đang được chọn.
- Link "Giỏ hàng" phải hiển thị **badge số lượng** sản phẩm trong giỏ.
- Nút Đăng xuất phải nhãn là "Đăng xuất" (không phải "Thoát").
- Breadcrumb bắt buộc có ở các trang con (Giỏ hàng, Thanh toán, Chi tiết sản phẩm).

### FR-24: Feedback & State Requirements

- Sau khi bấm "Thêm vào giỏ", phải có phản hồi trực quan (toast/badge).
- Khi xóa item khỏi giỏ phải có dialog xác nhận.
- Trang trống (Empty State) phải có icon/hình minh họa và message thân thiện.
- Tất cả ảnh sản phẩm phải có thuộc tính `alt` mô tả nội dung ảnh (không để rỗng).

---

## 9. Yêu cầu Bảo mật (Security Requirements — Tham khảo)

| ID     | Yêu cầu                                                                                                         |
| ------ | --------------------------------------------------------------------------------------------------------------- |
| SEC-01 | Mật khẩu **không** được lưu dưới dạng plaintext.                                                                |
| SEC-02 | Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ.                                                          |
| SEC-03 | API Admin phải kiểm tra `role = 'admin'` trong Token, không chỉ kiểm tra sự tồn tại của Token.                  |
| SEC-04 | Mọi dữ liệu từ user nhập vào khi hiển thị trên UI phải được escape đúng cách, không dùng `innerHTML` trực tiếp. |
| SEC-05 | Truy vấn CSDL phải dùng Parameterized Query, không nối chuỗi trực tiếp.                                         |
| SEC-06 | API cập nhật hồ sơ không được cho phép thay đổi trường `role` từ client.                                        |
| SEC-07 | OTP đặt lại mật khẩu phải đủ entropy (tối thiểu 6 chữ số), có thời hạn và vô hiệu hóa sau khi dùng.             |

---



Attached file: checklist/inventory.md

# UI Inventory — EShop Account Screens (G1)

- **Scope:** Register, Login (primary); Forgot Password step 1/2, Profile (secondary).
- **Evidence:** 8 screenshot trong `screenshots/input/`, spec `spec-G1.md` (FR-01..04, FR-21..24, SEC), kiểm tra thêm bằng DevTools.
- **Status:** Đã review. Bản AI gốc (P01, AI log #1) được sửa theo `checklist/inventory-review.md` (R1–R9 + mục 3).
- **Tag trong cột States:** `observed` = thấy trong screenshot · `DevTools` = không thấy trong ảnh, hiện lấy từ source code, **cần tự xác nhận bằng DevTools** (F12 → Elements) · `assumed` = chưa kiểm chứng.

## Shared header & footer

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| All | "EShop" logo | Link | Về Home | default (observed); hover/focus (assumed) |
| All | "Giỏ hàng" | Link | Mở Cart | default (observed); hover underline (assumed) |
| All (logged out) | "Đăng nhập" | Link | Mở Login | default (observed); không có active highlight khi đang ở `/login` (observed) |
| All (logged out) | "Đăng ký" | Link | Mở Register | default (observed); không có active highlight khi đang ở `/register` (observed) |
| All (logged in) | "Chào, {name}" | Link (text vàng) | Mở Profile | default "Chào, Test User" (observed); name dài / name chứa HTML (assumed) |
| All (logged in) | "Thoát" | Button (đỏ) | Logout | default (observed); hover/focus (assumed) |
| All | Footer "© 2026 EShop SUT…" | Text | Thông tin bản quyền | static (observed) |

## Login (`/login`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Login | Heading "Đăng Ký" | Heading (`<h2>`) | Tiêu đề trang | static (observed); tag `<h2>`, không có `<h1>` (DevTools) |
| Login | Label "Username" | Label | Nhãn cho field email | static (observed) |
| Login | Field email | Input `type="text"` | Nhập email | empty (observed `login-empty`); filled (observed `login-error`); focus (assumed) |
| Login | Label "Mật khẩu" | Label | Nhãn cho field password | static (observed) |
| Login | Field password | Input `type="text"` | Nhập password | empty (observed); filled, hiện plain text (observed `login-locked`); focus (assumed) |
| Login | "Quên mật khẩu?" | Link | Mở Forgot Password | default (observed); hover (assumed) |
| Login | "Sign In" | Button (submit, xanh dương) | Gửi form login | default (observed); `tabIndex=1` (DevTools); không thấy loading/disabled (observed) |
| Login | "Chưa có tài khoản? Đăng ký ngay" | Text + link | Mở Register | default (observed) |
| Login | Error banner "Đăng nhập thất bại. Vui lòng kiểm tra lại." | Inline alert (đỏ) | Báo login thất bại | hidden (observed `login-empty`); visible khi sai password (observed `login-error`); visible, cùng nội dung, khi bị lock (observed `login-locked`); nằm dưới button submit (observed) |

## Register (`/register`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Register | Heading "Đăng Ký Tài Khoản" | Heading (`<h2>`) | Tiêu đề trang | static (observed); không có `<h1>` (DevTools) |
| Register | Error banner "Mật khẩu quá yếu!…" | Inline alert (đỏ) | Báo lỗi đăng ký | hidden (observed `register-empty`); visible sau khi submit password bị từ chối (observed `register-error`); nằm trên các field (observed) |
| Register | Label + field "Họ Tên" | Label + Input `type="text"` | Nhập họ tên | empty (observed); filled (observed); focus (assumed) |
| Register | Label + field "Email" | Label + Input `type="text"` | Nhập email | empty (observed); filled (observed); `type="text"` (DevTools) |
| Register | Label + field "Mật khẩu" | Label + Input `type="password"` | Tạo password | empty (observed); filled, masked (observed) |
| Register | Hint "Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt." | Help text (chữ nhỏ, xám nhạt) | Giải thích password rule | luôn hiện (observed); không đổi khi lỗi (observed) |
| Register | "Đăng Ký" | Button (submit, đỏ) | Tạo tài khoản | default (observed); không thấy loading/disabled (observed) |
| Register | "Đã có tài khoản? Đăng nhập" | Text + link | Mở Login | default (observed) |

## Forgot Password — Step 1 (`/forgot-password`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| FP step 1 | Heading "Quên Mật Khẩu" | Heading (`<h2>`) | Tiêu đề trang | static (observed); không có `<h1>` (DevTools) |
| FP step 1 | Label + field "Nhập Email của bạn" | Label + Input `type="text"` | Nhập email đã đăng ký | empty (observed `forgot-step1`); filled/focus (assumed) |
| FP step 1 | "Lấy mã OTP" | Button (submit, xanh dương) | Request OTP, sang step 2 | default (observed) |
| FP step 1 | Thông báo email không tồn tại | (chưa xác định) | Báo lỗi request | chưa kiểm chứng (assumed) |

## Forgot Password — Step 2 (cùng URL `/forgot-password`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| FP step 2 | Heading "Quên Mật Khẩu" | Heading (`<h2>`) | Tiêu đề trang | static (observed) |
| FP step 2 | Info box "Mã OTP của bạn là: 4452" | Inline info (xanh lá) | Hiện OTP (demo) | visible sau khi request (observed `forgot-step2`); OTP 4 chữ số (observed) |
| FP step 2 | Label + field "Mã OTP (4 số)" | Label + Input `type="text"` | Nhập OTP | empty (observed); paste (assumed) |
| FP step 2 | Label + field "Mật khẩu mới" | Label + Input `type="password"` | Nhập password mới | empty (observed) |
| FP step 2 | "Đặt lại mật khẩu" | Button (submit, xanh lá) | Gửi OTP + password mới | default (observed) |
| FP step 2 | "← Quay lại" | Button (xanh lá, cùng style với submit) | Quay về step 1 | default (observed) |
| FP step 2 | Kết quả reset (thành công / OTP sai / password yếu) | (chưa xác định) | Báo kết quả | chưa kiểm chứng (assumed) |

## Profile (`/profile`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Profile | Heading "Hồ sơ của bạn" | Heading (`<h2>`) | Tiêu đề khối hồ sơ | static (observed); không có `<h1>` (DevTools) |
| Profile | Label + field "Email (Không đổi)" | Label + Input disabled | Hiện email, read-only | disabled, nền xám, value `test@eshop.com` (observed) |
| Profile | Label + field "Họ Tên" | Label + Input `type="text"` | Sửa họ tên | filled "Test User" (observed) |
| Profile | Label + field "Số điện thoại" | Label + Input `type="text"` | Sửa SĐT | empty, placeholder "VD: 0912345678" (observed) |
| Profile | Label + textarea "Địa chỉ giao hàng" | Label + Textarea (resize được) | Sửa địa chỉ | empty, placeholder "Nhập địa chỉ của bạn" (observed) |
| Profile | "Cập nhật" | Button (submit, xanh dương) | Lưu hồ sơ | default (observed) |
| Profile | Thông báo lưu thành công / lỗi | (chưa xác định) | Báo kết quả lưu | chưa kiểm chứng (assumed) |
| Profile | Heading "Lịch sử đơn hàng" + text "Bạn chưa có đơn hàng nào." | Heading + empty state (chỉ có text) | Order history (FR-11, ngoài G1) | empty (observed) |

## Expected by spec but absent

Các element spec yêu cầu nhưng **không có** trong screenshot. Đây là input cho checklist, chưa phải verdict.

| Screen | Element spec yêu cầu | Requirement |
|---|---|---|
| All | Mỗi trang có đúng 1 `<h1>` | FR-21 |
| Header | Navbar highlight trang hiện tại | FR-23 |
| Header | Badge số lượng trên "Giỏ hàng" | FR-23 |
| Header | Nút logout ghi "Đăng xuất" (thay vì "Thoát") | FR-23 |
| Login, Register, FP, Profile | Dấu `*` cạnh label của field bắt buộc | FR-22 |
| Login | Field email `type="email"`, field password `type="password"` | FR-02, FR-22 |
| Register | Field "Xác nhận mật khẩu" | FR-01 |
| Register, FP step 1 | Field email `type="email"` | FR-22 |
| FP step 1, 2 | Step indicator "Bước 1 / 2", "Bước 2 / 2" | FR-03, FR-22 |
| FP step 1 | Button "Quay lại đăng nhập" | FR-03 |
| FP step 2 | Field "Xác nhận mật khẩu mới" | FR-03 |
| FP step 2 | OTP 6 chữ số | FR-03, SEC-07 |

## Inventory notes (quan sát để dùng ở P02–P05, chưa phải Passed/Failed)

- Ngôn ngữ không nhất quán: Login có "Username", "Sign In" giữa UI tiếng Việt (FR-21).
- Màu button: "Đăng Ký" là submit nhưng màu đỏ; ở FP step 2 cả submit và "← Quay lại" đều xanh lá (FR-21).
- Login: heading ghi "Đăng Ký"; error banner nằm dưới button submit (FR-22 yêu cầu ở trên).
- Login locked và wrong-password giống hệt nhau (FR-02: không lộ nguyên nhân). Việc không có thời gian unlock là vấn đề usability, không phải vi phạm FR-02.
- `tabIndex=1` trên "Sign In" làm Tab nhảy vào button trước các field (FR-21 Tab Order).
- Header render "Chào, {name}" bằng HTML; name chứa thẻ HTML có thể chạy được (SEC-04).
- Step 1 và step 2 của Forgot Password dùng chung URL, reload trang thì mất step 2.
- Ngoài screenshot, cần tự kiểm bằng DevTools: thẻ heading, `type` của input, tab order, `autocomplete`.
```

**AI output:**
```text
Đây là 17 item IA-03 dựa trên inventory đã review. Bản nháp đã lưu vào `checklist/ia-03.md`. Bạn chưa dán tiêu đề các mục trong slide nên mình nhóm theo thứ tự: global navbar → auth-state navigation → in-page links → multi-step wizard → post-action redirects → direct URL/history. Chưa chạy Passed/Failed.

# IA-03 — Navigation Checklist (G1 Account Screens)

- **Scope:** Login, Register, Forgot Password step 1/2, Profile, shared header/footer.
- **Input:** reviewed `checklist/inventory.md` + `screenshots/input/spec-G1.md`.
- **Slide note:** The lecture slide headings were not pasted in the prompt, so the items are grouped by the usual IA-03 sub-areas: global navbar, auth-state navigation, in-page links, multi-step wizard navigation, post-action redirects, and direct-URL/history behaviour. Re-map IDs if the slide uses a different order.
- **Status:** Draft for human review — no Passed/Failed execution yet.
- **Req column:** FR-21..24 are the GUI requirement sources; "—" means the item is a general navigation heuristic not tied to a single FR.

| ID | Screen | Element | Check | Expected Result | Req |
|---|---|---|---|---|---|
| IA-03-01 | All G1 screens (logged out) | Header auth links | The logged-out header shows the Login and Register links and hides the authenticated controls. | "Đăng nhập" and "Đăng ký" are visible; "Chào, {name}" and "Thoát" are absent on Login, Register, and Forgot Password. | FR-23 |
| IA-03-02 | Profile | Header logged-in state | The logged-in header shows the profile greeting and Logout and hides the Login/Register links. | "Chào, {name}" and "Thoát" are visible; "Đăng nhập" and "Đăng ký" are absent. | FR-23 |
| IA-03-03 | All G1 screens | Navbar current-page highlight | The navigation item for the current screen is visually highlighted. | On `/login` the "Đăng nhập" item has an active style; on `/register` the "Đăng ký" item; on `/profile` the profile/greeting item. | FR-23 |
| IA-03-04 | All G1 screens | "Giỏ hàng" link + badge | The cart link displays the current item-count badge. | Badge is present and shows the current count; with an empty cart it shows `0` (or a documented empty-cart state). | FR-23 |
| IA-03-05 | Profile | "Thoát" button | The logout control uses the label "Đăng xuất", not "Thoát". | Button text is "Đăng xuất". | FR-23 |
| IA-03-06 | Login | "EShop" logo | The logo returns the user to Home from any G1 screen. | Clicking "EShop" navigates to `/`; the Home product list renders. | — |
| IA-03-07 | Login | "Quên mật khẩu?" link | The forgot-password link opens Forgot Password step 1. | URL becomes `/forgot-password`; step 1 form renders; the browser does not perform a full page reload. | FR-03 |
| IA-03-08 | Login | "Đăng ký ngay" link | The registration link opens the Register screen. | URL becomes `/register`; the Register form renders. | FR-01 |
| IA-03-09 | Register | "Đăng nhập" link | The login link opens the Login screen. | URL becomes `/login`; the Login form renders. | FR-02 |
| IA-03-10 | Forgot Password — Step 1 | "Quay lại đăng nhập" control | Step 1 provides a visible control that returns to Login. | A link/button labelled "Quay lại đăng nhập" is visible and navigates to `/login`. | FR-03 |
| IA-03-11 | Forgot Password — Step 2 | "← Quay lại" button | The back control returns to step 1 without losing the email already entered. | Clicking returns to the step-1 form; the email field still contains the address; no data is lost. | FR-03 |
| IA-03-12 | Forgot Password — Step 2 | Browser refresh / Back | Refreshing or pressing Back does not leave the user in a broken or blank step-2 state. | Refresh returns to step 1 with a clear message or restores step 2; Back returns to step 1/previous screen; no blank page or dead end. | FR-03 |
| IA-03-13 | Register | Successful-registration redirect | A successful registration navigates to Login. | After a valid submit, URL is `/login`; the Login form renders; a success indication is shown; the user is not auto-logged in. | FR-01 |
| IA-03-14 | Login | Successful-login redirect | A successful login navigates to Home or the originally requested page. | URL is `/` (or the return URL); the header switches to the logged-in state; the Login form is no longer shown. | FR-02 |
| IA-03-15 | Profile | "Thoát" action | Logging out clears the session and switches the header to the logged-out state. | Token is removed; header shows Login/Register again; the profile form and order data are no longer accessible. | FR-23 |
| IA-03-16 | Profile (logged out) | Direct URL `/profile` | An unauthenticated visit to `/profile` does not render the profile form. | The app redirects to `/login` or shows a clear login prompt with a link; no editable profile or order data is shown. | FR-04 |
| IA-03-17 | Login (logged in) | Direct URL `/login` | An authenticated user visiting `/login` is redirected away from the login form. | The app redirects to Home or Profile; the Login form is not shown. | FR-02 |

📝 Đã ghi log #4 vào report/ai-audit.md
```

### 5
- **Công cụ AI:** OpenCode — DeepSeek V4.1 Flash Free
- **Ngày giờ:** 04/11/2026 01:29
- **Bước:** P05 — Checklist IA-04
- **File đã tạo/sửa:** checklist/ia-04.md

**Prompt:**
```text
@screenshots/input/spec-G1.md @checklist/inventory.md Dựa trên UI inventory đã review bên dưới, tạo các checklist item CHỈ cho IA-04 Feedback / state.
Bám theo các nhóm checklist trong slide bài giảng: <dán tiêu đề các mục trong slide>.
Rules:
- Mỗi item là MỘT check verify được, có expected result rõ ràng.
- Gắn với một screen và một element cụ thể.
- Không lặp giữa các screen, trừ khi expected result khác nhau.
- Item nào xuất phát từ FR-01..FR-04 thì ghi vào cột "Req".
Bảng: | ID (<IA>-NN) | Screen | Element | Check | Expected Result | Req |
Khoảng 12–18 item.

UI inventory:
<dán nội dung checklist/inventory.md>   Ghi vào log 

Attached file: screenshots/input/spec-G1.md

### FR-01: Đăng ký tài khoản

- Người dùng phải cung cấp: **Họ Tên**, **Email**, **Mật khẩu**.
- Email phải có định dạng hợp lệ (`user@domain.com`) và là duy nhất trong hệ thống.
- **Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`).
- Phải có trường **Xác nhận mật khẩu** — hệ thống từ chối nếu hai trường không khớp.
- Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.

### FR-02: Đăng nhập & Khóa tài khoản

- Người dùng nhập Email và Mật khẩu.
- Sau mỗi lần đăng nhập sai, hệ thống tăng bộ đếm lên **đúng 1 đơn vị**.
- Nếu đăng nhập sai từ **3 lần trở lên** liên tiếp, tài khoản bị tạm khóa **30 giây** (môi trường demo). Hệ thống trả về thông báo lỗi phù hợp; không để lộ chi tiết nguyên nhân.
- Đăng nhập thành công trả về JWT Token. Token được lưu phía client và gửi kèm tất cả các yêu cầu có xác thực qua header `Authorization: Bearer <token>`.
- Trường email phải dùng `type="email"` (có validate HTML5 format).

### FR-03: Quên mật khẩu & Đặt lại mật khẩu (2 bước)

**Bước 1 — Lấy mã OTP:**

- Người dùng nhập địa chỉ Email đã đăng ký.
- Hệ thống sinh mã OTP **6 chữ số ngẫu nhiên** và gửi qua Email (trong môi trường demo: hiển thị trực tiếp trên màn hình).
- Giao diện phải hiển thị **chỉ báo bước (Step Indicator)** — ví dụ: "Bước 1 / 2".
- Có nút **Quay lại đăng nhập**.

**Bước 2 — Đặt lại mật khẩu:**

- Người dùng nhập OTP, Mật khẩu mới, và **Xác nhận mật khẩu mới**.
- Mật khẩu mới phải tuân thủ điều kiện như FR-01.
- Hai trường mật khẩu phải khớp nhau.
- OTP chỉ hợp lệ cho email đã yêu cầu, không thể dùng cho email khác.

### FR-04: Quản lý hồ sơ cá nhân

- Người dùng đã đăng nhập có thể cập nhật: **Họ Tên**, **Số điện thoại**, **Địa chỉ giao hàng mặc định**.
- **Số điện thoại hợp lệ**: bắt đầu bằng số `0`, từ 10–11 chữ số.
- Email không được phép thay đổi qua giao diện.
- Người dùng chỉ có thể cập nhật hồ sơ của chính mình; không thể tự thay đổi thuộc tính `role`.

---

## 8. Yêu cầu Giao diện (GUI Requirements)

### FR-21: Tiêu chuẩn Giao diện Chung

- **Nhất quán ngôn ngữ**: Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn).
- **Nhất quán màu sắc**: Các nút hành động tích cực (Submit, Mua hàng) dùng màu xanh dương. Các nút nguy hiểm/hủy bỏ dùng màu đỏ.
- **Nhất quán đơn vị tiền**: Luôn dùng ký hiệu `₫` với định dạng phân cách hàng nghìn.
- **Tiêu đề trang**: Mỗi trang có đúng 1 thẻ `<h1>` mô tả nội dung trang.
- **Tab Order**: Thứ tự focus theo Tab phải đi từ trên xuống dưới, trái sang phải.

### FR-22: Form Requirements

- Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn.
- Trường Email phải dùng `type="email"`.
- Trường Mật khẩu phải dùng `type="password"` (không hiển thị rõ).
- Thông báo lỗi phải xuất hiện **trên** nút submit, không phải bên dưới.
- Các form có từ 2 bước trở lên phải có **Step Indicator** rõ ràng.

### FR-23: Navigation Requirements

- Thanh điều hướng (Navbar) phải **highlight** trang đang được chọn.
- Link "Giỏ hàng" phải hiển thị **badge số lượng** sản phẩm trong giỏ.
- Nút Đăng xuất phải nhãn là "Đăng xuất" (không phải "Thoát").
- Breadcrumb bắt buộc có ở các trang con (Giỏ hàng, Thanh toán, Chi tiết sản phẩm).

### FR-24: Feedback & State Requirements

- Sau khi bấm "Thêm vào giỏ", phải có phản hồi trực quan (toast/badge).
- Khi xóa item khỏi giỏ phải có dialog xác nhận.
- Trang trống (Empty State) phải có icon/hình minh họa và message thân thiện.
- Tất cả ảnh sản phẩm phải có thuộc tính `alt` mô tả nội dung ảnh (không để rỗng).

---

## 9. Yêu cầu Bảo mật (Security Requirements — Tham khảo)

| ID     | Yêu cầu                                                                                                         |
| ------ | --------------------------------------------------------------------------------------------------------------- |
| SEC-01 | Mật khẩu **không** được lưu dưới dạng plaintext.                                                                |
| SEC-02 | Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ.                                                          |
| SEC-03 | API Admin phải kiểm tra `role = 'admin'` trong Token, không chỉ kiểm tra sự tồn tại của Token.                  |
| SEC-04 | Mọi dữ liệu từ user nhập vào khi hiển thị trên UI phải được escape đúng cách, không dùng `innerHTML` trực tiếp. |
| SEC-05 | Truy vấn CSDL phải dùng Parameterized Query, không nối chuỗi trực tiếp.                                         |
| SEC-06 | API cập nhật hồ sơ không được cho phép thay đổi trường `role` từ client.                                        |
| SEC-07 | OTP đặt lại mật khẩu phải đủ entropy (tối thiểu 6 chữ số), có thời hạn và vô hiệu hóa sau khi dùng.             |

---



Attached file: checklist/inventory.md

# UI Inventory — EShop Account Screens (G1)

- **Scope:** Register, Login (primary); Forgot Password step 1/2, Profile (secondary).
- **Evidence:** 8 screenshot trong `screenshots/input/`, spec `spec-G1.md` (FR-01..04, FR-21..24, SEC), kiểm tra thêm bằng DevTools.
- **Status:** Đã review. Bản AI gốc (P01, AI log #1) được sửa theo `checklist/inventory-review.md` (R1–R9 + mục 3).
- **Tag trong cột States:** `observed` = thấy trong screenshot · `DevTools` = không thấy trong ảnh, hiện lấy từ source code, **cần tự xác nhận bằng DevTools** (F12 → Elements) · `assumed` = chưa kiểm chứng.

## Shared header & footer

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| All | "EShop" logo | Link | Về Home | default (observed); hover/focus (assumed) |
| All | "Giỏ hàng" | Link | Mở Cart | default (observed); hover underline (assumed) |
| All (logged out) | "Đăng nhập" | Link | Mở Login | default (observed); không có active highlight khi đang ở `/login` (observed) |
| All (logged out) | "Đăng ký" | Link | Mở Register | default (observed); không có active highlight khi đang ở `/register` (observed) |
| All (logged in) | "Chào, {name}" | Link (text vàng) | Mở Profile | default "Chào, Test User" (observed); name dài / name chứa HTML (assumed) |
| All (logged in) | "Thoát" | Button (đỏ) | Logout | default (observed); hover/focus (assumed) |
| All | Footer "© 2026 EShop SUT…" | Text | Thông tin bản quyền | static (observed) |

## Login (`/login`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Login | Heading "Đăng Ký" | Heading (`<h2>`) | Tiêu đề trang | static (observed); tag `<h2>`, không có `<h1>` (DevTools) |
| Login | Label "Username" | Label | Nhãn cho field email | static (observed) |
| Login | Field email | Input `type="text"` | Nhập email | empty (observed `login-empty`); filled (observed `login-error`); focus (assumed) |
| Login | Label "Mật khẩu" | Label | Nhãn cho field password | static (observed) |
| Login | Field password | Input `type="text"` | Nhập password | empty (observed); filled, hiện plain text (observed `login-locked`); focus (assumed) |
| Login | "Quên mật khẩu?" | Link | Mở Forgot Password | default (observed); hover (assumed) |
| Login | "Sign In" | Button (submit, xanh dương) | Gửi form login | default (observed); `tabIndex=1` (DevTools); không thấy loading/disabled (observed) |
| Login | "Chưa có tài khoản? Đăng ký ngay" | Text + link | Mở Register | default (observed) |
| Login | Error banner "Đăng nhập thất bại. Vui lòng kiểm tra lại." | Inline alert (đỏ) | Báo login thất bại | hidden (observed `login-empty`); visible khi sai password (observed `login-error`); visible, cùng nội dung, khi bị lock (observed `login-locked`); nằm dưới button submit (observed) |

## Register (`/register`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Register | Heading "Đăng Ký Tài Khoản" | Heading (`<h2>`) | Tiêu đề trang | static (observed); không có `<h1>` (DevTools) |
| Register | Error banner "Mật khẩu quá yếu!…" | Inline alert (đỏ) | Báo lỗi đăng ký | hidden (observed `register-empty`); visible sau khi submit password bị từ chối (observed `register-error`); nằm trên các field (observed) |
| Register | Label + field "Họ Tên" | Label + Input `type="text"` | Nhập họ tên | empty (observed); filled (observed); focus (assumed) |
| Register | Label + field "Email" | Label + Input `type="text"` | Nhập email | empty (observed); filled (observed); `type="text"` (DevTools) |
| Register | Label + field "Mật khẩu" | Label + Input `type="password"` | Tạo password | empty (observed); filled, masked (observed) |
| Register | Hint "Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt." | Help text (chữ nhỏ, xám nhạt) | Giải thích password rule | luôn hiện (observed); không đổi khi lỗi (observed) |
| Register | "Đăng Ký" | Button (submit, đỏ) | Tạo tài khoản | default (observed); không thấy loading/disabled (observed) |
| Register | "Đã có tài khoản? Đăng nhập" | Text + link | Mở Login | default (observed) |

## Forgot Password — Step 1 (`/forgot-password`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| FP step 1 | Heading "Quên Mật Khẩu" | Heading (`<h2>`) | Tiêu đề trang | static (observed); không có `<h1>` (DevTools) |
| FP step 1 | Label + field "Nhập Email của bạn" | Label + Input `type="text"` | Nhập email đã đăng ký | empty (observed `forgot-step1`); filled/focus (assumed) |
| FP step 1 | "Lấy mã OTP" | Button (submit, xanh dương) | Request OTP, sang step 2 | default (observed) |
| FP step 1 | Thông báo email không tồn tại | (chưa xác định) | Báo lỗi request | chưa kiểm chứng (assumed) |

## Forgot Password — Step 2 (cùng URL `/forgot-password`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| FP step 2 | Heading "Quên Mật Khẩu" | Heading (`<h2>`) | Tiêu đề trang | static (observed) |
| FP step 2 | Info box "Mã OTP của bạn là: 4452" | Inline info (xanh lá) | Hiện OTP (demo) | visible sau khi request (observed `forgot-step2`); OTP 4 chữ số (observed) |
| FP step 2 | Label + field "Mã OTP (4 số)" | Label + Input `type="text"` | Nhập OTP | empty (observed); paste (assumed) |
| FP step 2 | Label + field "Mật khẩu mới" | Label + Input `type="password"` | Nhập password mới | empty (observed) |
| FP step 2 | "Đặt lại mật khẩu" | Button (submit, xanh lá) | Gửi OTP + password mới | default (observed) |
| FP step 2 | "← Quay lại" | Button (xanh lá, cùng style với submit) | Quay về step 1 | default (observed) |
| FP step 2 | Kết quả reset (thành công / OTP sai / password yếu) | (chưa xác định) | Báo kết quả | chưa kiểm chứng (assumed) |

## Profile (`/profile`)

| Screen | Element | Type | Purpose | States |
|---|---|---|---|---|
| Profile | Heading "Hồ sơ của bạn" | Heading (`<h2>`) | Tiêu đề khối hồ sơ | static (observed); không có `<h1>` (DevTools) |
| Profile | Label + field "Email (Không đổi)" | Label + Input disabled | Hiện email, read-only | disabled, nền xám, value `test@eshop.com` (observed) |
| Profile | Label + field "Họ Tên" | Label + Input `type="text"` | Sửa họ tên | filled "Test User" (observed) |
| Profile | Label + field "Số điện thoại" | Label + Input `type="text"` | Sửa SĐT | empty, placeholder "VD: 0912345678" (observed) |
| Profile | Label + textarea "Địa chỉ giao hàng" | Label + Textarea (resize được) | Sửa địa chỉ | empty, placeholder "Nhập địa chỉ của bạn" (observed) |
| Profile | "Cập nhật" | Button (submit, xanh dương) | Lưu hồ sơ | default (observed) |
| Profile | Thông báo lưu thành công / lỗi | (chưa xác định) | Báo kết quả lưu | chưa kiểm chứng (assumed) |
| Profile | Heading "Lịch sử đơn hàng" + text "Bạn chưa có đơn hàng nào." | Heading + empty state (chỉ có text) | Order history (FR-11, ngoài G1) | empty (observed) |

## Expected by spec but absent

Các element spec yêu cầu nhưng **không có** trong screenshot. Đây là input cho checklist, chưa phải verdict.

| Screen | Element spec yêu cầu | Requirement |
|---|---|---|
| All | Mỗi trang có đúng 1 `<h1>` | FR-21 |
| Header | Navbar highlight trang hiện tại | FR-23 |
| Header | Badge số lượng trên "Giỏ hàng" | FR-23 |
| Header | Nút logout ghi "Đăng xuất" (thay vì "Thoát") | FR-23 |
| Login, Register, FP, Profile | Dấu `*` cạnh label của field bắt buộc | FR-22 |
| Login | Field email `type="email"`, field password `type="password"` | FR-02, FR-22 |
| Register | Field "Xác nhận mật khẩu" | FR-01 |
| Register, FP step 1 | Field email `type="email"` | FR-22 |
| FP step 1, 2 | Step indicator "Bước 1 / 2", "Bước 2 / 2" | FR-03, FR-22 |
| FP step 1 | Button "Quay lại đăng nhập" | FR-03 |
| FP step 2 | Field "Xác nhận mật khẩu mới" | FR-03 |
| FP step 2 | OTP 6 chữ số | FR-03, SEC-07 |

## Inventory notes (quan sát để dùng ở P02–P05, chưa phải Passed/Failed)

- Ngôn ngữ không nhất quán: Login có "Username", "Sign In" giữa UI tiếng Việt (FR-21).
- Màu button: "Đăng Ký" là submit nhưng màu đỏ; ở FP step 2 cả submit và "← Quay lại" đều xanh lá (FR-21).
- Login: heading ghi "Đăng Ký"; error banner nằm dưới button submit (FR-22 yêu cầu ở trên).
- Login locked và wrong-password giống hệt nhau (FR-02: không lộ nguyên nhân). Việc không có thời gian unlock là vấn đề usability, không phải vi phạm FR-02.
- `tabIndex=1` trên "Sign In" làm Tab nhảy vào button trước các field (FR-21 Tab Order).
- Header render "Chào, {name}" bằng HTML; name chứa thẻ HTML có thể chạy được (SEC-04).
- Step 1 và step 2 của Forgot Password dùng chung URL, reload trang thì mất step 2.
- Ngoài screenshot, cần tự kiểm bằng DevTools: thẻ heading, `type` của input, tab order, `autocomplete`.
```

**AI output:**
```text
Đây là 18 item IA-04 dựa trên inventory đã review. Bản nháp đã lưu vào `checklist/ia-04.md`. Bạn chưa dán tiêu đề các mục trong slide nên mình nhóm theo thứ tự: error feedback → success feedback → empty/loading/error states → submit states → feedback accessibility. Chưa chạy Passed/Failed.

# IA-04 — Feedback / State Checklist (G1 Account Screens)

- **Scope:** Login, Register, Forgot Password step 1/2, Profile, shared feedback/state areas.
- **Input:** reviewed `checklist/inventory.md` + `screenshots/input/spec-G1.md`.
- **Slide note:** The lecture slide headings were not pasted in the prompt, so the items are grouped by the usual IA-04 sub-areas: error feedback, success feedback, empty/loading/error states, submit states, and feedback accessibility. Re-map IDs if the slide uses a different order.
- **Status:** Draft for human review — no Passed/Failed execution yet.
- **Req column:** FR-21..24 are the GUI requirement sources; "—" means the item is a general feedback/state heuristic not tied to a single FR.

| ID | Screen | Element | Check | Expected Result | Req |
|---|---|---|---|---|---|
| IA-04-01 | Login | Error banner after wrong password | Wrong credentials produce a visible error that does not reveal whether the email exists or which field is wrong. | Banner appears; text is generic ("Đăng nhập thất bại...") and does not say "email not found" or "wrong password". | FR-02 |
| IA-04-02 | Login | Locked-account feedback | After repeated failures lock the account, the UI tells the user it is locked and when to retry, without revealing credential details. | A distinct lock message/countdown is shown (e.g., "Tài khoản tạm khóa, thử lại sau 30 giây"); it is not identical to the wrong-password message; no email/password detail is leaked. | FR-02 |
| IA-04-03 | Login | Error-banner lifecycle | The previous login error is cleared or updated when the user edits a field or retries. | Editing email/password removes the old error; a new submit shows only the current result; no stale error remains. | — |
| IA-04-04 | Register | Success feedback after registration | A successful registration gives visible confirmation before or while redirecting to Login. | After a valid submit, a success message/toast ("Đăng ký thành công") is shown; the app then navigates to `/login`; the redirect is not silent. | FR-01 |
| IA-04-05 | Register | Weak-password error message | The weak-password message accurately lists the rule that failed and matches the actual validation. | Message names the missing uppercase/lowercase/digit/special requirement; it does not claim "special character" when the validator actually requires a space; it stays visible until corrected. | FR-01 |
| IA-04-06 | Register | Duplicate-email error message | A duplicate email produces a human-readable message, not a raw database/API error. | Banner says the email is already registered (e.g., "Email đã được sử dụng"); no `SQLITE_CONSTRAINT`, SQL, or stack trace is shown. | FR-01 |
| IA-04-07 | Forgot Password — Step 1 | Unknown-email feedback | An unknown email produces a generic, non-enumerating message and does not use a blocking `alert()`. | Inline message says the request could not be completed / check the email; it does not say "User not found"; no `window.alert` dialog. | FR-03 |
| IA-04-08 | Forgot Password — Step 2 | OTP success info box | After requesting an OTP, the screen clearly presents it as an informational/success state. | Green info box shows the OTP and remains visible while the user types it; it is not styled as an error; the message identifies the email the OTP belongs to. | FR-03 |
| IA-04-09 | Forgot Password — Step 2 | Wrong-OTP error | A wrong OTP produces a specific inline error near the OTP field and preserves the entered values. | Error says the OTP is invalid/expired; it is inline (not only `alert()`); email and OTP fields are not cleared unexpectedly; the user can retry. | FR-03 |
| IA-04-10 | Forgot Password — Step 2 | Reset-success feedback | A successful reset confirms that the password changed before or while redirecting to Login. | A visible success message ("Đặt lại mật khẩu thành công") is shown; the app then navigates to `/login`; the old password no longer works. | FR-03 |
| IA-04-11 | Profile | Update-success feedback | Saving the profile gives visible confirmation and reflects the new values. | A success toast/inline message appears; the form shows the saved values after reload; the save is not silent. | FR-04 |
| IA-04-12 | Profile | Update-error feedback | An invalid phone or failed save shows a specific, actionable error instead of a generic failure. | Message identifies the invalid field/rule (e.g., "Số điện thoại phải bắt đầu bằng 0 và có 10–11 chữ số") or the server problem; not just "Lỗi cập nhật". | FR-04 |
| IA-04-13 | Profile | Order-history empty state | The empty order history uses an icon/illustration plus a friendly message, per FR-24. | At least one icon/illustration is visible with the message "Bạn chưa có đơn hàng nào."; the panel is not text-only. | FR-24 |
| IA-04-14 | Profile | Order-history loading state | While orders are being fetched, the order-history panel shows a loading indicator/skeleton. | A spinner/skeleton/loading text is visible during the request; the panel does not look empty or frozen. | — |
| IA-04-15 | Profile | Order-history error state | If the order request fails, the panel shows an error message and a retry action, not the empty state. | Error text (e.g., "Không tải được đơn hàng") and a "Thử lại" button are shown; the empty-state message is not used for a failed request. | — |
| IA-04-16 | All G1 forms | Submit loading/disabled state | Clicking submit immediately shows a loading/disabled state and prevents duplicate submissions. | Button becomes disabled or shows a spinner/label; a second click does nothing; exactly one request per submit in DevTools Network. | — |
| IA-04-17 | All G1 screens | Feedback accessibility | Error and success messages are announced to assistive technology. | Feedback container has `role="alert"`/`aria-live="assertive"` for errors or `role="status"`/`aria-live="polite"` for success; a screen reader announces the message when it appears. | — |
| IA-04-18 | All G1 forms | Network/API failure state | When the API is unreachable or returns 5xx, the form shows a human-readable failure and keeps the user's input. | Message says the server/network failed and to try again; no raw JSON/stack; entered values remain; a retry is possible. | — |

📝 Đã ghi log #5 vào report/ai-audit.md
```

### 6
- **Công cụ AI:** OpenCode — DeepSeek V4.1 Flash Free
- **Ngày giờ:** 04/11/2026 01:43
- **Bước:** P05b — Review checklist (trùng / measurable / IA)
- **File đã đọc:** checklist/gui-checklist.xlsx
- **File đã sửa:** report/ai-audit.md
- **Ghi chú:** Checklist review có 67 item (IA-01: 17, IA-02: 17, IA-03: 17, IA-04: 16); sheet `Review` ghi 3 item đã xóa (IA-02-10, IA-04-14, IA-04-15).

**Prompt:**
```text
Đây là checklist sau khi tôi review (<N> item). Check giúp: item trùng nhau, item không measurable, item xếp sai IA.
KHÔNG thêm item mới. Chỉ trả về: | ID | Issue | Suggested fix |.
<dán các cột ID, IA, Check, Expected Result>
```

**AI output:**
```text
| ID | Issue | Suggested fix |
|---|---|---|
| IA-04-05 | Trùng phần kiểm tra nội dung message với IA-02-06: cả hai đều yêu cầu message nêu rule bị thiếu. | Giữ IA-02-06 chỉ kiểm accept/reject; bỏ clause “message names…” khỏi IA-02-06. IA-04-05 là nơi duy nhất kiểm nội dung/độ chính xác của message. |
| IA-04-06 | Trùng scenario duplicate email với IA-02-07: cả hai submit `test@eshop.com` và expect thông báo “email đã đăng ký”. | IA-02-07 chỉ kiểm reject + vẫn ở Register; IA-04-06 chỉ kiểm message không lộ raw DB/API/SQL. Hoặc gộp vào IA-02-07 và xóa IA-04-06. |
| IA-04-08 | Trùng assertion “info box hiển thị OTP” với IA-02-12. | IA-02-12 chỉ kiểm OTP đúng 6 digits + input nhận 6, từ chối 5/7; IA-04-08 chỉ kiểm presentation (info/success, không phải error, còn hiển thị khi nhập). |
| IA-04-09 | Trùng assertion “inline error, không alert” với IA-02-14. | IA-02-14 chỉ kiểm vị trí above submit + không `window.alert`; IA-04-09 chỉ kiểm nội dung lỗi OTP + giữ nguyên email/OTP để retry. |
| IA-04-12 | Trùng assertion “invalid phone error” với IA-02-15. | IA-02-15 chỉ kiểm accept/reject + persistence; IA-04-12 chỉ kiểm message specificity + server failure. Bỏ “with a message” khỏi IA-02-15. |
| IA-04-04 | Trùng assertion “navigates to `/login`” với IA-03-13; clause redirect cũng thuộc IA-03. | Bỏ clause redirect khỏi IA-04-04; chỉ giữ success message. Nếu giữ timing, định nghĩa thời gian hiển thị tối thiểu thay vì “before or while redirecting”. |
| IA-01-11 | Trộn visual (IA-01) với behavior “cannot be edited” (IA-02); behavior này trùng IA-02-16. | Bỏ “cannot be edited” khỏi IA-01-11; chỉ giữ visual distinction/geometry. Behavior read-only giữ ở IA-02-16. |
| IA-02-18 | Expected “browser offers save/fill” phụ thuộc password manager/browser settings, không deterministic. | Bỏ clause browser offer; chỉ kiểm `autocomplete` attribute trong DOM. |
| IA-03-04 | “0 (or a documented empty-cart state)” cho hai kết quả; “documented” không định nghĩa. | Chốt một expected: badge hiện `0` khi empty, hoặc badge ẩn khi empty. Bỏ “or a documented empty-cart state”. |
| IA-03-06 | Screen = Login nhưng Check nói “from any G1 screen”; không verify được “any” chỉ từ Login. | Đổi Screen thành “All G1 screens” hoặc đổi Check/Expected thành “from Login”. |
| IA-03-12 | “clear message or restores step 2” + Back “step 1/previous” + “no dead end”: nhiều outcome, không có tiêu chí pass/fail duy nhất. | Chỉ giữ một hành vi: Refresh → step 1 (email trống); bỏ phần Back. Bỏ “clear message” chung chung. |
| IA-03-14 | “Home or the originally requested page” / “`/` (or the return URL)” không xác định. | Chốt `/` nếu app không có return URL; hoặc định nghĩa rõ case return URL. |
| IA-03-16 | “redirect to `/login` or clear login prompt” — hai outcome, “clear” chủ quan. | Chốt một: redirect `/login` (hoặc prompt với text cụ thể). Bỏ “or”. |
| IA-03-17 | “Home or Profile” — hai outcome. | Chốt một đích (ví dụ `/`). Bỏ “Home or Profile”. |
| IA-02-05 | “no account is created” không kiểm trực tiếp trên UI; mâu thuẫn với việc đã bỏ “user count unchanged” ở IA-02-07. | Đổi expected thành: sau mismatch, đăng nhập bằng credential vừa submit phải thất bại; hoặc bỏ clause “no account is created”. |
| IA-03-03 | “active style” không định nghĩa. | Định nghĩa cụ thể: `aria-current="page"` + style (màu/underline/background) khác item thường. |
| IA-04-17 | “screen reader announces” phụ thuộc AT/browser, khó deterministic. | Kiểm `role`/`aria-live` trong DOM + accessibility tree; manual screen reader chỉ là optional, không làm tiêu chí pass/fail duy nhất. |
| IA-01-05 | “neutral/outline or otherwise clearly secondary” chủ quan. | Định nghĩa style cụ thể (ví dụ: nền trắng, border xám, không xanh/đỏ) thay vì “otherwise clearly secondary”. |
| IA-04-16 | “immediately” không có mốc thời gian. | Định nghĩa “immediately” = button disabled/spinner trước khi request hoàn tất; dùng DevTools throttling để quan sát. |
| IA-04-13 | Order History là FR-11, ngoài scope G1; IA-04-14/15 đã bị xóa vì lý do này nhưng IA-04-13 còn. | Xóa khỏi checklist G1; nếu cần thì chuyển sang checklist FR-11. |
```

📝 Đã ghi log #6 vào report/ai-audit.md
