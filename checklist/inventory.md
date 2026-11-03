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
