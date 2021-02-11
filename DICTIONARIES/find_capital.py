capitals = dict(France="Paris", United_States="Washington", United_Kingdom="London", Portugal="Lisbon", Italy="Rome")

user_input = input("which country would you like to check? ").lower()

while 'united_kingdom' not in user_input and not user_input.isalpha():
    if user_input == 'united_states':
        break
    print("you must input a string")
user_input = user_input.title()

if user_input in capitals:
    print(f"the capital of {user_input} is {capitals[user_input]}")
else:
    print("No Data Available")