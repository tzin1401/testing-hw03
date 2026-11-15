# Usability findings — G1 Auth & Account

> **Draft do AI soạn từ `sessions/P1…P7/notes.md`. Human review required**: sinh viên chốt severity, sửa recommendation, rồi mới đăng issue.
> Quote chép nguyên văn từ notes. Pilot không tính vào số liệu (chỉ dùng để sửa kịch bản).

- **Flow:** Register → Login sai, bị lockout → Quên mật khẩu (OTP) → Login → cập nhật Profile
- **N = 7** (P1–P7), 13–15/11/2026, Chrome 155 desktop, moderated think-aloud
- **Dữ liệu:** `sessions/P<n>/notes.md` + `screenshots/`, `sus-responses.csv`, `sus.xlsx`

## 1. Kết quả theo chặng (effectiveness)

| Code | Register | Nhận ra lockout → tới "Quên mật khẩu?" | Reset password | Update Profile | Can thiệp | SUS |
|---|---|---|---|---|---|---|
| P1 | No (blocker) | With help (sau câu trung lập) | No (blocker) | With help, lưu SĐT sai (`901000000`) | 5 | 35.0 |
| P2 | No (blocker) | With help | No (blocker) | N/A (dependent) | 5 | 40.0 |
| P3 | No (blocker) | With help | No (blocker) | N/A (dependent) | 5 | 27.5 |
| P4 | No (tự bỏ) | Không chạy | Không chạy | Không chạy | 0 | 25.0 |
| P5 | No (blocker) | With help | No: tự đăng nhập ở lần reset thứ 3, sau đó mật khẩu mới vẫn bị từ chối | No (blocker) | 5 | 32.5 |
| P6 | No (blocker) | **Yes** (≈ 01:24, tự thấy link) | No (blocker) | N/A (dependent) | 4 | 42.5 |
| P7 | No (blocker) | With help | No (blocker) | No (blocker, moderator nhập hộ mật khẩu để vào) | 8 | 30.0 |

**Task completed toàn flow: 0/7.**

| Objective | Ngưỡng | Kết quả | Đạt? |
|---|---|---|---|
| O1 — Tự đăng ký | ≥ 5/7 | **0/7** (cả 7 bị từ chối mật khẩu 7–12 lần) | ❌ |
| O2 — Tự tìm tới "Quên mật khẩu?" trong 2 phút | ≥ 5/7 | **1/6** (P6). Không ai hiểu là bị khoá; P5 chỉ đoán | ❌ |
| O3 — Reset median ≤ 3 phút, ≤ 1 lỗi | — | **0/6** reset thành công; median thời gian chặng ≈ 6:02 (P1 3:15 … P6 ≥ 9:44) | ❌ |
| O4 — Lưu được SĐT + địa chỉ | ≥ 6/7 | **0/3** người tới được Profile lưu đúng; 4 người không tới được | ❌ |
| O5 — SUS mean ≥ 68 | 68 | **33.2** | ❌ |

Tổng 32 lần can thiệp (median 5/người). Register là blocker đầu chuỗi: mọi chặng sau phải chạy bằng tài khoản dự phòng.

## 2. SUS

| | Giá trị |
|---|---|
| n | 7 |
| Mean | **33.2** |
| Median | 32.5 |
| SD | 6.4 |
| Min / Max | 25.0 (P4) / 42.5 (P6) |
| So với benchmark 68 | thấp hơn 34.8 điểm |
| Bangor adjective | giữa *Awful* (20.3) và *Poor* (35.7), gần **Poor**; grade F |

Tính bằng 2 cách, ra cùng kết quả: `skills/usability-eval/scripts/sus.py usability/sus-responses.csv` và `usability/sus.xlsx` (công thức, tự tính lại được). Pilot = 20.0, không tính.

Điểm trung bình từng câu (thang 1–5):

| Câu | Mean | Đọc nhanh |
|---|---:|---|
| Q6 Quá nhiều điểm không nhất quán | **4.43** | tệ nhất (câu chẵn, cao = tệ) |
| Q8 Rườm rà | 4.14 | |
| Q10 Phải học nhiều thứ | 4.00 | |
| Q4 Cần người kỹ thuật hỗ trợ | 3.71 | khớp với 32 lần can thiệp |
| Q2 Phức tạp không cần thiết | 3.29 | |
| Q1 Muốn dùng thường xuyên | 3.00 | |
| Q9 Tự tin khi dùng | 2.71 | |
| Q3 Dễ dùng | 2.57 | |
| Q5 Chức năng tích hợp tốt | 2.29 | thấp nhất (câu lẻ, thấp = tệ) |
| Q7 Học nhanh | 2.29 | |

## 3. Affinity grouping

