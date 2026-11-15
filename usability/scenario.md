# Task scenario và task card

In mỗi card ra một tờ giấy riêng. Card 2 chỉ đưa sau khi participant xong card 1.

## Task card 1

> Bạn muốn mua đồ trên trang EShop nên cần có một tài khoản riêng.
> Hãy tạo tài khoản bằng tên của bạn và email **p<n>.hw03@test.local**.
> Bạn tự chọn mật khẩu.

## Task card 2

> Một tháng sau, bạn quay lại EShop để đặt hàng. Trong sổ tay, bạn ghi mật khẩu là: **`<moderator chép mật khẩu participant vừa tạo, đổi 1 ký tự>`**
> Hãy vào được tài khoản của mình.
> Sau đó cập nhật thông tin giao hàng: số điện thoại **<SĐT trong plan.md>**, địa chỉ **<địa chỉ trong plan.md>**.
> Bạn có thể dùng mọi cách mà bạn sẽ dùng khi ở nhà.

## Các từ cần tránh (leading words)

Không dùng trên card hoặc khi nói với participant:

| Không dùng | Lý do |
|---|---|
| "Đăng ký", "Đăng nhập", "Quên mật khẩu", "Hồ sơ", "Cập nhật" | Trùng label trên UI, chỉ thẳng vào button/link |
| "mã OTP", "đặt lại", "reset" | Tiết lộ cách recover |
| "bị khoá", "lockout" | Báo trước lỗi, participant sẽ không tự nhận ra |
| "mật khẩu mạnh", "có dấu cách" | Gợi ý cách vượt qua bug password rule |
| "nhanh", "dễ" | Đặt kỳ vọng, ảnh hưởng SUS |

## Time on task — các chặng

| Chặng | Bắt đầu | Kết thúc |
|---|---|---|
| Register | Đưa card 1 | Màn hình chuyển sang trang Login sau khi đăng ký thành công |
| Nhận ra bị lockout | Lần submit login sai đầu tiên | Participant bấm "Quên mật khẩu?" (hoặc nói ra là tài khoản bị khoá) |
| Reset password | Bấm "Quên mật khẩu?" | Login thành công bằng mật khẩu mới |
| Update Profile | Login thành công | Lưu thành công cả SĐT và địa chỉ (hoặc bỏ cuộc) |
