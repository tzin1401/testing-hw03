# AGENT.md — Luật cho mọi AI agent làm việc trong repo này

Áp dụng cho mọi công cụ AI (Claude Code, Cursor, Copilot, Gemini CLI, ChatGPT…) khi làm việc trong thư mục này.

## Luật ghi AI log

**Khi nào ghi:** chỉ khi prompt của người dùng có cụm **"ghi vào log"** (không phân biệt hoa thường).
Không có cụm đó → **không** ghi gì vào log.

**Ghi vào đâu:** `report/ai-audit.md` (đáp ứng §9 của đề HW03).

**Cách ghi (làm sau khi đã trả lời xong prompt, trong cùng lượt):**

1. Lấy số thứ tự tiếp theo `<n>` = số mục `### <số>` lớn nhất trong file + 1 (file trống → 1).
2. Lấy thời gian **lúc nhận prompt**, định dạng `DD/MM/YYYY HH:MM` (giờ máy, ví dụ chạy `date '+%d/%m/%Y %H:%M'`).
3. Thêm 1 dòng vào bảng tóm tắt đầu file (thay dòng mẫu trong comment nếu bảng còn trống):
   `| <n> | <bước, ví dụ "P02 — Checklist IA-01"> | <tên công cụ + model> | <ngày giờ> | [#<n>](#<n>) |`
4. Thêm vào **cuối file** đúng khối sau:

   ````markdown
   ### <n>
   - **Công cụ AI:** <tên công cụ + model, ví dụ "Claude Code — Claude Opus 5.5">
   - **Ngày giờ:** <DD/MM/YYYY HH:MM>
   - **Bước:** <mã bước trong hướng dẫn nếu đoán được, không thì mô tả ngắn>

   **Prompt:**
   ```text
   <prompt nguyên văn của người dùng, kể cả cụm "ghi vào log">
   ```

   **AI output:**
   ```text
   <câu trả lời nguyên văn đã gửi cho người dùng>
   ```
   ````

5. Output dài hơn ~150 dòng → lưu nguyên văn vào `report/ai-outputs/<n>.md`, trong khối **AI output** chỉ ghi `Xem report/ai-outputs/<n>.md`.
6. Nếu AI đã sửa/tạo file (checklist, Excel, skill…) → thêm dòng `- **File đã tạo/sửa:** <danh sách đường dẫn>` dưới dòng **Bước**.
7. Cuối câu trả lời, báo một dòng: `📝 Đã ghi log #<n> vào report/ai-audit.md`.

**Không được:**
- Tóm tắt, dịch, hay "làm đẹp" prompt và output — phải nguyên văn.
- Sửa hoặc xóa mục log cũ.
- Ghi thông tin cá nhân của người tham gia usability (họ tên, SĐT, Zalo). Nếu prompt có, thay bằng mã `P1…P7` và ghi chú `(đã ẩn thông tin cá nhân)`.
- Tự commit file log, trừ khi người dùng yêu cầu.
