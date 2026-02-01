def printDigits(n):
    while n != 0:
        last_digit = n % 10
        n //= 10
        print(last_digit)

n = int(input())
printDigits(n)