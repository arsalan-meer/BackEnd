def write_first_line_to_file(file_contents, output_filename):
    first_line = file_contents.split('\n')[0]
    with open(output_filename, 'w') as output_file:
        output_file.write(first_line)