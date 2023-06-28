def call_counter(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file_name, 'a') as file:
                file.write(f"Function '{func.__name__}' was called {wrapper.counter} times\n")
            wrapper.counter += 1
            return func(*args, **kwargs)

        wrapper.counter = 1
        return wrapper
    return decorator


@call_counter('data.txt')
def add(a, b):
    return a + b
print(add(4, 6))
print(add(4, 6))
print(add(4, 6))
print(add(4, 6))

