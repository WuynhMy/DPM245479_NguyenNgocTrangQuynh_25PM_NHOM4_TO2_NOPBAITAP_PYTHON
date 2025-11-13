'''Viết chương trình nhập vào một dãy n số thực M[0], M[1],..., M[n-1], sắp xếp
dãy số theo thứ tự giảm dần. Xuất ra dãy số sau khi sắp xếp.'''
# Nhập số phần tử của dãy
n = int(input("Nhập số phần tử của dãy n = "))

# Nhập dãy n số thực
M = []
for i in range(n):
    x = float(input(f"Nhập M[{i}] = "))
    M.append(x)

# Sắp xếp dãy theo thứ tự giảm dần
M.sort(reverse=True)

# Xuất kết quả
print("\n🔽 Dãy sau khi sắp xếp giảm dần:")
for i, x in enumerate(M):
    print(f"M[{i}] = {x}")
