# In ra các số chẵn trong khoảng từ 0 đến 1000
print("Các số chẵn trong khoảng từ 0 đến 1000:")
for i in range(0, 1001, 2):
    print(i, end=" ")

# Tính tổng các số chẵn trong khoảng từ 0 đến 1000
tong_so_chan = sum(range(0, 1001, 2))
print("\nTổng các số chẵn trong khoảng từ 0 đến 1000:", tong_so_chan)
