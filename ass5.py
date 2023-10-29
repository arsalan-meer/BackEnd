def read_file_in_reverse(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        reversed_lines = lines[::-1]
        for line in reversed_lines:
            print(line.strip())
        return reversed_lines