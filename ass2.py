def read_file_into_list(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines
