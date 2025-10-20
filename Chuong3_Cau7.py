'''Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày
vừa nhập (ngày/tháng/năm).'''
# Nhập ngày / tháng / năm
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

# Hàm kiểm tra năm nhuận
def is_leap_year(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

# Số ngày trong mỗi tháng
days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]

day += 1  # tăng 1 ngày

# Kiểm tra nếu hết tháng
if day > days_in_month[month - 1]:
    day = 1
    month += 1

# Kiểm tra nếu hết năm
if month > 12:
    month = 1
    year += 1

print(f"Ngày kế tiếp là: {day:02d}/{month:02d}/{year}")
