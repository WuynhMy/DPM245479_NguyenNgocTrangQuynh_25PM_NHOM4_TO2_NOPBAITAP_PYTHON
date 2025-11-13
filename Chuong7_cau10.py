'''Xử lý JSON File - Viết phần mềm Quản Lý Sinh Viên
Yêu cầu:
Viết phần mềm quản lý Sinh Viên
Mỗi một lớp có: Mã lớp, tên; một lớp có nhiều Sinh viên
Mỗi sinh viên có: mã, tên, năm sinh; Mỗi một sinh viên thuộc về một lớp.
Cho phép: lưu mới, sửa, xóa, tìm kiếm, sắp xếp, lưu và đọc JSon File
'''
{
  "lop": [
    {"ma_lop": "L01", "ten_lop": "CNTT A"},
    {"ma_lop": "L02", "ten_lop": "Kinh tế B"}
  ],
  "sinh_vien": [
    {"ma_sv": "SV01", "ten_sv": "Nguyen Van A", "nam_sinh": 2003, "ma_lop": "L01"},
    {"ma_sv": "SV02", "ten_sv": "Tran Thi B", "nam_sinh": 2004, "ma_lop": "L02"}
  ]
}
import json
import os


# ==============================
# ĐỊNH NGHĨA LỚP DỮ LIỆU
# ==============================
class Lop:
    def __init__(self, ma_lop, ten_lop):
        self.ma_lop = ma_lop
        self.ten_lop = ten_lop

    def to_dict(self):
        return {"ma_lop": self.ma_lop, "ten_lop": self.ten_lop}


class SinhVien:
    def __init__(self, ma_sv, ten_sv, nam_sinh, ma_lop):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv
        self.nam_sinh = int(nam_sinh)
        self.ma_lop = ma_lop

    def to_dict(self):
        return {
            "ma_sv": self.ma_sv,
            "ten_sv": self.ten_sv,
            "nam_sinh": self.nam_sinh,
            "ma_lop": self.ma_lop,
        }


# ==============================
# LỚP QUẢN LÝ
# ==============================
class QuanLySinhVien:
    def __init__(self, filename="sinhvien.json"):
        self.filename = filename
        self.lop = []
        self.sinh_vien = []
        self.doc_file()

    # ---- Đọc file JSON ----
    def doc_file(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.lop = [Lop(**lop) for lop in data.get("lop", [])]
            self.sinh_vien = [SinhVien(**sv) for sv in data.get("sinh_vien", [])]

    # ---- Ghi file JSON ----
    def ghi_file(self):
        data = {
            "lop": [lop.to_dict() for lop in self.lop],
            "sinh_vien": [sv.to_dict() for sv in self.sinh_vien],
        }
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # ---- Quản lý Lớp ----
    def them_lop(self, ma_lop, ten_lop):
        if any(l.ma_lop == ma_lop for l in self.lop):
            print("❌ Mã lớp đã tồn tại!")
            return
        self.lop.append(Lop(ma_lop, ten_lop))

    # ---- Quản lý Sinh viên ----
    def them_sv(self, ma_sv, ten_sv, nam_sinh, ma_lop):
        if any(sv.ma_sv == ma_sv for sv in self.sinh_vien):
            print("❌ Mã sinh viên đã tồn tại!")
            return
        if not any(l.ma_lop == ma_lop for l in self.lop):
            print("❌ Mã lớp không tồn tại!")
            return
        self.sinh_vien.append(SinhVien(ma_sv, ten_sv, nam_sinh, ma_lop))

    def sua_sv(self, ma_sv, ten_moi=None, nam_sinh_moi=None, ma_lop_moi=None):
        for sv in self.sinh_vien:
            if sv.ma_sv == ma_sv:
                if ten_moi:
                    sv.ten_sv = ten_moi
                if nam_sinh_moi:
                    sv.nam_sinh = int(nam_sinh_moi)
                if ma_lop_moi:
                    sv.ma_lop = ma_lop_moi
                return True
        return False

    def xoa_sv(self, ma_sv):
        self.sinh_vien = [sv for sv in self.sinh_vien if sv.ma_sv != ma_sv]

    def tim_kiem_sv(self, keyword):
        return [sv for sv in self.sinh_vien if keyword.lower() in sv.ten_sv.lower()]

    def sap_xep_theo_ten(self, tang_dan=True):
        self.sinh_vien.sort(key=lambda sv: sv.ten_sv, reverse=not tang_dan)

    def hien_thi_sv(self):
        print("\n=== DANH SÁCH SINH VIÊN ===")
        for sv in self.sinh_vien:
            ten_lop = next((l.ten_lop for l in self.lop if l.ma_lop == sv.ma_lop), "Không rõ")
            print(f"{sv.ma_sv:6} | {sv.ten_sv:25} | {sv.nam_sinh:4} | {ten_lop}")


# ==============================
# GIAO DIỆN MENU
# ==============================
def menu():
    ql = QuanLySinhVien()

    while True:
        print("""
========= MENU =========
1. Thêm lớp
2. Thêm sinh viên
3. Sửa sinh viên
4. Xóa sinh viên
5. Tìm kiếm sinh viên
6. Sắp xếp theo tên
7. Hiển thị danh sách
8. Lưu dữ liệu
0. Thoát
========================
""")
        chon = input("Chọn: ").strip()

        if chon == "1":
            ma = input("Mã lớp: ")
            ten = input("Tên lớp: ")
            ql.them_lop(ma, ten)

        elif chon == "2":
            ma = input("Mã SV: ")
            ten = input("Tên SV: ")
            nam = input("Năm sinh: ")
            ma_lop = input("Mã lớp: ")
            ql.them_sv(ma, ten, nam, ma_lop)

        elif chon == "3":
            ma = input("Mã SV cần sửa: ")
            ten = input("Tên mới (Enter để bỏ qua): ")
            nam = input("Năm sinh mới (Enter để bỏ qua): ")
            ma_lop = input("Mã lớp mới (Enter để bỏ qua): ")
            ql.sua_sv(ma, ten or None, nam or None, ma_lop or None)

        elif chon == "4":
            ma = input("Mã SV cần xóa: ")
            ql.xoa_sv(ma)

        elif chon == "5":
            kw = input("Từ khóa tìm kiếm: ")
            kq = ql.tim_kiem_sv(kw)
            for sv in kq:
                print(f"{sv.ma_sv} - {sv.ten_sv} - {sv.nam_sinh}")

        elif chon == "6":
            ql.sap_xep_theo_ten()
            print("✅ Đã sắp xếp theo tên.")

        elif chon == "7":
            ql.hien_thi_sv()

        elif chon == "8":
            ql.ghi_file()
            print("✅ Đã lưu dữ liệu vào file JSON.")

        elif chon == "0":
            ql.ghi_file()
            print("👋 Thoát chương trình.")
            break

        else:
            print("❌ Lựa chọn không hợp lệ!")


# ==============================
# CHẠY CHƯƠNG TRÌNH
# ==============================
if __name__ == "__main__":
    menu()
