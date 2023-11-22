#cau1: nhap vao 1 list cac phan tu deu la so nguyen
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

# Tìm và in phần tử lớn nhất, nhỏ nhất và tổng
phan_tu_lon_nhat = max(my_list)
phan_tu_nho_nhat = min(my_list)
tong_cac_phan_tu = sum(my_list)

print("Phần tử lớn nhất:", phan_tu_lon_nhat)
print("Phần tử nhỏ nhất:", phan_tu_nho_nhat)
print("Tổng các phần tử:", tong_cac_phan_tu)
