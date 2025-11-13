'''Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU'''
import random

# Nhập số lượng phần tử
N = int(input("Nhập số lượng phần tử N: "))

# Sinh list gồm N số ngẫu nhiên không trùng nhau trong khoảng 0–99
lst = random.sample(range(100), N)

print("Danh sách ngẫu nhiên không trùng:", lst)
