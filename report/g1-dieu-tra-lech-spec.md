# G1 – Điều tra điểm lệch spec (FR-01 → FR-04)

- Ngày: 2026-11-03, ~16:45–16:50 UTC
- Môi trường: Ubuntu, Chrome (browser pane), web `http://localhost:5173`, backend `:3000`, DB seed mặc định
- Người thực hiện: Claude Code (AI) điều khiển trình duyệt, đọc trạng thái DB (read-only) để đo bộ đếm.
  → **Phải tự chạy lại và chụp ảnh trước khi đưa vào report / GitHub Issues**, và ghi lần điều tra này vào AI Audit.
- Tài khoản: `test@eshop.com` / `Test1234!` (seed)

## Kết quả

| # | Spec | Thực tế (đã thấy trên UI) | Kết luận |
|---|---|---|---|
| D1 | FR-02: sai 1 lần → bộ đếm +1 | Sai 1 lần → `login_attempts = 2` | ❌ Lệch: +2 mỗi lần |
| D2 | FR-02: khóa khi sai ≥ 3 lần | Sai lần **2** đã bị khóa (đếm = 4) | ❌ Lệch: khóa sau 2 lần |
| D3 | FR-02: khóa 30 giây | `locked_until` = lúc sai + **180 giây** | ❌ Lệch: khóa 3 phút |
| D4 | FR-02: thông báo lỗi phù hợp | Khi bị khóa, nhập **đúng** mật khẩu vẫn chỉ thấy "Đăng nhập thất bại. Vui lòng kiểm tra lại." → người dùng không biết mình bị khóa, không biết chờ bao lâu | ❌ Usability: thông báo không phân biệt "sai" và "bị khóa" |
| D5 | (hợp lý) hết khóa thì bắt đầu đếm lại | Hết 3 phút, sai **1 lần** → khóa tiếp 3 phút (đếm 4 → 6). Bộ đếm chỉ reset khi đăng nhập đúng | ❌ Lệch / logic |
| D6 | (hợp lý) reset mật khẩu thành công thì mở khóa | Reset thành công nhưng đăng nhập bằng mật khẩu mới vẫn thất bại tới khi hết khóa | ❌ Logic, chặn flow usability |
| D7 | FR-03: OTP 6 chữ số | OTP 4 chữ số, nhãn "Mã OTP (4 số)" | ❌ Lệch |
| D8 | FR-03: step indicator "Bước 1/2" | Không có ở cả 2 bước | ❌ Lệch |
| D9 | FR-03: có ô xác nhận mật khẩu mới | Bước 2 chỉ có OTP + Mật khẩu mới | ❌ Lệch |
| D10 | FR-01/03: mật khẩu cần ký tự đặc biệt `@$!%*?&` | Regex thực tế **bắt buộc dấu cách** và **cấm ký tự đặc biệt**. `NewPass1!` / `Vinh1234!` bị từ chối, `NewPass1 x` được chấp nhận. Thông báo lỗi vẫn nói "phải có KÝ TỰ ĐẶC BIỆT" | ❌ Lệch, **blocker** cho người dùng |
| D11 | FR-01: có ô Xác nhận mật khẩu | Form Đăng ký chỉ có Họ tên, Email, Mật khẩu | ❌ Lệch |
| D12 | FR-02: ô email `type="email"` | Login: ô email `type="text"`, nhãn "Username" | ❌ Lệch |

## Lỗi giao diện thấy thêm (Login)
- Tiêu đề trang Login ghi **"Đăng Ký"** thay vì "Đăng nhập".
- Ô mật khẩu Login là `type="text"` → mật khẩu hiện rõ.
- Trộn ngôn ngữ: nút "Sign In", nhãn "Username" giữa giao diện tiếng Việt.
- Forgot password: thông báo kết quả dùng `alert()` của trình duyệt; nút "← Quay lại" cùng màu xanh lá với nút chính.
- Register: dòng gợi ý luật mật khẩu chữ rất nhỏ, xám nhạt (cần đo contrast).

## Lệch tài liệu
- `setup_guide.md` ghi admin là `admin123`, nhưng seed thực tế là `Admin123!`.
- **Mỗi lần khởi động lại backend (`node server.js`) thì DB bị xóa và seed lại** (`database.js` chạy `DROP TABLE`). Tài khoản người tham gia tạo sẽ mất nếu restart server.

## Ảnh hưởng tới Task 2 (flow G1)
1. **Bước Đăng ký gần như chắc chắn kẹt (D10):** người dùng làm theo đúng hướng dẫn trên màn hình (thêm ký tự đặc biệt) thì luôn bị từ chối. Cần chốt **quy tắc can thiệp** trước, ví dụ kẹt > 3 phút thì người điều phối gợi ý, và ghi lại là *blocker*. Pilot sẽ xác nhận.
2. **Bị khóa nhanh hơn (D2) và lâu hơn (D3, D5, D6):** sau khi reset vẫn phải chờ tới 3 phút → thời gian mỗi buổi tăng; người tham gia dễ nghĩ reset hỏng. Đây là phát hiện usability đáng giá — ghi nhận, đừng "sửa" giùm người tham gia.
3. **Không restart backend giữa các buổi** (DB bị xóa), hoặc chủ động restart để mỗi buổi bắt đầu sạch.

## Việc cần tự làm
- [ ] Chạy lại từng mục D1–D12, chụp ảnh (có overlay MSSV/tên/email), ghi giờ.
- [ ] Đưa vào checklist (cột Req = FR tương ứng) và log GitHub Issues.
- [ ] Ghi lần điều tra bằng AI này vào `ai-audit.md`.
