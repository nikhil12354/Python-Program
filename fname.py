#This is a simple python project to show first and last name

fName = input("Please enter first name:")
lName = input("Please enter last name:")
age = input("How old are you?:")


if age.isdigit():
    print(f"My name is {fName} {lName} & my age is {age}.")

else:
    print("Age should be a number and not a letter.")