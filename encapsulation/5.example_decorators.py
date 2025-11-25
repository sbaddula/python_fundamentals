def my_decorator(func):
    def wrapper():
        print("Before execution")
        func()
        print("After execution")
    return wrapper

@my_decorator
def greet():
    print("Hello, World!")

greet()

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def add(a, b):
    return a + b

print(add(5, 3))