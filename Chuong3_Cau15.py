'''Giải thích cách chạy các dòng lệnh rang'''
'''range (bắt đầu , kết thúc,step )
(a) range(5) → từ 0 → 4 (mặc định start = 0, step = +1)
→ Kết quả: 0, 1, 2, 3, 4

(b) range(5, 10) → từ 5 → 9
→ 5, 6, 7, 8, 9

(c) range(5, 20, 3) → từ 5, mỗi lần +3, dừng trước 20
→ 5, 8, 11, 14, 17

(d) range(20, 5, -1) → từ 20 ↓ mỗi lần -1, dừng trước 5
→ 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6

(e) range(20, 5, -3) → từ 20 ↓ mỗi lần -3, dừng trước 5
→ 20, 17, 14, 11, 8

(f) range(10, 5) → đi lên (step mặc định = +1) nhưng 10 > 5 → không chạy
→ Kết quả: rỗng

(g) range(0) → giống range(0, 0) → không có gì để in
→ Kết quả: rỗng

(h) range(10, 101, 10) → từ 10 đến 100 (vì 101 không lấy)
→ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100

(i) range(10, -1, -1) → từ 10 ↓ mỗi lần -1 tới 0
→ 10, 9, 8, ..., 1, 0

(j) range(-3, 4) → từ -3 → 3 (mỗi lần +1)
→ -3, -2, -1, 0, 1, 2, 3

(k) range(0, 10, 1) → từ 0 → 9
→ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9'''