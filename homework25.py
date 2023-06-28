# # def call_coutner(file_path):
# #     open_file = open(file_path, "a").write("Function 'add' was called\n")
# #     return open_file
# #
# # @call_coutner("data.txt")
# # def add(a, b):
# #     return a + b
# # print(add(4, 6))
#
#
# from functools import wraps
# def decorator(*args, **kwargs):
#     def inner(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print(args)
#             value = func(*args, **kwargs)
#             print("end")
#             return value
#         return wrapper
#     return inner
# @decorator()
# def say():
#     print("hello")
# say()
#
# """
# С параметрами надо 2 уровня вложенности
# """
#
#
# from functools import wraps
# def decorator(func):
#         # @wraps(func)
#         def wrapper(*args, **kwargs):
#             print(args)
#             value = func(*args, **kwargs)
#             print("end")
#             return value
#         return wrapper
# @decorator
# def say(a=1,b=2):
#     print("hello")
# # say()
#     return a + b
# print(say())
# print(say.__name__)
# """
# если есть wraps то мы декорируем нашу функцию обертку в декоратор
# Обёртка -
# """


def call_counter(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file_name, 'a') as file:
                file.write(f"Function '{func.__name__}' was called {wrapper.counter} times\n") #сделай непалевно
            wrapper.counter += 1
            return func(*args, **kwargs)

        wrapper.counter = 1
        return wrapper
    return decorator


@call_counter('data.txt')
def add(a, b):
    return a + b
print(add(4, 6))

