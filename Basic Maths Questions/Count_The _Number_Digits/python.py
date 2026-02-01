def countDigits(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

n = int(input())
num_of_digits_in_n = countDigits(n)
print(num_of_digits_in_n)

# Time Complexity == O(n)
# Space Complexity == O(1)