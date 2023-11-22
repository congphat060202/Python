# Nhập giá trị n từ bàn phím
n = int(input("Nhập giá trị n: "))

# Khởi tạo biến tổng s
s = 0

# Tính tổng các số từ 1 đến n
for i in range(1, n + 1):
    s += 1/i

# In kết quả
print(f"Gia tri cua s la: {s}")
