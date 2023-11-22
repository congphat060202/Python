# Nhập mảng số nguyên từ bàn phím
mang_so_nguyen = []
n = int(input("Nhập số lượng phần tử của mảng: "))
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i + 1}: "))
    mang_so_nguyen.append(phan_tu)

# Tính và in ra tổng các số trong khoảng từ 10 đến 100
tong_cac_so_10_den_100 = sum(x for x in mang_so_nguyen if 10 <= x <= 100)
print(f"Tổng các số từ 10 đến 100 là: {tong_cac_so_10_den_100}")

# Tính và in ra trung bình cộng của các số trong khoảng từ 10 đến 100
so_luong_so_10_den_100 = len([x for x in mang_so_nguyen if 10 <= x <= 100])
if so_luong_so_10_den_100 > 0:
    trung_binh_cong = tong_cac_so_10_den_100 / so_luong_so_10_den_100
    print(f"Trung bình cộng của các số từ 10 đến 100 là: {trung_binh_cong}")
else:
    print("Không có số nào trong khoảng từ 10 đến 100.")
