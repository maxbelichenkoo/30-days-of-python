#task 1

str1 = "Thirty "
str2 = "Days "
str3 = "Of "
str4 = "Python"
full_sent = str1 + str2 + str3 + str4
print(full_sent)

#task 2

str1 = "Coding "
str2 = "For "
str3 = "All"
full_sent = str1 + str2 + str3
print(full_sent)

#task 3-7
company = "Coding For All"
print(company)
length = len(company)
print(length)
upper = company.upper()
print(upper)
lower = company.lower()
print(lower)

#task 8-11
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
found = "Coding"
print(company.index(found))
print(company.index("Coding"))

print(company.replace("Coding", "Python"))

#task 12
text = "Python For Everyone"
print(text.replace("Everyone", "All"))

#task 13
sent = "Coding For All"
print(sent.split())

#task 14
apps = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(apps.split(", "))

#task 15
sent = "Coding For All"
print(sent[0])

#task 16
sent = "Coding For All"
print(len(sent) - 1)

#task 17
string = "Coding For All"
print(string[10])

#task 18-19
print("".join([word[0].upper() for word in text.split()]))
print("".join([word[0].upper() for word in string.split()]))

#task 20-21
print(string.find("C"))
print(string.find("F"))

#task 22
prompt = "Coding For All People"
print(prompt.rfind("l"))

#task 23-27
end = 'You cannot end a sentence with because because because is a conjunction'
print(end.find("because"))
print(end.rindex("because"))
print(end[31:54])
print(end.find("because"))
print(end[31:54])

#task 28-29
print(string.startswith("Coding"))
print(string.endswith("coding"))

#task 30
spaces ="    Coding For All      "
print(spaces.strip())

#task 31
ex1 = "30DaysOfPython"
ex2 = "thirty_days_of_python"
print(ex1.isidentifier())
print(ex2.isidentifier())

#task 32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(libraries))

#task 33
print("I am enjoying this challenge.\nI just wonder what is next.")

#task 34
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

#task 35
radius = 10
area = int(3.14 * radius ** 2)
print(f"The area of a circle with radius {radius} is {area} meters square.")

#task 36
a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")