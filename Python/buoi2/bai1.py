#cau 1: Viet chuong trinh nhap vao mot chuoi
a = input("Nhap mot chuoi")
print(a.upper())
#cau 2
chuoi = "nguyen nhat hoang"
chuoihoa = chuoi.upper()
chuoihoachudau = chuoi.capitalize()
chuoichucaidauinhoa = chuoi.title()
#cau 3
email = "nhathoangdn95@gmail.com"
emailSplit = email.split('@')
print(emailSplit[0])
print(emailSplit[1])


print(chuoi)
print(chuoichucaidauinhoa)
#cau 6
# Nhập chuỗi từ người dùng
chuoi_ky_tu = input("Nhập vào chuỗi ký tự: ")

# Sử dụng set() để tạo một tập hợp chứa các ký tự duy nhất
cac_loai_gia_tri = set(chuoi_ky_tu)

# Sử dụng phương thức join() để tạo một chuỗi từ tập hợp các ký tự duy nhất
chuoi_cac_loai_gia_tri = ''.join(cac_loai_gia_tri)

# In ra các loại giá trị xuất hiện trong chuỗi
print("Các loại giá trị trong chuỗi là:", chuoi_cac_loai_gia_tri)
#cau 8
from datetime import datetime
# # Nhập họ lót, tên và năm sinh từ người dùng
ho_lot = input("Nhập họ lót: ")
ten = input("Nhập tên: ")
nam_sinh = int(input("Nhập năm sinh: "))
# # Tính tuổi bằng cách lấy năm hiện tại trừ đi năm sinh
nam_hien_tai = datetime.now().year
tuoi = nam_hien_tai - nam_sinh
# # In ra họ và tên cùng với tuổi
print(f"Họ và tên: {ho_lot} {ten}")
print(f"Tuổi: {tuoi} tuổi")
print("Bai 8")
chuoi = input("Nhập chuỗi ký tự: ")
ky_tu = input("Nhập ký tự cần kiểm tra: ")

so_lan_xuat_hien = chuoi.count(ky_tu)
print(f"Số lần xuất hiện của ký tự '{ky_tu}' trong chuỗi là: {so_lan_xuat_hien}")
