def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i: 
                count += 1
    return count

numbers_with_six_divisors = []

for num in range(200, 501):
    if count_divisors(num) == 6:
        numbers_with_six_divisors.append(num)

print("Числа от 200 до 500 с ровно шестью делителями:", numbers_with_six_divisors)