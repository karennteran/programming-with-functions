from datetime import datetime

# functions:
# print the current time and task name
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = "susan"
print_time("first name assigned")

for x in range(0,10):
    print(x)
print_time("loop completed")

print()

# without a function and a little peek at list again:
first_name = input("enter your first name: ")
first_name_initial = first_name[0:1]
last_name = input("enter your last name: ")
last_name_initial = last_name[0:1]

print(f"your initials are: {first_name_initial.capitalize()}{last_name_initial.capitalize()}")
print()

# changing code above with a function
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input("enter your first name: ")
first_name_initial = get_initial(first_name) 

last_name = input("enter your last name: ")
last_name_initial = get_initial(last_name)

print(f"your initials are: {first_name_initial}{last_name_initial}")
print()

# another way to call this same function above:
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input("enter your first name: ")
last_name = input("enter your last name: ")

print(f"your initials are: {get_initial(first_name)}{get_initial(last_name)}")
