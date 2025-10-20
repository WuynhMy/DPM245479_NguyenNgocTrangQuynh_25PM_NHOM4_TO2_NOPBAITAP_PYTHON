'''Vẽ các hình dưới đây'''
def draw_hollow_rectangle(h, w):
    if h <= 0 or w <= 0:
        print("Kích thước phải > 0.")
        return
    for i in range(h):
        if i == 0 or i == h - 1:
            print('*' * w)
        else:
            if w == 1:
                print('*')
            else:
                print('*' + ' ' * (w - 2) + '*')

def draw_right_triangle_inc(n):
    if n <= 0:
        print("Chiều cao phải > 0.")
        return
    for i in range(1, n + 1):
        print('*' * i)

def draw_right_triangle_dec(n):
    if n <= 0:
        print("Chiều cao phải > 0.")
        return
    for i in range(n, 0, -1):
        print('*' * i)

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ.")

def menu():
    while True:
        print("\n=== MENU VẼ HÌNH BẰNG * ===")
        print("1. Hình chữ nhật rỗng (h x w)")
        print("2. Tam giác vuông tăng (1 -> n)")
        print("3. Tam giác vuông giảm (n -> 1)")
        print("0. Thoát")
        choice = input("Chọn (0-3): ").strip()

        if choice == '0':
            print("Kết thúc chương trình.")
            break
        elif choice == '1':
            h = get_int("Nhập chiều cao h: ")
            w = get_int("Nhập chiều rộng w: ")
            draw_hollow_rectangle(h, w)
        elif choice == '2':
            n = get_int("Nhập n (chiều cao): ")
            draw_right_triangle_inc(n)
        elif choice == '3':
            n = get_int("Nhập n (chiều cao): ")
            draw_right_triangle_dec(n)
        else:
            print("Lựa chọn không hợp lệ. Nhập 0-3.")
        input("\nNhấn Enter để quay lại menu...")

if __name__ == "__main__":
    menu()
