def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i: 
                count += 1
    return count

def find_numbers_with_k_divisors(a, b, k):
    numbers_with_k_divisors = []
    
    for num in range(a, b + 1):
        if count_divisors(num) == k:
            numbers_with_k_divisors.append(num)
    
    return numbers_with_k_divisors

a = 100 
b = 300 
k = 6    

result = find_numbers_with_k_divisors(a, b, k)
print(f"Числа от {a} до {b} с количеством делителей равным {k}: {result}")