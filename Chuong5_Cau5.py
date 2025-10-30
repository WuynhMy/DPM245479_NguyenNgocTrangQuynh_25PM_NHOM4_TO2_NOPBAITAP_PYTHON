'''Xử lý chuỗi với các hàm cơ bản'''# Nhập chuỗi từ người dùng
chuoi = input("Nhập vào một chuỗi bất kỳ: ")

# Khởi tạo các biến đếm
dem_hoa = dem_thuong = dem_so = dem_dac_biet = dem_khoang_trang = 0
dem_nguyen_am = dem_phu_am = 0

nguyen_am = "aeiouAEIOU"

for ch in chuoi:
    if ch.isupper():
        dem_hoa += 1
    elif ch.islower():
        dem_thuong += 1

    if ch.isdigit():
        dem_so += 1
    elif not ch.isalnum() and not ch.isspace():
        dem_dac_biet += 1
    elif ch.isspace():
        dem_khoang_trang += 1

    # Kiểm tra nguyên âm / phụ âm (chỉ tính chữ cái)
    if ch.isalpha():
        if ch in nguyen_am:
            dem_nguyen_am += 1
        else:
            dem_phu_am += 1

# --- Xuất kết quả ---
print("\nKẾT QUẢ PHÂN TÍCH CHUỖI:")
print(f"Số chữ IN HOA: {dem_hoa}")
print(f"Số chữ in thường: {dem_thuong}")
print(f"Số chữ là chữ số: {dem_so}")
print(f"Số ký tự đặc biệt: {dem_dac_biet}")
print(f"Số ký tự khoảng trắng: {dem_khoang_trang}")
print(f"Số nguyên âm: {dem_nguyen_am}")
print(f"Số phụ âm: {dem_phu_am}")
