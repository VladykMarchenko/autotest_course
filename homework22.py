def read_last(file_path, symbol_number):
    open_file = open(file_path).readlines()
    for file in open_file:
        if file.strip() != "":
            print(file.strip()[-symbol_number:])
read_last('read_last.txt', 6)

