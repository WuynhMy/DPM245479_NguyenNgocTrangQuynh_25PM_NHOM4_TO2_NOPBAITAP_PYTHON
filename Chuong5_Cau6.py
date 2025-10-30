'''Trích lọc số âm trong chuỗi'''
import re

def NegativeNumberInStrings(s):
    # Tìm tất cả số âm, có thể có nhiều chữ số
    # (?<!-) đảm bảo trước dấu '-' không phải là một dấu '-'
    ket_qua = re.findall(r'(?<!-)-\d+', s)
    return ket_qua


# --- Kiểm tra thử ---
chuoi = "abc-5xyz-12k9l--p"
ds_so_am = NegativeNumberInStrings(chuoi)

print("Các số nguyên âm tìm thấy:", ds_so_am)

