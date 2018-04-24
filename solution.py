import sys

#digit_string = sys.argv[1]
digit_string = input("Введите строку, состоящую из цифр от 0 до 9\n")
sum = 0
for digit in digit_string:
    sum += int(digit)
print(sum)