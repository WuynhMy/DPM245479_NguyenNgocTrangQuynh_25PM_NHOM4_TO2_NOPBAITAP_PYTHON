'''Viết chương trình nhập vào một dãy các số theo thứ tự tăng, nếu nhập sai
quy cách thì yêu cầu nhập lại. In dãy số sau khi đã nhập xong '''
def nhap_day_tang():
    while True:
        try:
            # Nhập dãy số cách nhau bằng dấu cách
            s = input("Nhập dãy số theo thứ tự tăng dần (cách nhau bởi dấu cách): ")
            lst = [int(x) for x in s.split()]

            # Kiểm tra thứ tự tăng dần
            if all(lst[i] < lst[i + 1] for i in range(len(lst) - 1)):
                return lst
            else:
                print("❌ Dãy không tăng dần! Vui lòng nhập lại.\n")
        except ValueError:
            print("⚠️ Lỗi: Vui lòng nhập toàn số nguyên.\n")


# --- Chương trình chính ---
day_so = nhap_day_tang()
print(f"✅ Dãy số hợp lệ: {day_so}")
