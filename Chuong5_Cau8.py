'''Tách lấy tên bài hát'''
'''Cho một chuỗi là đường dẫn của 1 file nhạc, ví dụ: d:\\music\muabui.mp3
Hãy viết 2 hàm để:
- Lấy ra muabui.mp3
- Lấy ra muabui
Lưu ý đường dẫn bài hát là bất kỳ. Nên khi truyền vào bài hát nào thì lấy chính xác theo
bài hát đó.'''
import os

# Hàm 1: Lấy ra tên file có phần mở rộng
def lay_ten_file(day_duong_dan):
    return os.path.basename(day_duong_dan)

# Hàm 2: Lấy ra tên file không có phần mở rộng
def lay_ten_khong_duoi(day_duong_dan):
    ten_day_duoi = os.path.basename(day_duong_dan)
    ten_khong_duoi, _ = os.path.splitext(ten_day_duoi)
    return ten_khong_duoi


# --- Ví dụ sử dụng ---
duong_dan = r"d:\music\muabui.mp3"

print("Tên file có đuôi:", lay_ten_file(duong_dan))        # ➜ muabui.mp3
print("Tên file không đuôi:", lay_ten_khong_duoi(duong_dan))  # ➜ muabui