| # | Theme | Mô tả | Participants | Count | Quotes (nguyên văn) | Loại |
|---|---|---|---|---|---|---|
| T1 | Mật khẩu hợp lệ vẫn bị chê "quá yếu" | Mật khẩu đủ hoa/thường/số/ký tự đặc biệt bị từ chối 7–12 lần, thông báo y hệt mỗi lần, không nói thiếu gì. Không ai đọc dòng hint xám nhỏ | P1–P7 | 7/7 | P3: "Thì tôi đọc rồi, nó đòi ký tự đặc biệt, tôi cho rồi còn gì." · P4: "Sao nó không chịu cho qua vậy? Tôi đổi lung tung rồi." · P6: "Vẫn vậy. Mình chịu rồi, không biết nó muốn gì nữa. Nhờ anh/chị giúp." | **Systemic** (validator #15 + thông báo không cụ thể + hint contrast #8) |
| T2 | "Đặt lại mật khẩu" không phản hồi | Bấm xong trang đứng im, không thông báo thành công/lỗi, không chuyển trang. Participant bấm lại nhiều lần rồi phải thử đăng nhập để đoán | P1, P2, P3, P5, P6, P7 | 6/6 | P3: "Bấm mà màn hình trơ ra, đổi chưa ta?" · P7: "Có chữ gì để đọc đâu, chỉ có cái mã OTP." · P2: "Thiếu cái thông báo thành công." | **Systemic** (feedback; P1 thấy popup alert, 5 người còn lại không thấy gì, xem mục 5) |
| T3 | Không biết mình bị khoá | Thông báo login sai và khi đã bị khoá giống hệt nhau. Participant nghĩ mình gõ sai/ghi sổ sai, gõ lại cùng mật khẩu nhiều lần | P1, P2, P3, P5, P6, P7 | 6/6 | P1: "Mình tưởng mình ghi sổ nhầm. Nó chỉ báo 'đăng nhập thất bại, kiểm tra lại' nên mình nghĩ lỗi ở mình." · P3: "Nó chỉ bảo kiểm tra lại, biết kiểm tra gì đâu." | **Systemic** (#36) |
| T4 | Mật khẩu mới vẫn không đăng nhập được | Sau khi "đặt lại", đăng nhập bằng mật khẩu mới vẫn thất bại; làm lại reset 2–4 vòng. Hệ quả của T1 (mật khẩu mới cũng bị validator từ chối) + T2 (không báo) + tài khoản vẫn đang bị khoá | P2, P3, P5, P6, P7 | 5/6 | P6: "Vẫn báo thất bại. Mình đổi mật khẩu 2 lần rồi mà… không hiểu." · P5: "Trời, mật khẩu vừa đặt cũng bị từ chối." | **Systemic** (chuỗi T1 + T2 + T3) |
| T5 | Link "Quên mật khẩu?" khó thấy | Link xanh nhỏ bên phải ô mật khẩu; 5/6 người chỉ thấy sau câu trung lập của moderator | P1, P2, P3, P5, P7 | 5/6 | P5: "À có chữ Quên mật khẩu nhỏ xíu bên phải, chắc phải bấm cái này." · P7: "À có chữ Quên mật khẩu bé bé màu xanh nè, mình quên thật mà." | **Systemic** (design, chưa có issue) |
| T6 | Profile không lưu được SĐT/địa chỉ | P1: `0901000000` bị báo không hợp lệ, chỉ lưu được khi bỏ số 0. P5, P7: bấm "Cập nhật" không báo gì, tải lại thì trống | P1, P5, P7 | 3/3 người tới được | P1: "Bỏ số 0 thì nó nhận, nhưng số này đâu còn đúng là số của mình nữa." · P7: "Mất sạch hết rồi! Mình nhập hai lần mà." | **Systemic** (#23 + thiếu feedback; P5/P7 cần kiểm lại, xem mục 5) |
| T7 | Trang đăng nhập ghi "Đăng Ký", "Username", "Sign In" | Participant ngập ngừng, đoán Username là email; không ai bị chặn | P1, P2, P3, P5, P6, P7 | 6/6 | P1: "Sao trang đăng nhập lại ghi Đăng Ký, mà ghi Username với Sign In nữa, lộn xộn." | Isolated bug (#1, #2) |
| T8 | Không tin tưởng để lưu thông tin thật | Probe 8: cả 7 người không dám lưu SĐT/địa chỉ thật. Lý do: lỗi liên tục, mật khẩu hiện chữ rõ (#3), OTP hiện trên trang, dữ liệu mất | P1–P7 | 7/7 | P2: "…rồi mã hiện lộ thế kia thì mình chưa dám để số điện thoại với địa chỉ thật." · P5: "…mật khẩu thì hiện chữ rõ ở ô đăng nhập, mình không dám để số điện thoại thật." | **Systemic** (hệ quả của T1–T6 + #3) |
| T9 | OTP hiện thẳng trên trang | Tiện nhưng làm giảm cảm giác an toàn | P1, P2, P3, P5, P6, P7 | 6/6 | P3: "Mã nằm ngay đó thì có cần mã làm gì, nhìn như trang làm chơi." · P5: "Ai biết email mình cũng lấy được mã ngay trên trang, vậy đổi mật khẩu của mình được luôn à?" | Design (chế độ demo của SUT, chưa có issue) |
| T10 | Bấm submit không có dấu hiệu đang xử lý | ~2 giây đầu form không đổi, participant tưởng chưa bấm, bấm lại | P1, P4, P7 | 3/7 | P1: "Bấm rồi mà chẳng thấy gì, hay là chưa ăn?" · P4: "Bấm mà không thấy phản hồi. Chắc tôi chưa bấm trúng, bấm lại." | Isolated bug (#40) |
| T11 | "← Quay lại" ở bước 2 về bước nhập email, không về đăng nhập | | P3, P5 | 2/6 | P3: "Quay lại mà sao ra cái ô email nữa, mình muốn về đăng nhập mà." | Isolated bug (mới) |
| T12 | Tooltip tiếng Anh "Please fill out this field." | Validation mặc định của trình duyệt | P3 | 1/7 | P3: "Ơ nó nói tiếng Anh, thôi gõ lại email." | Isolated bug (mới) |

## 4. Severity (Nielsen 0–4)

| Theme | Frequency | Impact | Persistence | Severity | Justification | Recommendation |
|---|---|---|---|---|---|---|
| T1 Mật khẩu hợp lệ bị chê | 7/7 | Chặn task (7/7 blocker) | Lặp lại mỗi lần thử, không tự vượt được | **4** | Blocker đầu chuỗi, gây 7 lần can thiệp và kéo SUS xuống | Sửa validator đúng rule đang hiển thị (#15); thông báo nêu đúng điều kiện chưa đạt; checklist rule cập nhật theo lúc gõ; hint đủ contrast (#8) |
| T2 Reset không phản hồi | 6/6 | Chặn task | Lặp lại 2–4 vòng reset | **4** | Không ai biết reset thành công hay thất bại, dẫn thẳng tới T4 | Thông báo inline thành công/lỗi; thành công thì chuyển về đăng nhập; hiện rule mật khẩu ở bước 2 (#25) |
| T4 Mật khẩu mới không dùng được | 5/6 | Chặn task | Lặp lại | **4** | Hệ quả T1 + T2 + T3, nhưng người dùng thấy là một vấn đề riêng: "đổi rồi vẫn không vào" | Reset thành công phải mở khoá tài khoản; sửa T1, T2 |
| T6 Profile không lưu được | 3/3 người tới được | Chặn task (P5, P7) / lưu sai dữ liệu (P1) | Lặp lại 3–5 lần | **4** | Mục tiêu cuối của flow không đạt; P1 bị ép lưu số điện thoại sai | Chấp nhận SĐT bắt đầu bằng 0 (#23); thông báo khi lưu; kiểm lại vì sao P5/P7 mất dữ liệu |
| T3 Không biết bị khoá | 6/6 | Làm chậm nhiều (median ~1:30), cần can thiệp | Lặp lại mỗi lần sai | **3** | Không chặn hẳn (cuối cùng vẫn tới Quên mật khẩu) nhưng sai hướng, gõ lại mật khẩu cũ | Thông báo riêng khi bị khoá + thời gian chờ + link Quên mật khẩu ngay trong thông báo (#36) |
| T5 Link Quên mật khẩu khó thấy | 5/6 | Cần can thiệp | Lặp lại | **3** | Chỉ 1/6 tự thấy trong 2 phút (O2 fail) | Link to hơn, nằm cạnh/ trong thông báo lỗi sau 2 lần sai |
| T8 Mất niềm tin | 7/7 | Không chặn task, nhưng người dùng nói sẽ bỏ trang | Toàn phiên | **3** | Ảnh hưởng trực tiếp tới việc mua hàng; P4, P6, P7 nói "mua chỗ khác/đóng lại" | Sửa T1–T6, che mật khẩu ở login (#3) |
| T7 Label trang login sai | 6/6 | Ngập ngừng, không chặn | Một lần mỗi người | **2** | Vượt được nhưng góp vào Q6 "không nhất quán" = 4.43 | Sửa tiêu đề, label tiếng Việt (#1, #2) |
| T9 OTP hiện trên trang | 6/6 | Không chặn, giảm trust | — | **2** | Là hành vi demo, nhưng 6/6 người tự nêu ra | Ghi rõ "chế độ demo" hoặc gửi qua email (Mailpit) |
| T10 Không có trạng thái loading | 3/7 | Bấm lặp | Lần đầu | **2** | Gây double submit, thêm nhầm lẫn ở T1 | Disable nút + spinner (#40) |
| T11 "Quay lại" sai đích | 2/6 | Lạc hướng nhẹ | Một lần | **1** | | "Quay lại" bước 2 → bước 1, thêm link "Về đăng nhập" (#32) |
| T12 Tooltip tiếng Anh | 1/7 | Không đáng kể | Một lần | **1** | | Dùng thông báo validation tiếng Việt |

## 5. Cần sinh viên kiểm lại trước khi kết luận

| Quan sát | Session | Vì sao cần kiểm |
|---|---|---|
| Reset với mật khẩu yếu: P1 thấy popup alert "Mật khẩu quá yếu", P2/P3/P5/P6/P7 không thấy gì | P1 vs còn lại | Có thể popup bị đóng nhanh, bị chặn, hoặc hành vi khác nhau. Xem lại recording |
| P5, P7: bấm "Cập nhật" không báo gì, tải lại thì trống. P1 lại có popup lỗi SĐT | P5, P7 | Có thể popup lỗi #23 bị bỏ lỡ; P7 lưu riêng địa chỉ cũng mất. Xem recording rồi mới đăng issue mới |
| P5: lần reset thứ 3 tự đăng nhập, lần thứ 4 thì không; Profile hiện `backup5b.hw03@test.local` | P5 | Có thể do dữ liệu/phiên cũ còn sót |
| P7: header đã hiện "Chào, Đức Huy" khi chưa đăng nhập | P7 | Có thể localStorage từ buổi trước chưa xoá (lỗi chuẩn bị session, không phải bug) |

## 6. Hạn chế của đợt test

- **Card đã dùng khác `scenario.md`**: pilot đề xuất bỏ "tên của bạn", "cập nhật", "mọi cách", nhưng file chưa được sửa. Ghi rõ card thực tế đã dùng cho P1–P7.
- **Lệch intervention rule**:
  - P4 kẹt 5:24 nhưng không có câu trung lập.
  - P1 và P7: moderator đưa hoặc nhập hộ mật khẩu gốc để đi tiếp. Việc này không có trong rule, P7 đã tự ghi nhận.
- **Chuỗi phụ thuộc**: vì Register bị chặn 7/7, các chặng sau chạy bằng tài khoản dự phòng, nên O2–O4 đo trên ít người hơn (6, 6, 3).
- **Ngưỡng theo số lần**: rule "> 3 phút" trên thực tế được áp dụng như "> 3 lần cùng cách" (theo đề xuất của pilot). Cần ghi điều này vào `plan.md`.
- Chỉ có 1 device (Chrome desktop). Participant không phải người dùng thật của EShop.

## 7. Đề xuất issue (chưa đăng, chờ duyệt)

Label: `type: usability` hoặc `usability`, `severity`, `priority`, `status: new`, `module`. Mỗi issue đính screenshot từ session.

| # | Title | Severity | Liên quan | Screenshot gợi ý |
|---|---|---|---|---|
| U1 | [USABILITY][register] 7/7 participants could not register: valid passwords rejected with the same unhelpful message | blocker | #15, #8 | `P6/screenshots/10-register-blocked.jpg` |
| U2 | [USABILITY][forgot-password] Reset gives no feedback; 6/6 participants could not tell whether the password changed | blocker | #25, #21 | `P7/screenshots/19-reset-no-response-4.jpg` |
| U3 | [USABILITY][forgot-password] New password still fails to log in after reset (account stays locked) | critical | #36 | `P6/screenshots/23-login-newpass2-fail-after-wait.jpg` |
| U4 | [USABILITY][profile] Participants could not save phone/address (0-prefix rejected, data empty after reload) | critical | #23 | `P7/screenshots/28-profile-empty-after-reopen.jpg` (đăng sau khi kiểm mục 5) |
| U5 | [USABILITY][login] Lockout is indistinguishable from a wrong password; 0/6 understood they were locked | major | #36 | `P1/screenshots/12-login-fail-4.jpg` |
| U6 | [USABILITY][login] "Quên mật khẩu?" link is hard to find; 5/6 needed a prompt | major | mới | `P5/screenshots/05-login-fail-4th-same-generic-message.jpg` |
| U7 | [USABILITY][forgot-password] OTP shown on the page lowers trust (6/6 mentioned it) | minor | mới | `P3/screenshots/08-forgot-otp-on-screen.jpg` |
| U8 | [BUG][forgot-password] "← Quay lại" on step 2 returns to the email step instead of Login | trivial | #32 | `P3/screenshots/10-quay-lai-goes-to-step1.jpg` |
| U9 | [BUG][login] Browser validation tooltip shown in English | trivial | mới | `P3/screenshots/12-english-validation-tooltip.jpg` |

T7 và T10 đã có issue (#1, #2, #40). Chỉ cần comment link session vào các issue đó, không tạo issue mới.
