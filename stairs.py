numberOfStairs = int(input("Введите количество ступенек\n"))

for i in range(1,numberOfStairs + 1):
    print(" " * (numberOfStairs - i) + "#" * i)