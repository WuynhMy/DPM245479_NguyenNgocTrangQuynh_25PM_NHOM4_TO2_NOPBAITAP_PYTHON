'''Viết chương trình tính logax'''
import math

# Nhập giá trị a và x
a = float(input("Nhập cơ số a: "))
x = float(input("Nhập số x: "))

# Kiểm tra điều kiện hợp lệ
if a > 0 and a != 1 and x > 0:
    logax = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {logax}")
else:
    print("Giá trị không hợp lệ! Cần có: a > 0, a ≠ 1 và x > 0.")
