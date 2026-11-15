# Observation notes — P7

| Field                                | Value                                                                                                                         |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Participant code                     | P7                                                                                                                            |
| Ngày | 15/11/2026 |
| Device | Laptop Linux x86_64, Chrome 155.0.8059.84, viewport 1440×900 |
| Start / End time | 10:45 / 11:13 (10:45:07 → 11:13:07) |
| Consent ghi hình + ghi âm | Có |
| Task completed                       | No (Register = blocker, Reset = blocker, Profile = blocker; Lockout = With help)                                              |
| Time on task — Register             | 04:07                                                                                                                         |
| Time on task — Nhận ra bị lockout | 01:58                                                                                                                         |
| Time on task — Reset password       | 04:56                                                                                                                         |
| Time on task — Update Profile       | 04:10                                                                                                                         |
| Số lần moderator can thiệp | 8 (4 câu trung lập; 1 lần đưa tài khoản dự phòng ở Register; 2 lần cho bỏ chặng ở Reset và Profile; 1 lần nhập hộ mật khẩu gốc, lệch rule) |
| SUS score | 30.0 |
| Recording | Có (ghi âm + quay màn hình) |

## Observations

Mốc thời gian tính từ 10:45:07 (lúc đưa card 1).

| Time (mm:ss)   | Step/Screen                        | Observation                                                                                                                                                               | Quote (nguyên văn)                                                                                                                         | Type        | Moderator intervened? |
| --- | --- | --- | --- | --- | --- |
| 00:18 | Home                               | Mở trang chủ, bấm "Đăng ký" ở góc phải.                                                                                                                          | "Thấy nút rồi, bấm luôn." | success     | N                     |
| 00:33 | Register — form                   | Form 3 ô. Dòng yêu cầu mật khẩu là chữ xám nhỏ dưới ô.                                                                                                       | "Dễ. Mật khẩu mình ghép tên với sáu số." | success     | N                     |
| 00:57 | Register — nhập                  | Nhập "Đức Huy", email trên card, mật khẩu `Huy@123456`. Không đọc dòng chữ nhỏ.                                                                       | "Dòng chữ xám bé tí đó chắc chẳng quan trọng, bấm Đăng Ký luôn." | success     | N                     |
| 01:21 | Register — lỗi 1                 | Báo đỏ: "Mật khẩu quá yếu! ... KÝ TỰ ĐẶC BIỆT". Lỗi hiện sau vài giây, không có dấu hiệu đang xử lý.                                               | "Ơ, mật khẩu mình có ký hiệu @ đàng hoàng mà." | error       | N                     |
| 01:43 | Register — lỗi 2                 | Thêm `!` vào cuối (`Huy@123456!`), submit, vẫn báo "quá yếu".                                                                                               | "Có chấm than rồi. Nó chưa nhận hay sao?" | error       | N                     |
| 02:13 | Register — thử lại cách cũ    | Bấm Đăng Ký lần nữa không đổi gì, vẫn lỗi như cũ.                                                                                                           | "Thử bấm lại coi, biết đâu lần trước nó lag." | frustration | N                     |
| 02:52 | Register — đổi ký tự          | Đổi sang `Huy@123456@`, vẫn lỗi.                                                                                                                                 | "Thêm @ nữa xem sao." | error       | N                     |
| 03:04 | Register — kẹt > 3 lần          | Thử `Huy@123456#`, vẫn lỗi (4 lần cùng một cách). Moderator nói: "Bạn thử đọc lại thông báo trên màn hình xem."                                    | "Đọc lại rồi. Vô lý thật, mình đủ điều kiện mà." | error       | Y                     |
| 03:40 | Register — sau can thiệp         | Thử `Huy@123456@#` (2 ký tự đặc biệt), vẫn lỗi.                                                                                                              | "Cho hai ký tự luôn xem có chịu không." | frustration | N                     |
| 04:07 | Register — blocker                | Thử `Huy@123456$` rồi `Huy@123456*`, đều lỗi (3 lần sau câu trung lập). Bỏ chặng, moderator đưa tài khoản dự phòng.                             | "Thôi mình chịu, mật khẩu kiểu gì nó cũng chê." | frustration | Y                     |
| 04:37 | Login — màn hình đầu          | Vào trang đăng nhập thì header đã hiện "Chào, Đức Huy" và nút "Thoát" dù chưa đăng nhập. Tiêu đề form là "Đăng Ký", ô "Username", nút "Sign In". | "Lạ, mình chưa đăng nhập mà sao nó chào tên 'Đức Huy'? Sao nó biết tên mình? Mà sao trang đăng nhập ghi là Đăng Ký?" | hesitation  | N                     |
| 05:41 | Login — bấm Thoát               | Bấm "Thoát" cho chắc, header trở về "Đăng nhập / Đăng ký".                                                                                                     | "Chắc ai đó đăng nhập trước, mình thoát ra rồi vào lại cho sạch." | hesitation  | N                     |
| 06:32 | Lockout — sai lần 1              | Nhập email và `abc12345` theo card. Báo "Đăng nhập thất bại. Vui lòng kiểm tra lại." ở dưới cùng form, dưới link "Đăng ký ngay".                    | "Nhập lại phát nữa." | error       | N                     |
| 06:53 | Lockout — sai lần 2              | Bấm Sign In lần nữa, cùng thông báo.                                                                                                                                | "Vẫn vậy. Chắc đúng cái mật khẩu trong sổ mà." | error       | N                     |
| 07:17 | Lockout — sai lần 3              | Gõ lại `abc12345`, cùng thông báo. Thông báo không đổi giữa các lần.                                                                                       | "Mình gõ chậm hẳn hoi rồi đó." | frustration | N                     |
| 07:41 | Lockout — kẹt > 3 lần           | Bấm lần 4, cùng thông báo. Moderator nói: "Bạn thử đọc lại thông báo trên màn hình xem."                                                                  | "Toàn báo kiểm tra lại, chẳng nói sai đâu. Thử viết hoa chữ a coi." | error       | Y                     |
| 08:09 | Lockout — đổi chữ hoa          | Thử `Abc12345`, vẫn lỗi.                                                                                                                                             | "Không được. Hay mình chép sai, hoặc quên mất rồi." | error       | N                     |
| 08:21 | Lockout — tìm thấy link         | Nhìn thấy chữ xanh nhỏ "Quên mật khẩu?" bên phải ô mật khẩu, bấm vào. Kết thúc chặng nhận ra lockout.                                                   | "À có chữ Quên mật khẩu bé bé màu xanh nè, mình quên thật mà." | success     | N                     |
| 08:51 | Reset — lấy mã                  | Nhập email, bấm "Lấy mã OTP". Trên màn hình hiện luôn "Mã OTP của bạn là: 4989".                                                                             | "Mã có sẵn trên màn hình, khỏi mở hộp thư." | success     | N                     |
| 09:18 | Reset — nhập mật khẩu mới     | Nhập OTP 4989 và mật khẩu mới `Huy@123456@`, bấm "Đặt lại mật khẩu".                                                                                      | "Mật khẩu mới thì dùng cái @ hồi nãy, chắc nó chịu." | success     | N                     |
| 09:30 | Reset — không phản hồi         | Bấm nút, màn hình không đổi: không thông báo thành công hay lỗi, không chuyển trang. Bấm thêm 3 lần, vẫn y nguyên.                                    | "Vẫn im re." | frustration | N                     |
| 10:36 | Reset — kẹt > 3 lần             | Sau 4 lần bấm không phản hồi, moderator nói: "Bạn thử đọc lại thông báo trên màn hình xem." Trên màn hình chỉ có mã OTP.                            | "Có chữ gì để đọc đâu, chỉ có cái mã OTP. Thôi qua đăng nhập thử, biết đâu đổi rồi." | error       | Y                     |
| 11:13 | Reset — thử đăng nhập         | Đăng nhập bằng mật khẩu mới, vẫn "Đăng nhập thất bại".                                                                                                       | "Chưa đổi. Làm lại." | error       | N                     |
| 11:49 | Reset — vòng 2                   | Bấm lại "Quên mật khẩu?", nhận OTP mới (5696), nhập mật khẩu `Huy123456!`.                                                                                | "Lần này đổi sang cái không có @ xem sao." | hesitation  | N                     |
| 12:22 | Reset — vòng 2 không phản hồi | Bấm "Đặt lại mật khẩu", vẫn không có phản hồi nào.                                                                                                            | "Lại im re." | frustration | N                     |
| 13:16 | Reset — blocker                   | Đăng nhập bằng `Huy123456!`, vẫn thất bại (3 lần sau câu trung lập). Bỏ chặng.                                                                          | "Mình chịu, chắc phải gọi cho shop." | frustration | Y                     |
| 13:16 → 16:46 | Chờ                               | Moderator chờ thật 03:30 để thử tài khoản lại (không nói gì về thời gian khoá).                                                                             | "Không có câu nào, participant chờ." | hesitation  | N                     |
| 16:46 | Login — moderator nhập hộ       | Moderator nhập hộ mật khẩu gốc `Abc12345 ` (lệch rule). Đăng nhập thành công, về trang chủ, header "Chào, Đức Huy".                                        | "Vào được rồi, mà sao lúc nãy chưa đăng nhập đã thấy tên mình nhỉ." | success     | Y                     |
| 17:04 | Profile — mở                     | Bấm vào "Chào, Đức Huy" ra trang "Hồ sơ của bạn" có ô SĐT, địa chỉ, nút "Cập nhật".                                                                        | "Chỗ nhập SĐT với địa chỉ đây rồi." | success     | N                     |
| 17:31 | Profile — lưu lần 1             | Nhập 0901000000 và địa chỉ, bấm "Cập nhật". Màn hình không có thông báo gì.                                                                                | "Bấm xong chả thấy báo lưu hay chưa." | hesitation  | N                     |
| 18:22 | Profile — lưu lần 2             | Bấm "Cập nhật" lần nữa, vẫn không thông báo. Nhấn F5, trang trông không đổi.                                                                                | "Chắc lưu rồi, nhưng chắc ăn thì thoát ra vào lại xem." | hesitation  | N                     |
| 18:58 | Profile — mở lại                | Thoát ra trang chủ rồi vào lại Hồ sơ: SĐT và địa chỉ trống như ban đầu.                                                                                   | "Mất sạch hết rồi! Mình nhập hai lần mà." | frustration | N                     |
| 19:47 | Profile — kẹt                    | Nhập lại lần 3, mở lại vẫn trống. Moderator nói: "Bạn thử đọc lại thông báo trên màn hình xem." Trên màn hình không có thông báo nào.           | "Không thấy chữ nào xác nhận. Thử nhập mỗi địa chỉ coi." | error       | Y                     |
| 20:56 | Profile — blocker                 | Thử chỉ địa chỉ, rồi chỉ SĐT `+84901000000`, mở lại đều trống (3 lần sau câu trung lập). Bỏ chặng.                                                    | "Thôi mình không dám lưu thông tin thật ở đây nữa." | frustration | Y                     |

