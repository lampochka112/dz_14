def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = [p for p in range(2, int(300**0.25) + 1) if is_prime(p)]

numbers_with_five_divisors = [p**4 for p in primes if p**4 <= 300]

print("Числа от 1 до 300 с ровно пятью делителями:", numbers_with_five_divisors)