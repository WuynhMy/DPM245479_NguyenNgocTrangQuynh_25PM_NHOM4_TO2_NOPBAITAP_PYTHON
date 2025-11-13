'''Xử lý CSV File - Viết phần mềm Quản Lý Nhân Viên
Yêu cầu:
Viết hàm cho phép lưu tập tin dưới dạng CSV file, yêu cầu khởi tạo là 10 dòng, mỗi
dòng sẽ có 10 số ngẫu nhiên bất kỳ cách nhau bởi dấu “;”.
Tiếp theo viết hàm cho phép đọc tập tin ở mục trên, xuất ra tổng giá trị của các phần tử
trên mỗi dòng.
'''
import csv
import random

# ==============================
# HÀM GHI FILE CSV
# ==============================
def ghi_file_csv(filename="dulieu.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=';')
        for _ in range(10):  # 10 dòng
            dong = [random.randint(0, 100) for _ in range(10)]  # 10 số ngẫu nhiên
            writer.writerow(dong)
    print(f"✅ Đã tạo file CSV '{filename}' với 10 dòng dữ liệu ngẫu nhiên.")


# ==============================
# HÀM ĐỌC FILE VÀ TÍNH TỔNG
# ==============================
def doc_file_va_tinh_tong(filename="dulieu.csv"):
    print("\n=== KẾT QUẢ TÍNH TỔNG TỪ FILE CSV ===")
    try:
        with open(filename, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=';')
            for i, row in enumerate(reader, start=1):
                # chuyển từng phần tử thành số nguyên
                numbers = [int(x) for x in row if x.strip() != ""]
                tong = sum(numbers)
                print(f"Dòng {i}: {numbers}  ➜  Tổng = {tong}")
    except FileNotFoundError:
        print("❌ File chưa tồn tại. Hãy chạy hàm ghi_file_csv() trước.")


# ==============================
# CHƯƠNG TRÌNH CHÍNH (MAIN)
# ==============================
if __name__ == "__main__":
    ghi_file_csv()             # Tạo file CSV 10x10
    doc_file_va_tinh_tong()    # Đọc file và tính tổng từng dòng
