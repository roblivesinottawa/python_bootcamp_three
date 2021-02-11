import os.path

filename = 'test.txt'

if not os.path.isfile(filename):
    print('file does not exist')
else:
    with open(filename) as file:
        content = file.read()
    
    print(content)