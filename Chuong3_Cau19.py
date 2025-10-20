'''Tính giá trị biểu thức S'''
import math

x = float(input("Nhập x: "))
n = int(input("Nhập n (n >= 0): "))

if n < 0:
    print("n phải >= 0")
else:
    S = 0.0
    for k in range(n + 1):
        num = x ** (2 * k + 1)
        den = math.factorial(2 * k + 1)
        S += num / den
    print("S =", S)

