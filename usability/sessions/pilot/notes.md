# Pilot

| Field            | Value                                                                 |
| ---------------- | --------------------------------------------------------------------- |
| Participant code | Pilot                                                                 |
| Ngày | 12/11/2026 |
| Device | Laptop Linux x86_64, Chrome 155.0.8059.84, viewport 1366×768 |
| Start / End      | 15:00 / 15:05 (≈ 5 phút) |
| Consent ghi hình + ghi âm | Có |
| Recording | Có (ghi âm + quay màn hình) |
| Email dùng      | pilot.hw03@test.local                                               |
| Task completed   | **No** — 3/4 chặng BLOCKED, 1 chặng không quan sát được |
| Screenshot       | `screenshots/01…14` (theo thứ tự bước)                         |

## 1. Bảng quan sát

| Bước | Màn hình      | Hành động                                                       | Suy nghĩ (think-aloud)                                                                                                                  | Type       |
| ------ | --------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 1      | Home            | Bấm "Đăng ký" góc phải                                       | "Muốn tạo tài khoản, thấy ngay nút Đăng ký."                                                                                    | success    |
| 2      | Register        | Đọc form                                                         | "Dòng gợi ý dưới ô mật khẩu chữ bé, xám nhạt, phải nheo mắt mới đọc được."                                           | friction   |
| 3      | Register        | Nhập tên, email, mật khẩu `Mai@12345`                      | "Không có nút con mắt, không có ô nhập lại mật khẩu — sợ gõ sai."                                                          | hesitation |
| 4      | Register        | Bấm Đăng Ký → "Mật khẩu quá yếu! … KÝ TỰ ĐẶC BIỆT." | "Ơ? Mình nhập đủ kiểu rồi, sao vẫn báo yếu?"                                                                          | error      |
| 5      | Register        | Đổi thành `Mai!12345`, submit                               | "Thông báo y nguyên, không biết nó có gửi lại không hay vẫn là thông báo cũ."                                             | error      |
| 6      | Register        | Đổi thành `Mai#2026!$`, submit                            | "Lần 3 vẫn vậy. Bỏ cuộc." → **BLOCKED**                                                                                      | error      |
| 7      | Login           | Bấm "Đăng nhập" trên header                                   | "Lạ, bấm Đăng nhập mà tiêu đề ghi 'Đăng Ký'? Ô ghi 'Username' — mình có username đâu. Nút lại tiếng Anh 'Sign In'." | friction   |
| 8      | Login           | Nhập email + `mai#2026!$` (theo card 2)                     | "Ô mật khẩu hiện rõ chữ, ai đứng sau là thấy!"                                                                                 | friction   |
| 9      | Login           | Submit → "Đăng nhập thất bại. Vui lòng kiểm tra lại."     | "Sai email hay sai mật khẩu? Không biết."                                                                                            | error      |
| 10     | Login           | Thử lại với `Mai#2026!$`                                  | "Chắc lúc tạo mình gõ chữ hoa." → vẫn thất bại, không thấy báo khoá                                                        | error      |
| 11     | Forgot password | Bấm "Quên mật khẩu?"                                           | "Ở nhà thì mình bấm quên mật khẩu thôi."                                                                                        | success    |
| 12     | Forgot password | Nhập email, bấm "Lấy mã OTP"                                   | "Bấm rồi mà không có gì xảy ra — không báo đã gửi, không có ô nhập OTP."                                                | error      |
| 13     | Forgot password | Đợi, bấm lại                                                   | "Lần 2 vẫn im."                                                                                                                        | error      |
| 14     | Forgot password | Nhấn Enter trong ô email                                         | "Không phản hồi gì cả. Bỏ." → **BLOCKED**                                                                                   | error      |
| —     | Profile         | Không vào được (chưa đăng nhập)                           | —                                                                                                                                       | BLOCKED    |

## 2. Thời gian và kết quả từng chặng

| Chặng               | Bắt đầu → Kết thúc | Thời gian | Kết quả                                                                                                                                                                                         |
| -------------------- | ------------------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Register             | 15:00:00 → 15:02:09     | ~2:09      | **BLOCKED** — 3 lần submit bị từ chối dù mật khẩu đủ các loại ký tự đang hiển thị                                                                                          |
| Nhận ra bị lockout | 15:02:09 → ~15:03:23    | ~1:14      | **Không quan sát được** — tài khoản không tồn tại, 2 lần sai không có thông báo khoá; participant tự sang "Quên mật khẩu?" vì thói quen, không phải vì hiểu lỗi |
| Reset password       | ~15:03:23 → 15:05:00    | ~1:37      | **BLOCKED** — "Lấy mã OTP" không có phản hồi (có thể do email chưa đăng ký, nhưng UI không nói gì)                                                                         |
| Update Profile       | —                       | —         | **BLOCKED** — không bắt đầu được                                                                                                                                                    |
| **Tổng**      | 15:00:00 → 15:05:00     | ~5:00      | 0/4 chặng hoàn thành                                                                                                                                                                           |

**Nhận xét:** các chặng nối tiếp nhau, chặng 1 bị chặn là 3 chặng sau không chạy được. Lỗi nằm ở kịch bản chứ không chỉ ở trang.

## 3. Những chỗ task card chưa ổn

Buổi pilot lộ ra mấy chỗ trong card dễ làm participant hiểu sai hoặc bị lệch hướng. Mình ghi lại để sửa trước buổi P1.

