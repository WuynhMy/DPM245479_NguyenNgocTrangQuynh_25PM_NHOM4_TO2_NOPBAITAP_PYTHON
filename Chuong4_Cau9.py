'''Viết chương trình tính căn bậc 2 lồng nhau'''
import math

# Nhập n
n = int(input("Nhập n: "))

# Tính S(n)
s = 0
for i in range(n):
    s = math.sqrt(2 + s)

# Xuất kết quả
print(f"S({n}) = {s}")
