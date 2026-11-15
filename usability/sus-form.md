# SUS — nội dung Google Form

Tạo ở https://forms.google.com. Mỗi câu SUS là *Linear scale* 1–5 (1 = Hoàn toàn không đồng ý, 5 = Hoàn toàn đồng ý), bắt buộc trả lời.

**Câu 0 (Short answer):** Mã người tham gia (P1…P7). Không hỏi họ tên.

| # | Câu hỏi (bản tiếng Việt) | Bản gốc (Brooke, 1996) |
|---|---|---|
| 1 | Tôi nghĩ là tôi sẽ muốn dùng hệ thống này thường xuyên. | I think that I would like to use this system frequently. |
| 2 | Tôi thấy hệ thống này phức tạp một cách không cần thiết. | I found the system unnecessarily complex. |
| 3 | Tôi thấy hệ thống này dễ sử dụng. | I thought the system was easy to use. |
| 4 | Tôi nghĩ là tôi sẽ cần người có chuyên môn hỗ trợ mới dùng được hệ thống này. | I think that I would need the support of a technical person to be able to use this system. |
| 5 | Tôi thấy các chức năng của hệ thống được kết hợp tốt với nhau. | I found the various functions in this system were well integrated. |
| 6 | Tôi thấy hệ thống này có quá nhiều điểm không nhất quán. | I thought there was too much inconsistency in this system. |
| 7 | Tôi nghĩ hầu hết mọi người sẽ học cách dùng hệ thống này rất nhanh. | I would imagine that most people would learn to use this system very quickly. |
| 8 | Tôi thấy hệ thống này rất rườm rà, khó thao tác. | I found the system very cumbersome to use. |
| 9 | Tôi cảm thấy rất tự tin khi dùng hệ thống này. | I felt very confident using the system. |
| 10 | Tôi cần học nhiều thứ trước khi có thể bắt đầu dùng hệ thống này. | I needed to learn a lot of things before I could get going with this system. |

**Câu cuối (Multiple choice):** "Tôi đồng ý cho quay màn hình và ghi âm buổi test, chỉ dùng cho bài tập môn học." — Đồng ý / Không đồng ý.

## Cách tính

- Câu lẻ (1, 3, 5, 7, 9): điểm − 1. Câu chẵn (2, 4, 6, 8, 10): 5 − điểm.
- SUS = tổng × 2.5 (0–100). Benchmark trung bình: 68.
- Formula Calc (Q1…Q10 ở cột B…K): `=((B2-1)+(5-C2)+(D2-1)+(5-E2)+(F2-1)+(5-G2)+(H2-1)+(5-I2)+(J2-1)+(5-K2))*2.5`
