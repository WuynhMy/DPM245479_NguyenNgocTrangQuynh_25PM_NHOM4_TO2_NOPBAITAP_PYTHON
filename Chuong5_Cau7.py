'''Toi uu chuoi danh tu'''
'''Viết chương trình tối ưu Chuỗi danh từ
Một Chuỗi được gọi là tối ưu khi: Không chứa các khoảng trắng dư thừa, các từ cách
nhau bởi một khoảng trắng, Ký tự đầu tiên của các từ Viết Hoa
Ví dụ:
Input “ TRần duY thAnH ”
Output “Trần Duy Thanh”'''
def toi_uu_chuoi_danh_tu(s):
    # Xóa khoảng trắng dư thừa ở đầu và cuối, tách các từ bằng split()
    tu = s.strip().split()
    # Viết hoa chữ cái đầu, các chữ còn lại viết thường
    tu_da_xu_ly = [word.capitalize() for word in tu]
    # Ghép lại bằng một khoảng trắng
    ket_qua = ' '.join(tu_da_xu_ly)
    return ket_qua

# --- Ví dụ sử dụng ---
chuoi_nhap = "  TRần   duY   thAnH   "
chuoi_toi_uu = toi_uu_chuoi_danh_tu(chuoi_nhap)
print(chuoi_toi_uu)
