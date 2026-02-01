def evenly_divides(N):
    count = 0
    temp = N
    while temp > 0:
        last_digit = temp % 10
        if last_digit > 0 and N % last_digit == 0:
            count += 1
            temp //= 10
        return count
    
N = int(input())
Digits_that_evenly_divides = evenly_divides(N)
print(Digits_that_evenly_divides)
