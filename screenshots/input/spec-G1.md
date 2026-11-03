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

