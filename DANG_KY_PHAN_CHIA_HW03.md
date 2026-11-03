# HW03 – Đăng ký màn hình & flow (tránh trùng)

> Theo đề §5: trong nhóm, **không ai được trùng màn hình chính** (GUI checklist) **hoặc trùng flow** (usability).
> Màn hình **phụ** được phép trùng.
> Bài làm cá nhân — mỗi người tự làm checklist, tự tuyển **7 người tham gia riêng** (không dùng chung người).

## Cách đăng ký
1. Chọn **1 gói** bên dưới (ai đăng ký trước được trước).
2. Ghi tên vào bảng đăng ký cuối file và gửi lại nhóm.
3. Muốn đề xuất gói khác → ghi vào mục "Gói tự đề xuất", nhưng không được trùng màn hình chính / tính năng trọng tâm của flow với gói đã có người.
4. Hạn chốt: **<ngày/giờ>**. Sau khi chốt không đổi (vì log AI và git commit có thời gian).

## Các gói

| Gói | Màn hình chính (Task 1) | Màn hình phụ gợi ý | Flow usability (Task 2) | FR liên quan |
|---|---|---|---|---|
| **G1 – Tài khoản** | Login / Register | Forgot password, Profile | Đăng ký tài khoản → đăng nhập sai bị khóa → khôi phục mật khẩu → cập nhật hồ sơ | FR-01→04 |
| **G2 – Tìm & xem sản phẩm** | Product List / Search | Home, Product Detail | Tìm sản phẩm theo nhu cầu & mức giá → so sánh → thêm vào giỏ | FR-05, 06, 07 |
| **G3 – Thanh toán** | Checkout | Cart, Order History | Giỏ hàng có sẵn → checkout dùng mã giảm giá → kiểm tra đơn trong lịch sử | FR-07→11 |
| **G4 – Quản trị** | Admin Dashboard / Product CRUD | Category, Coupon, CSV import | Admin tạo mã giảm giá mới → sửa giá sản phẩm → xem đơn hàng | FR-12→19 |
| **G5 – Mobile** | Màn hình chính trên Mobile app (Expo) | Product, Cart trên mobile | Mua 1 sản phẩm hoàn chỉnh trên điện thoại | Pool D |

> Nhóm ít hơn 5 người thì bỏ bớt gói, không cần ghép.
> Gói G4 cần người tham gia "đóng vai admin" → nên tìm người từng bán hàng online / quản lý shop.

## Bảng đăng ký

| Thành viên | MSSV | Gói | Màn hình chính | Flow (ghi rõ) | Nền tảng Task 3 (≥3) |
|---|---|---|---|---|---|
| Nguyễn Lê Thế Vinh | 23120190 | G1 – Tài khoản | Login / Register | Đăng ký tài khoản → đăng nhập sai bị khóa → khôi phục mật khẩu → cập nhật hồ sơ |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Gói tự đề xuất (nếu có)

| Thành viên | Màn hình chính | Flow | Khác các gói trên ở điểm nào |
|---|---|---|---|
|  |  |  |  |

## Lưu ý chung
- **Không dùng chung prompt** — chép prompt giữa các bạn là 0 điểm cả hai.
- **Không dùng chung người tham gia** — TA gọi kiểm tra 2 người, trùng sẽ dễ bị nghi.
- Chụp lại bảng đã chốt, mỗi người đưa vào phần *Scope* trong report của mình.
