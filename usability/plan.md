# Usability Test Plan — G1 Authentication & Account

- **Phương pháp:** moderated usability evaluation, think-aloud, 7 participant (P1–P7) + 1 pilot.
- **Flow:** Register → Login sai nên bị lockout → tự recover qua "Quên mật khẩu" (OTP 2 bước) → Login → cập nhật Profile (họ tên, SĐT, địa chỉ).
- **SUT:** EShop web `http://localhost:5173`, commit `85af3ba`, Google Chrome desktop trên máy của moderator.
- **Target user:** 18–35 tuổi, đã từng mua hàng online ít nhất 1 lần/tháng, không làm IT/tester, không học lớp HW03.
- **Thang đo sau session:** SUS 10 câu (bản tiếng Việt, xem `sus-form.md`).

## Objectives (ISO 9241-11)

| # | Objective | Research question | Metric | Success threshold |
|---|---|---|---|---|
| O1 | Effectiveness — đăng ký | Người dùng có tự tạo được tài khoản với rule password đang hiển thị không? | Task success chặng Register (Yes / With help / No); số lần submit bị từ chối | ≥ 5/7 tự hoàn thành không cần can thiệp |
| O2 | Effectiveness — nhận ra lockout | Người dùng có hiểu vì sao không đăng nhập được và biết hướng tự khắc phục không? | Thời gian từ lần login sai đầu tiên tới khi bấm "Quên mật khẩu?"; quote cho thấy hiểu/không hiểu nguyên nhân | ≥ 5/7 tự tìm tới "Quên mật khẩu?" trong 2 phút |
| O3 | Efficiency — reset password | Flow OTP 2 bước có nhanh và rõ ràng không? | Time on task chặng Reset; số lỗi (OTP sai, password bị từ chối, login lại vẫn bị khoá) | Median ≤ 3 phút; ≤ 1 lỗi/người |
| O4 | Efficiency — cập nhật Profile | Người dùng có lưu được SĐT và địa chỉ thật của mình không? | Task success chặng Profile; số lần lưu thất bại | ≥ 6/7 lưu thành công |
| O5 | Satisfaction & trust | Người dùng cảm thấy flow tài khoản dễ dùng và đáng tin không? | SUS score; probe nhóm trust | SUS mean ≥ 68 (benchmark) |

## Ghi chú về SUT trước khi chạy (moderator đọc, không nói cho participant)

Các hành vi dưới đây đã thấy ở Task 1. Chúng dự kiến gây friction. Moderator chỉ quan sát, không giải thích:

- Password rule thực tế bắt buộc có **dấu cách** và cấm ký tự đặc biệt, trái với hint trên màn hình (issue #15).
- Login sai **2 lần** là bị khoá **180 giây**. Thông báo khi bị khoá giống hệt thông báo sai password.
- Reset password **không** mở khoá tài khoản: nếu reset xong trong 180 giây thì login bằng password mới vẫn báo lỗi.
- SĐT bắt đầu bằng `0` bị từ chối (issue #23). OTP hiển thị ngay trên màn hình (demo).

## Intervention rule

| Tình huống | Moderator làm gì | Ghi vào notes |
|---|---|---|
| Kẹt **> 3 phút** ở cùng một bước | Nói một câu trung lập: *"Bạn thử đọc lại thông báo trên màn hình xem."* | Type = `error`, Moderator intervened = `Y` |
| Vẫn kẹt thêm **2 phút** sau câu trên | Cho phép bỏ qua chặng. Với Register: đưa tài khoản dự phòng (xem test data) để đi tiếp | Task completed của chặng = `No`, đánh dấu **blocker** |
| Bị khoá và chờ unlock | Không nói về thời gian khoá. Nếu participant hỏi: *"Bạn cứ làm như khi ở nhà."* | Ghi thời gian chờ thực tế |
| Participant hỏi "làm vậy đúng không?" | *"Bạn nghĩ sao?"* | Type = `hesitation` |
| Participant im lặng > 20 giây | *"Bạn đang nghĩ gì vậy?"* (nhắc think-aloud, không gợi ý) | Không tính là intervention |

## Test data

| Code | Email đăng ký | SĐT mới | Địa chỉ mới | Tài khoản dự phòng (nếu Register bị block) |
|---|---|---|---|---|
| Pilot | `pilot.hw03@test.local` | 0901000000 | 1 Nguyễn Văn Cừ, Q.5, TP.HCM | `backup0.hw03@test.local` |
| P1 | `p1.hw03@test.local` | 0901000001 | 12 Lê Lợi, Q.1, TP.HCM | `backup1.hw03@test.local` |
| P2 | `p2.hw03@test.local` | 0901000002 | 45 Trần Hưng Đạo, Q.5, TP.HCM | `backup2.hw03@test.local` |
| P3 | `p3.hw03@test.local` | 0901000003 | 78 Võ Văn Tần, Q.3, TP.HCM | `backup3.hw03@test.local` |
| P4 | `p4.hw03@test.local` | 0901000004 | 9 Pasteur, Q.1, TP.HCM | `backup4.hw03@test.local` |
| P5 | `p5.hw03@test.local` | 0901000005 | 230 Nguyễn Trãi, Q.1, TP.HCM | `backup5.hw03@test.local` |
| P6 | `p6.hw03@test.local` | 0901000006 | 56 Lý Thường Kiệt, Q.10, TP.HCM | `backup6.hw03@test.local` |
| P7 | `p7.hw03@test.local` | 0901000007 | 101 Cách Mạng Tháng 8, Q.3, TP.HCM | `backup7.hw03@test.local` |

- Tài khoản dự phòng tạo trước mỗi session bằng API, password `Abc12345 ` (có dấu cách cuối):
  ```bash
  curl -s -X POST localhost:3000/api/register -H 'Content-Type: application/json' -d '{"name":"Backup","email":"backup1.hw03@test.local","password":"Abc12345 "}'
  ```
- Email là địa chỉ test, không phải email thật của participant.
- Backend **không** restart giữa các session (restart xoá dữ liệu). Chỉ restart trước pilot.

## Session script (moderator)

1. Mở `http://localhost:5173` ở cửa sổ ẩn danh. Bật OBS (screen + micro).
2. Xin consent ghi hình + ghi âm (câu cuối Google Form, hoặc hỏi miệng và ghi vào notes).
3. Câu mở đầu: *"Mình đang test sản phẩm chứ không test bạn. Không có câu trả lời sai. Bạn cứ nói to những gì đang nghĩ nhé."*
4. Đưa **Task card 1**. Bấm giờ chặng Register.
5. Khi participant đăng ký xong: hỏi *"Bạn ghi mật khẩu vừa tạo vào giấy này giúp mình."* Moderator chép lại mật khẩu đó lên **Task card 2** nhưng **đổi 1 ký tự** (ví dụ chữ hoa đầu thành chữ thường).
6. Đưa **Task card 2**. Bấm giờ: Nhận ra bị lockout → Reset password → Update Profile.
7. Kết thúc: participant điền Google Form SUS. Sau đó hỏi probe questions.
8. **Debrief:** giải thích mật khẩu trên card 2 đã bị đổi có chủ đích để mô phỏng việc quên mật khẩu. Cảm ơn participant.
9. Dừng OBS, lưu `usability/sessions/P<n>/recording.mp4` (hoặc link Drive).
