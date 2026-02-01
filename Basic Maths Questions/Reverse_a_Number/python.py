n = int(input())
x = 0

while n != 0:
    last_digit = n % 10
    x = x * 10 + last_digit
    n //= 10

print(x)