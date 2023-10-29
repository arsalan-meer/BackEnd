def read_file(file_name):
    with open(file_name, 'r') as file:
        contents = file.read()
        print(contents)
        return contents