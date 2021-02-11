def copy_file(in_file, out_file):
    with open(in_file) as file:
        with open(out_file, 'w') as file_one:
            file_one.write(file.read())

copy_file('capitals.txt', 'new_capitals.txt')