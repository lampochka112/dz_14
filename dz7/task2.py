import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)
        end_time = time.time()  
        print(f"Время выполнения: {end_time - start_time:.6f} секунд")
        return result
    return wrapper

@time_decorator
def get_prime_numbers(start, end):
    primes = []
    for num in range(start, end + 1):
        if num < 2:
            continue  
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

start_range = int(input("Введите начало диапазона: "))
end_range = int(input("Введите конец диапазона: "))

primes = get_prime_numbers(start_range, end_range)

print(f"Простые числа от {start_range} до {end_range}: {primes}")