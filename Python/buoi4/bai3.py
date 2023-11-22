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

# Sắp xếp và in ra danh sách tăng dần
sorted_list_tang_dan = sorted(my_list)
print("Danh sách sau khi sắp xếp tăng dần:", sorted_list_tang_dan)

# Sắp xếp và in ra danh sách giảm dần
sorted_list_giam_dan = sorted(my_list, reverse=True)
print("Danh sách sau khi sắp xếp giảm dần:", sorted_list_giam_dan)

# In ra danh sách đảo ngược
reversed_list = list(reversed(my_list))
print("Danh sách đảo ngược:", reversed_list)
