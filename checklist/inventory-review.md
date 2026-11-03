# Review — P01 UI inventory (AI log #1, OpenCode — DeepSeek V4.1 Flash Free)

- Đối chiếu với: 8 screenshot trong `screenshots/input/`, `spec-FR01-04.md`, README đầy đủ của SUT, source code `frontend-web/src/pages/*.jsx`.
- **Overall verdict: INCOMPLETE.** Dùng được sau khi sửa. Phần "observed" mô tả đúng hết. Lỗi nằm ở việc lấy thông tin ngoài phạm vi prompt cho phép, trích sai requirement, và trộn "inventory" với "expected element".

## 1. Đúng (VALID): đã đối chiếu với screenshot

| Dòng trong inventory                                                                                                                                          | Kiểm chứng                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Login heading "Đăng Ký", label "Username", button "Sign In"                                                                                                 | Đúng (`login-*.png`)                             |
| Login password hiện plain text                                                                                                                                | Đúng: `login-locked.png` thấy rõ `Test1234!` |
| Login error banner nằm **dưới** button Sign In; locked state y hệt wrong-password state                                                              | Đúng                                               |
| Register: banner lỗi ở trên các field, không có Confirm Password, hint password chữ nhỏ và mờ, button đỏ                                           | Đúng (`register-error.png`)                      |
| Forgot step 2: OTP 4 số ("4452", label "Mã OTP (4 số)"), không có step indicator, 2 button cùng màu xanh lá                                            | Đúng (`forgot-step2.png`)                        |
| Profile: email bị disable, nền xám; phone và address có placeholder; empty state chỉ có text; header "Chào, Test User" màu vàng + "Thoát" màu đỏ | Đúng (`profile.png`)                             |

## 2. Cần sửa

| #  | Vấn đề                                                                                                                                                        | Verdict           | Lý do                                                                                                                           | Sửa thành                                                                                                     |
| -- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| R1 | Trích **FR-22, FR-23, SEC-07** dù chúng không có trong file spec được đính kèm. OpenCode đã tự đọc README đầy đủ trong repo            | INCOMPLETE        | Vi phạm rule của prompt "chỉ từ screenshot hoặc spec". Tuy vậy các trích dẫn đều đúng và hữu ích                 | Giữ các dòng đó, ghi rõ nguồn "README §8–9". Lần sau đính kèm luôn FR-21..24 và SEC (xem mục 4) |
| R2 | "Lockout notice / remaining-time countdown … (FR-02)": cho rằng FR-02 yêu cầu countdown                                                                      | **INVALID** | FR-02 chỉ ghi "thông báo lỗi phù hợp; **không để lộ chi tiết nguyên nhân**". FR-02 không yêu cầu countdown | Xóa phần "required by FR-02". Chuyển ý countdown sang item Human (usability), không gắn Req               |
| R3 | "Login heading … expected 'Đăng nhập' (FR-02)"                                                                                                               | INCOMPLETE        | FR-02 không quy định heading. Heading thuộc FR-21 (1 `<h1>` mô tả trang)                                                 | Đổi Req thành FR-21                                                                                          |
| R4 | Liệt kê element **không tồn tại** và **không có trong spec**: show/hide password, submitting/loading state                                   | INVALID           | Prompt cấm đoán element. Đây là ý tưởng checklist, không phải inventory                                               | Xóa khỏi inventory, chuyển sang danh sách Human item ở bước 1.6                                          |
| R5 | Element thiếu so với spec (Confirm Password, step indicator, "Quay lại đăng nhập", `*`, cart badge, nav highlight) được trộn lẫn với element thật | INCOMPLETE        | Inventory nên tách "đang có" và "spec yêu cầu nhưng không có"                                                          | Gom các dòng này thành section riêng **"Expected by spec but absent"**                               |
| R6 | Profile orders table liệt kê tên cột (Mã ĐH, Ngày đặt…) với ghi chú "observed"                                                                       | INVALID           | Screenshot chỉ có empty state. Tên cột lấy từ source code                                                                  | Ghi "(assumed — from code)" hoặc xóa, vì Order History thuộc FR-11, ngoài G1                              |
| R7 | "Chào, Test User" và "Thoát" bị lặp ở cả Shared chrome lẫn Profile                                                                                       | INCOMPLETE        | Trùng dòng                                                                                                                     | Giữ ở Shared chrome (state: logged in), xóa ở Profile                                                       |
| R8 | Giữ chi tiết "OTP expiry / single-use indicator (SEC-07)"                                                                                                      | INCOMPLETE        | SEC-07 là yêu cầu backend (entropy, hết hạn). Không có element UI nào tương ứng                                       | Bỏ khỏi inventory. Nếu muốn, dùng làm item IA-04 "có báo OTP hết hạn không"                          |
| R9 | Trộn nhận xét kiểu defect ("text is wrong", "contrary to FR-03") vào cột States                                                                            | INCOMPLETE        | Prompt ghi "chỉ step 1, chưa viết checklist". Verdict thuộc bước sau                                                       | Chuyển các nhận xét này xuống section "Inventory notes" ở cuối file                                     |

## 3. AI bỏ sót (thêm vào)

| Thiếu                                                                                                    | Nguồn                 | Ghi chú                                                                      |
| --------------------------------------------------------------------------------------------------------- | ---------------------- | ----------------------------------------------------------------------------- |
| Heading của cả 4 trang là `<h2>`, **không có `<h1>`**                                      | FR-21, code / DevTools | Ảnh tĩnh không thấy được → lý do (b) giới hạn input                |
| Tab order: button "Sign In" có `tabIndex=1`                                                            | FR-21, code            | Focus sẽ nhảy vào Sign In trước tiên. Ảnh tĩnh không thấy → (b)    |
| Header "Chào, {name}" render HTML (`dangerouslySetInnerHTML`)                                          | SEC-04, code           | Element vẫn là link, nhưng state "name chứa HTML" rất quan trọng → (b) |
| Login: không có `type="email"`, không có `type="password"`                                        | FR-22                  | AI đã ghi "Input (text)" nhưng chưa nối với FR-22                       |
| Nhất quán ngôn ngữ ("Sign In", "Username" giữa UI tiếng Việt)                                      | FR-21                  | Chỉ nằm trong notes, chưa gắn requirement                                 |
| Nhất quán màu: "Đăng Ký" là button submit nhưng màu đỏ (FR-21: positive action = xanh dương) | FR-21                  | AI ghi "red" nhưng chưa nối với FR-21                                     |
| Forgot step 1 → step 2 dùng chung URL `/forgot-password`, reload là mất step 2                      | Quan sát thêm        | Item cho IA-03                                                                |

## 4. Bài học cho prompt sau (đưa vào AI Critique)

- File spec đính kèm thiếu **FR-21..FR-24 (GUI Requirements)** và **SEC**, trong khi 4 nhóm này khớp đúng với IA-01..IA-04. Đây là lỗi input của mình. Command trong hướng dẫn đã được sửa để tách thêm các mục đó.
- Agent có quyền đọc repo (OpenCode) sẽ tự đọc thêm file ngoài phần đính kèm. Muốn giới hạn nguồn thì phải nói rõ "không đọc file khác", hoặc chạy ở thư mục không có repo SUT.
- Screenshot tĩnh không cho thấy semantic HTML, tab order hay cách render. Những thứ này phải tự kiểm tra bằng DevTools.