| Card | Câu                                                                                      | Vấn đề                                                                                                                                                                               |
| ---- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | "tạo tài khoản bằng **tên của bạn**"                                         | Thu tên thật → lọt vào recording/notes, không giữ được ẩn danh cho P1…P7.                                                                                                           |
| 1    | "email **p<n>.hw03@test.local**"                                                | Placeholder `<n>` dễ điền sai; buổi này dùng `pilot.hw03@test.local`, chưa có trong bảng test data.                                                                  |
| 2    | "mật khẩu là: `<moderator chép mật khẩu participant vừa tạo, đổi 1 ký tự>`" | Nếu Register bị block như hôm nay thì không có mật khẩu nào để chép. Nếu participant thử nhiều mật khẩu thì moderator không biết lấy cái nào. |
| 2    | "**cập nhật** thông tin giao hàng"                                              | Dùng chữ "cập nhật" là leading word, nằm trong danh sách không dùng.                                                                                                   |
| 2    | "số điện thoại **<SĐT trong plan.md>**, địa chỉ **<…>**"             | Card in ra còn placeholder → participant phải hỏi moderator. Điền sẵn từng card.                                                                                                |
| 2    | "Bạn có thể dùng **mọi cách** mà bạn sẽ dùng khi ở nhà."                | Gợi ý quá nhiều: câu này chỉ thẳng sang "Quên mật khẩu?", làm hỏng chỉ số O2 (thời gian tự nhận ra lockout).        |
| 2    | Không nói bao nhiêu lần thử                                                          | Participant chỉ thử 2 lần rồi đi quên mật khẩu → chưa chắc chạm ngưỡng lockout. Chặng "Nhận ra bị lockout" có thể không xảy ra với người thật.                 |

## 4. Việc cần sửa trước buổi P1

### Task card

- Card 1: "Hãy tạo tài khoản với tên **Minh Anh** và email **p1.hw03@test.local**" — in sẵn tên giả + email cụ thể cho từng P, bỏ `<n>`.
- Card 2: bỏ câu "dùng mọi cách…". Thay bằng: "Hãy vào được tài khoản của mình và thêm thông tin giao hàng: SĐT 0901000003, địa chỉ 45 …" (in sẵn, không dùng chữ "cập nhật").
- Card 2 in **trước 2 phiên bản**: (A) dùng mật khẩu participant tự tạo, (B) dùng tài khoản dự phòng. Moderator chọn A/B tuỳ chặng Register.
- Moderator ghi lại **mật khẩu cuối cùng được chấp nhận** ngay khi đăng ký thành công (thêm một dòng vào mẫu ghi chú).

### Dữ liệu test

- Tài khoản dự phòng `backupN.hw03@test.local` đang thiếu mật khẩu trong bảng. Cần thêm cột mật khẩu, tạo sẵn trước buổi và thử đăng nhập.
- Thêm sẵn cột "Mật khẩu card 2" cho tài khoản dự phòng (đã đổi 1 ký tự).
- Email `@test.local` không có hộp thư thật. Phải ghi rõ participant lấy OTP ở đâu (Mailpit mở sẵn ở tab 2, hoặc moderator đọc mã), nếu không chặng Reset sẽ luôn bị chặn.
- Xoá tài khoản test giữa các buổi, để email không bị "đã tồn tại".
- Thêm email `pilot.hw03@test.local` vào bảng test data.

### Cách can thiệp

- Thêm ngưỡng **theo số lần**, không chỉ theo thời gian: "Bị từ chối **3 lần** liên tiếp cùng một thông báo → câu trung lập". 3 phút + 2 phút = 5 phút chỉ cho Register là quá dài cho buổi ~30 phút.
- Khi Register bị block → đưa **card 2 phiên bản B** (tài khoản dự phòng), không chỉ "đi tiếp".
- Chặng Reset: nếu bấm "Lấy mã OTP" không phản hồi quá 1 phút → moderator nói "Bạn thử kiểm tra hộp thư xem" (trung lập, không nói OTP) hoặc cho bỏ qua sang Profile bằng tài khoản dự phòng đã đăng nhập sẵn.
- Ghi rõ: chặng phụ thuộc chặng trước bị block → đánh dấu "N/A (dependent)", không tính là fail của chặng đó khi phân tích O2–O4.

## 5. SUS (thang 1–5)

| #  | Câu                                                            | Điểm (1–5) |
| -- | --------------------------------------------------------------- | ------------- |
| 1  | Tôi nghĩ tôi sẽ muốn dùng hệ thống này thường xuyên | 2             |
| 2  | Hệ thống phức tạp không cần thiết                        | 4             |
| 3  | Hệ thống dễ dùng                                            | 1             |
| 4  | Tôi cần người kỹ thuật hỗ trợ mới dùng được        | 4             |
| 5  | Các chức năng được tích hợp tốt                        | 2             |
| 6  | Có quá nhiều điểm không nhất quán                       | 5             |
| 7  | Hầu hết mọi người sẽ học dùng rất nhanh                | 2             |
| 8  | Hệ thống rất rườm rà                                      | 4             |
| 9  | Tôi thấy tự tin khi dùng                                    | 1             |
| 10 | Tôi phải học nhiều thứ trước khi dùng được           | 3             |

**SUS = (1+0+1+1+0 + 1+1+0+1+2) × 2.5 = 20.0** (dưới benchmark 68 rất xa).

**Phản hồi của người dùng:**

> "Nói thật là mình bực. Mật khẩu đủ chữ hoa, chữ thường, số, ký tự đặc biệt như nó ghi mà vẫn bảo yếu, thử ba lần câu nào cũng y chang, không biết sai ở đâu. Bấm Đăng nhập thì trang ghi 'Đăng Ký', ô thì bắt 'Username' trong khi mình chỉ có email, mật khẩu hiện rõ chữ nữa — không yên tâm. Quên mật khẩu thì bấm nút chẳng có gì xảy ra. Ở nhà chắc mình tắt tab, mua chỗ khác."
