'''Xử lý XML File - Viết phần mềm Quản Lý Thiết Bị
Yêu cầu:
Chương trình quản lý thiết bị gồm có 2 tập dữ liệu
Tập lưu danh sách nhóm thiết bị có tên nhomthietbi.xml có dữ liệu mẫu và format như
dưới đây:'''
<?xml version="1.0" encoding="UTF-8" ?>
<nhoms>
 <nhom>
 <ma>n1</ma>
 <ten>Nhóm 1</ten>
 </nhom>
 <nhom>
 <ma>n2</ma>
 <ten>Nhóm 2</ten>
 </nhom>
 <nhom>
 <ma>n3</ma>
 <ten>Nhóm 3</ten>
 </nhom>
</nhoms>

<?xml version="1.0" encoding="UTF-8" ?>
<thietbis>
 <thietbi manhom="n1">
 <ma>tb1</ma>
 <ten>Thiết bị 2</ten>
 </thietbi>
 <thietbi manhom="n1">
 <ma>tb2</ma>
 <ten>Thiết bị 2</ten>
 </thietbi>
 <thietbi manhom="n2">
 <ma>tb3</ma>
 <ten>Thiết bị 3</ten>
 </thietbi>
 <thietbi manhom="n3">
 <ma>tb4</ma>
Trang 71/84
 <ten>Thiết bị 4</ten>
 </thietbi>
 <thietbi manhom="n3">
 <ma>tb5