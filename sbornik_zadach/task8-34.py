def sum_of_divisors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

numbers_with_sum_of_divisors_50 = []

for num in range(100, 301):
    if sum_of_divisors(num) == 50:
        numbers_with_sum_of_divisors_50.append(num)

print("Числа от 100 до 300 с суммой делителей равной 50:", numbers_with_sum_of_divisors_50)