# Nhập vào số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử: "))

# Khởi tạo danh sách rỗng
my_list = []

# Nhập từng phần tử và thêm vào danh sách
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i + 1}: "))
    my_list.append(phan_tu)

# In danh sách đã nhập
print("Danh sách đã nhập:", my_list)

# Tăng giá trị của phần tử đầu và cuối lên 10
if len(my_list) >= 2:
    my_list[0] += 10  # Tăng giá trị của phần tử đầu lên 10
    my_list[-1] += 10  # Tăng giá trị của phần tử cuối lên 10
else:
    print("Danh sách có ít hơn 2 phần tử, không thể thực hiện tăng giá trị của phần tử đầu và cuối.")

# In danh sách sau khi tăng giá trị
print("Danh sách sau khi tăng giá trị của phần tử đầu và cuối:", my_list)
# Xóa phần tử cuối cùng nếu danh sách không rỗng
if my_list:
    my_list.pop()
    print("Danh sách sau khi xóa phần tử cuối cùng:", my_list)
else:
    print("Danh sách rỗng, không có phần tử để xóa.")

    # Nhập vào vị trí cần xóa
vi_tri_can_xoa = int(input("Nhập vào vị trí cần xóa: "))

# Kiểm tra xem vị trí cần xóa có hợp lệ hay không
if 0 <= vi_tri_can_xoa < len(my_list):
    # Xóa phần tử tại vị trí đã nhập
    my_list.pop(vi_tri_can_xoa)
    print(f"Danh sách sau khi xóa phần tử tại vị trí {vi_tri_can_xoa}:", my_list)
else:
    print("Vị trí không hợp lệ. Không có phần tử nào được xóa.")

    # Nhập vào giá trị cần xóa
gia_tri_can_xoa = int(input("Nhập giá trị cần xóa: "))

# Kiểm tra xem giá trị cần xóa có trong danh sách hay không
if gia_tri_can_xoa in my_list:
    # Xóa giá trị khỏi danh sách
    my_list.remove(gia_tri_can_xoa)
    print(f"Danh sách sau khi xóa giá trị {gia_tri_can_xoa}:", my_list)
else:
    print(f"Giá trị {gia_tri_can_xoa} không có trong danh sách. Không có gì được xóa.")

    
# Nhập vào giá trị cần xóa
gia_tri_can_xoa = int(input("Nhập giá trị cần xóa: "))

# Kiểm tra xem giá trị cần xóa có trong danh sách hay không
while gia_tri_can_xoa in my_list:
    # Xóa tất cả các phần tử có giá trị bằng giá trị cần xóa
    my_list.remove(gia_tri_can_xoa)

print(f"Danh sách sau khi xóa tất cả giá trị {gia_tri_can_xoa}:", my_list)
