# f = open('test.txt', 'a')
# f.write('this is a third line of no real content again.\n')

# f.close()

# f = open('test.txt', 'r')


with open('test.txt', 'r') as f:
    for line in f.readlines():
        print(line, end='')