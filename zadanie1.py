import pickle
import os
import hashlib

def cache_result(cache_dir):
    def decorator(func):
        def wrapper(*args, **kwargs):
            cache_key = func.__name__ + str(args) + str(kwargs)
            cache_key_hash = hashlib.sha256(cache_key.encode()).hexdigest()
            cache_file = os.path.join(cache_dir, cache_key_hash + '.pkl')

            os.makedirs(cache_dir, exist_ok=True)

            if os.path.exists(cache_file):
                with open(cache_file, 'rb') as file:
                    result = pickle.load(file)
            else:
                result = func(*args, **kwargs)
                with open(cache_file, 'wb') as file:
                    pickle.dump(result, file)
            return result
        return wrapper
    return decorator

@cache_result('cached_results')
def exfunction(x):
    print(f"Obliczam wynik dla x = {x}")
    return x * 2

result1 = exfunction(5)
print("Wynik pierwszego wywołania:", result1)

result2 = exfunction(5)
print("Wynik drugiego wywołania:", result2)

result3 = exfunction(10)
print("Wynik trzeciego wywołania:", result3)