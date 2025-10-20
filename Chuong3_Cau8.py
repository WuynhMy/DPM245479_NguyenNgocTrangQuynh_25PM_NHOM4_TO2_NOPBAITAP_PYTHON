'''Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo
đúng phép toán đã nhập.'''
print("Nhap hai so a va b vao: ")
a=float(input("Nhap a: "))
b=float(input("Nhap b: "))
op = input("Nhập phép toán (+, -, *, /): ")
if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    if b == 0:
        result = "Lỗi: không thể chia cho 0"
    else:
        result = a / b
else:
    result = "Phép toán không hợp lệ"

print("Kết quả:", result)