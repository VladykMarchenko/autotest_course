def skip(condition, reason=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                print(reason)
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator

@skip(condition=False, reason='Skip')
def two_plus_two():
    return 2 + 2 == 4

two_plus_two()
print(two_plus_two())