## Probe answers

| # | Câu trả lời (tóm tắt + quote)                                                                                                                                                                                                                                                                                                                         |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Mình lướt qua, chữ bé tí, tưởng là gợi ý chứ có phải bắt buộc đâu. Hiểu vậy vì bản thân thông báo đỏ nói thế, nhưng mình thêm đủ rồi mà nó vẫn chê. |
| 2 | Màn hình không nói gì khác ngoài 'vui lòng kiểm tra lại', nên mình cứ tưởng mình gõ sai. |
| 3 | Mình quen thử lại trước, ít khi đi tìm chỗ khác. Mãi sau mới thấy chữ Quên mật khẩu. |
| 4 | Mình chắc bỏ luôn tài khoản này, đăng ký lại cho nhanh. Mà đăng ký thì cũng bị chê mật khẩu... |
| 5 | Mất lâu nhất là lúc bấm Đặt lại mật khẩu mà trang đứng im, mình không biết nó làm xong chưa. |
| 6 | Ba bước thì được, nhưng làm xong mình không biết đã đổi hay chưa, nên thấy thiếu cái thông báo cuối. |
| 7 | Mình thấy tiện, khỏi mở mail, nhưng nghĩ lại thì sợ, như vậy thì có khác gì không có mã. |
| 8 | Mình không dám lưu địa chỉ thật, vì nó chẳng báo gì và mất hết dữ liệu mình nhập. |
| 9 | Mình sửa chỗ đăng ký đầu tiên, vì vào không được thì mấy cái sau khỏi nói. |

