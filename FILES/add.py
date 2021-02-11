user_input = input("please enter another capital city: ")

file =  open('capitals.txt', 'a')
file.write('\n' + user_input)
file.close()

file = open('capitals.txt', 'r')
print(file.read())
file.close

