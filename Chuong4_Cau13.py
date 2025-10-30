'''Hàm kiểm tra số hoàn thiện, số thịnh vượng'''
def tong_uoc_so(n):
    """Hàm tính tổng các ước số của n (không kể chính n)."""
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong


def la_so_hoan_thien(n):
    """Kiểm tra số n có phải là số hoàn thiện không."""
    return tong_uoc_so(n) == n


def la_so_thinh_vuong(n):
    """Kiểm tra số n có phải là số thịnh vượng không."""
    return tong_uoc_so(n) > n


# --- Phần kiểm tra ---
n = int(input("Nhập số nguyên dương n: "))

if la_so_hoan_thien(n):
    print(f"{n} là số hoàn thiện.")
elif la_so_thinh_vuong(n):
    print(f"{n} là số thịnh vượng.")
else:
    print(f"{n} không phải là số hoàn thiện cũng không phải là số thịnh vượng.")
