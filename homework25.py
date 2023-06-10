def call_coutner(file_path):
    open_file = open(file_path, "a").write("Function 'add' was called\n")
    return open_file

@call_coutner("data.txt")
def add(a, b):
    return a + b
print(add(4, 6))



