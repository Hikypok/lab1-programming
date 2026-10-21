import math

print(f"{"x":>8} {"sin(x)":>10} {"cos(x)":>10}")
print("-" * 30)

for i in range(11):
    x = i * math.pi / 10
    y1 = math.sin(x)
    y2 = math.cos(x)
    print(f"{x:8.4f} {y1:10.4f} {y2:10.4f}")