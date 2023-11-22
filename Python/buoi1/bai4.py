import math
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

# tính nửa chu vi tam giác
s = (a+b+c)/2
# tính diện tích tam giác theo công thức Heron

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

# tính chu vi tam giác

perimeter = a+b+c

print(f"diện tích tam giác là: {area} ")
print(f"chu vi tam giác là: {perimeter}")
