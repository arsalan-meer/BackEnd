def read_even_numbered_lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        even_lines = [line.strip() for index, line in enumerate(lines) if index % 2 != 0]
        return even_lines