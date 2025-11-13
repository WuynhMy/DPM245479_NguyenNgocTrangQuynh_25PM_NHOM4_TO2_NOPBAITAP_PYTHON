'''Xử lý Text File - Viết phần mềm Quản Lý sản phẩm
Yêu cầu:
Viết phần mềm Quản Lý sản phẩm
Mỗi danh mục có: Mã , tên; Một danh mục có nhiều sản phẩm
Mỗi sản phẩm có: Mã, tên, đơn giá; Mỗi một sản phẩm thuộc về một danh mục.
Cho phép: lưu mới, sửa, xóa, tìm kiếm, sắp xếp, lưu và đọc Text File'''
# Danh mục
C|DM01|Điện thoại
C|DM02|Laptop

# Sản phẩm
P|SP01|iPhone 15|25000000|DM01
P|SP02|MacBook Pro|45000000|DM02
P|SP03|Samsung S24|22000000|DM01
import os

# ==============================
# ĐỊNH NGHĨA LỚP DỮ LIỆU
# ==============================
class Category:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten

class Product:
    def __init__(self, ma, ten, don_gia, ma_dm):
        self.ma = ma
        self.ten = ten
        self.don_gia = float(don_gia)
        self.ma_dm = ma_dm


# ==============================
# LỚP QUẢN LÝ
# ==============================
class QuanLySanPham:
    def __init__(self, filename="data.txt"):
        self.filename = filename
        self.danh_muc = []
        self.san_pham = []
        self.doc_file()

    # ---- Đọc dữ liệu từ file ----
    def doc_file(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split("|")
                if parts[0] == "C":
                    self.danh_muc.append(Category(parts[1], parts[2]))
                elif parts[0] == "P":
                    self.san_pham.append(Product(parts[1], parts[2], parts[3], parts[4]))

    # ---- Ghi dữ liệu ra file ----
    def ghi_file(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write("# Danh mục\n")
            for dm in self.danh_muc:
                f.write(f"C|{dm.ma}|{dm.ten}\n")
            f.write("\n# Sản phẩm\n")
            for sp in self.san_pham:
                f.write(f"P|{sp.ma}|{sp.ten}|{sp.don_gia}|{sp.ma_dm}\n")

    # ---- Quản lý Danh mục ----
    def them_danh_muc(self, ma, ten):
        self.danh_muc.append(Category(ma, ten))

    # ---- Quản lý Sản phẩm ----
    def them_san_pham(self, ma, ten, don_gia, ma_dm):
        self.san_pham.append(Product(ma, ten, don_gia, ma_dm))

    def sua_san_pham(self, ma, ten_moi=None, don_gia_moi=None, ma_dm_moi=None):
        for sp in self.san_pham:
            if sp.ma == ma:
                if ten_moi: sp.ten = ten_moi
                if don_gia_moi: sp.don_gia = float(don_gia_moi)
                if ma_dm_moi: sp.ma_dm = ma_dm_moi
                return True
        return False

    def xoa_san_pham(self, ma):
        self.san_pham = [sp for sp in self.san_pham if sp.ma != ma]

    def tim_kiem_san_pham(self, keyword):
        return [sp for sp in self.san_pham if keyword.lower() in sp.ten.lower()]

    def sap_xep_theo_gia(self, tang_dan=True):
        self.san_pham.sort(key=lambda sp: sp.don_gia, reverse=not tang_dan)

    def hien_thi_san_pham(self):
        print("\n=== DANH SÁCH SẢN PHẨM ===")
        for sp in self.san_pham:
            dm_ten = next((d.ten for d in self.danh_muc if d.ma == sp.ma_dm), "Không rõ")
            print(f"{sp.ma:6} | {sp.ten:25} | {sp.don_gia:10,.0f} | {dm_ten}")


# ==============================
# GIAO DIỆN MENU
# ==============================
def menu():
    ql = QuanLySanPham()
    while True:
        print("""
========= MENU =========
1. Thêm danh mục
2. Thêm sản phẩm
3. Sửa sản phẩm
4. Xóa sản phẩm
5. Tìm kiếm sản phẩm
6. Sắp xếp theo giá
7. Hiển thị danh sách
8. Lưu dữ liệu
0. Thoát
========================
""")
        chon = input("Chọn: ").strip()
        if chon == "1":
            ma = input("Mã danh mục: ")
            ten = input("Tên danh mục: ")
            ql.them_danh_muc(ma, ten)
        elif chon == "2":
            ma = input("Mã SP: ")
            ten = input("Tên SP: ")
            don_gia = input("Đơn giá: ")
            ma_dm = input("Mã danh mục: ")
            ql.them_san_pham(ma, ten, don_gia, ma_dm)
        elif chon == "3":
            ma = input("Mã SP cần sửa: ")
            ten = input("Tên mới (Enter nếu bỏ qua): ")
            don_gia = input("Đơn giá mới (Enter nếu bỏ qua): ")
            ma_dm = input("Mã danh mục mới (Enter nếu bỏ qua): ")
            ql.sua_san_pham(ma, ten or None, don_gia or None, ma_dm or None)
        elif chon == "4":
            ma = input("Mã SP cần xóa: ")
            ql.xoa_san_pham(ma)
        elif chon == "5":
            kw = input("Từ khóa: ")
            kq = ql.tim_kiem_san_pham(kw)
            for sp in kq:
                print(f"{sp.ma} - {sp.ten} - {sp.don_gia:,.0f}")
        elif chon == "6":
            ql.sap_xep_theo_gia()
            print("Đã sắp xếp theo giá tăng dần.")
        elif chon == "7":
            ql.hien_thi_san_pham()
        elif chon == "8":
            ql.ghi_file()
            print("Đã lưu dữ liệu.")
        elif chon == "0":
            ql.ghi_file()
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")


# ==============================
# CHẠY CHƯƠNG TRÌNH
# ==============================
if __name__ == "__main__":
    menu()
