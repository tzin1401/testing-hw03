# AI Audit Report — HW03 GUI & Usability

- Sinh viên: Nguyễn Lê Thế Vinh — 23120190
- Bài: HW03-AI — GUI & Usability (SUT: EShop)

**Declaration:** I use AI tools for the following tasks.

| # | Bước | Công cụ AI | Ngày giờ | Link |
|---|---|---|---|---|
| 1 | P01 — UI inventory (account screens) | OpenCode — DeepSeek V4.1 Flash Free | 04/11/2026 00:54 | [#1](#1) |

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