### SUS (P7, thang 1–5)

| Câu   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| ------ | - | - | - | - | - | - | - | - | - | -- |
| Điểm | 3 | 4 | 2 | 3 | 2 | 4 | 2 | 4 | 2 | 4 |

Tính theo công thức SUS chuẩn: câu lẻ (điểm − 1) = 2+1+1+1+1 = 6; câu chẵn (5 − điểm) = 1+2+1+1+1 = 6; tổng 12 × 2.5 = **30.0**.

## Bug thấy trong session

Chỉ ghi hành vi thấy trên màn hình. Không kết luận nguyên nhân.

| Mô tả                                                                                                                                                                                                                                   | Screenshot                                                                                                                                                                                                                                    | Issue |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| Đăng ký: mật khẩu có chữ hoa, chữ thường, số và ký tự đặc biệt (`!`, `@`, `#`, `$`, `*`) vẫn bị báo "Mật khẩu quá yếu" qua 9 lần thử. Dòng yêu cầu nhỏ, màu xám nhạt, khó đọc.              | `screenshots/02-register-form.jpg`, `04-register-err-weak.jpg`, `05-register-err-after-bang.jpg`, `06-register-err-after-at.jpg`, `07-register-blocker.jpg`                                                                         |       |
| Đăng ký: thông báo lỗi hiện sau vài giây, chụp ngay sau khi bấm vẫn thấy form chưa đổi, không có dấu hiệu đang xử lý. Chưa chắc do ứng dụng hay do chụp màn hình trễ.                                      | `03-register-filled.jpg`                                                                                                                                                                                                                    |       |
| Trang Đăng nhập: tiêu đề form là "Đăng Ký", nhãn "Username" (thay vì Email), nút "Sign In" (tiếng Anh) lẫn với tiếng Việt.                                                                                              | `08-login-already-greeting.jpg`                                                                                                                                                                                                             |       |
| Mở trang Đăng nhập khi chưa đăng nhập: header đã hiện "Chào, Đức Huy" và nút "Thoát". Chưa rõ nguyên nhân, nên kiểm lại trên tài khoản dự phòng (chưa xác minh).                          | `08-login-already-greeting.jpg`                                                                                                                                                                                                             |       |
| Đăng nhập sai: thông báo "Đăng nhập thất bại. Vui lòng kiểm tra lại." giống hệt nhau qua 5 lần liên tiếp, nằm dưới cùng form, dưới link "Đăng ký ngay". Không có gợi ý nào dẫn tới "Quên mật khẩu?". | `09-login-fail-1.jpg` … `13-login-fail-5.jpg`                                                                                                                                                                                            |       |
| Đặt lại mật khẩu: bấm "Đặt lại mật khẩu" (7 lần, 2 vòng OTP) không có thông báo thành công hay lỗi, không chuyển trang.                                                                                             | `16-forgot-filled.jpg`, `17-reset-no-response.jpg`, `18-reset-no-response-2.jpg`, `19-reset-no-response-4.jpg`, `22-reset-no-response-5.jpg`                                                                                        |       |
| Sau khi đặt lại, đăng nhập bằng mật khẩu mới (`Huy@123456@`, `Huy123456!`) đều "Đăng nhập thất bại".                                                                                                          | `20-login-after-reset-fail.jpg`, `23-login-fail-after-reset-2.jpg`                                                                                                                                                                        |       |
| Mã OTP hiện ngay trên trang sau khi nhập email (4 số, hiển thị công khai).                                                                                                                                                        | `15-forgot-otp-shown.jpg`, `21-forgot-otp-second.jpg`                                                                                                                                                                                     |       |
| Hồ sơ: bấm "Cập nhật" (5 lần) không có thông báo nào. Thoát rồi mở lại trang thì SĐT và địa chỉ trống.                                                                                                              | `26-profile-after-save-no-feedback.jpg`, `27-profile-after-resave.jpg`, `28-profile-empty-after-reopen.jpg`, `30-profile-empty-after-3rd.jpg`, `31-profile-empty-after-address-only.jpg`, `32-profile-empty-after-phone-only.jpg` |       |
