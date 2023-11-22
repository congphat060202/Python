import math

# Nhập giá trị n từ bàn phím
n = int(input("Nhập giá trị n: "))

# Tính n!
factorial_n = math.factorial(n)
print(f"{n}! = {factorial_n}")

# Tính tổng s = 1 + 1/2! + 1/3! + ... + 1/n!
s = 0
for i in range(0, n + 1):
    s += 1 / math.factorial(i)

print(f"Gia tri cua s la: {s}")
