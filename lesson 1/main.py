import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"הפונקציה '{func.__name__}' רצה במשך {execution_time:.4f} שניות")
        return result
    return wrapper


@measure_time
def simple_function():
    time.sleep(0.1)


@measure_time
def complex_function(n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += i * j
    return result

simple_function()
complex_function(1000)

def cache(func):
    memory = {}
    def wrapper(*args):
        if args in memory:
            return memory[args]
        else:
            result = func(*args)
            memory[args] = result
            return result
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_without_cache(n):
    if n <= 1:
        return n
    return fibonacci_without_cache(n-1) + fibonacci_without_cache(n-2)

@measure_time
def run_fibonacci(func, n):
    return func(n)

print("חישוב פיבונאצ'י עם Cache:")
result_with_cache = run_fibonacci(fibonacci, 30)
print(f"התוצאה: {result_with_cache}")

print("\nחישוב פיבונאצ'י ללא Cache:")
result_without_cache = run_fibonacci(fibonacci_without_cache, 30)
print(f"התוצאה: {result_without_cache}")