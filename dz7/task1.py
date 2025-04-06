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
def get_prime_numbers():
    primes = []
    for num in range(2, 1001):  
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1): 
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

primes = get_prime_numbers()
print("Простые числа от 0 до 1000:", primes)