# Nhập chiều dài và chiều rộng của hình chữ nhật từ bàn phím
chieu_dai = float(input("Nhập chiều dài của hình chữ nhật: "))
chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))

# Tính diện tích và chu vi
dien_tich = chieu_dai * chieu_rong
chu_vi = 2 * (chieu_dai + chieu_rong)

# In kết quả
print("Diện tích của hình chữ nhật là:", dien_tich)
print("Chu vi của hình chữ nhật là:", chu_vi)
