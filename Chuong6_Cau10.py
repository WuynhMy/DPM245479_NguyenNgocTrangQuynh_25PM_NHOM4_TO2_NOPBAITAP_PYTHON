'''Xử lý Ma Trận
Yêu cầu:
Nhập 2 matrix A, B.
Cộng 2 matrix
Viết hàm tính matrix hoán vị➔áp dụng để tìm cho A, B'''
def nhap_ma_tran(name):
    print(f"Nhập ma trận {name}:")
    m = int(input("Số hàng: "))
    n = int(input("Số cột: "))
    matrix = []
    for i in range(m):
        row = list(map(float, input(f"Nhập hàng {i+1} (các phần tử cách nhau bởi dấu cách): ").split()))
        while len(row) != n:
            print(f"⚠️ Lỗi: cần nhập đúng {n} phần tử.")
            row = list(map(float, input(f"Nhập lại hàng {i+1}: ").split()))
        matrix.append(row)
    return matrix

def cong_ma_tran(A, B):
    m = len(A)
    n = len(A[0])
    # Kiểm tra kích thước
    if m != len(B) or n != len(B[0]):
        raise ValueError("Không thể cộng hai ma trận khác kích thước!")
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]

def hoan_vi_ma_tran(M):
    # Trả về ma trận chuyển vị
    return [list(row) for row in zip(*M)]

def in_ma_tran(M, name="Ma trận"):
    print(f"{name}:")
    for row in M:
        print(row)
    print()  # dòng trống

# --- Chương trình chính ---
A = nhap_ma_tran("A")
B = nhap_ma_tran("B")

# In ma trận ban đầu
in_ma_tran(A, "Ma trận A")
in_ma_tran(B, "Ma trận B")

# Cộng 2 ma trận
try:
    C = cong_ma_tran(A, B)
    in_ma_tran(C, "Ma trận A + B")
except ValueError as e:
    print("❌ Lỗi:", e)

# Tính ma trận hoán vị
A_T = hoan_vi_ma_tran(A)
B_T = hoan_vi_ma_tran(B)
in_ma_tran(A_T, "Ma trận chuyển vị A")
in_ma_tran(B_T, "Ma trận chuyển vị B")
