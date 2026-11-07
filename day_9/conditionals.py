age = int(input("Enter your age: "))
agesleft = 18 - age
if age >= 18:
   print("You are old enough to learn to drive.")
else:
   print(f"You need {agesleft} more years to learn to drive.")

# Level 1 ex2

my_age = 18
your_age = int(input("Enter your age: "))
if your_age == my_age:
    print("We are the same age!")
elif your_age < my_age:
    agesleft = my_age - your_age
    if agesleft == 1:
        print("You are 1 year younger than me.")
    else:
        print(f"You are {agesleft} years younger than me.")
else:
    agesleft = your_age - my_age
    if agesleft == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {agesleft} years older than me.")

# Level 1 ex 3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# Level 2 ex 1

score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("Your grade is A")
elif 80 <= score <= 89:
    print("Your grade is B")
elif 70 <= score <= 79:
    print("Your score is C")
elif 60 <= score <= 69:
    print("Your score is D")
elif 0 <= score <= 59:
    print("Your score is F")

# Level 2 ex 2
users_month = input("Enter the month: ").capitalize()
Autumn = {"September", "October", "November"}
Winter = {"December", "January", "February"}
Spring = {"March", "April", "May"}
Summer = {"June", "July", "August"}
if users_month in Autumn:
    print("The season is autumn")
elif users_month in Winter:
    print("The season is winter")
elif users_month in Spring:
    print("The season is spring")
elif users_month in Summer:
    print("The season is summer")
else:
    print("Invalid month entered")

#Level 2 ex 3
fruits = ['banana', 'orange', 'mango', 'lemon']
users_fruit = input("Enter your fruit: ").lower()
if users_fruit in fruits:
    print("That fruit already exist in the list.")
elif users_fruit not in fruits:
    fruits.append(users_fruit)
    print(fruits)

#Level 3 ex 3
    person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
isit = "skills" in person
length = len(person["skills"])
middle_index = length // 2
if isit:
    print(person["skills"][middle_index])
if "skills" in person:
    has_python = "Python" in person["skills"]
    print(has_python)
if "skills" in person:
    skills_set = set(person["skills"])
    
    if skills_set == {"JavaScript", "React"}:
        print("He is a front end developer")
    elif skills_set == {"Node", "Python", "MongoDB"}:
        print("He is a backend developer")
    elif skills_set == {"React", "Node", "MongoDB"}:
        print("He is a fullstack developer")
    else:
        print("unknown title")
if person.get("is_married") and person.get("country") == "Finland":
    print(f"{person['first_name']} lives in {person['country']}. He is married.")
