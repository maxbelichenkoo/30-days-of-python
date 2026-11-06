
dog = {}
dog["name"] = ["Barsik"]
dog["color"] = ["ginger"]
dog["breed"] = ["German Shepherd"]
dog["legs"] = ["4"]
dog["age"] = ["6 years"]

student = {
    "first_name": "Maksym",
    "last_name": "Belichenko",
    "gender": "Male",
    "age": 18,
    "marital_status": "Single",
    "skills": ["Python", "Git", "Linguistics"],
    "country": "Ukraine",
    "city": "Odesa",
    "address": "Deribasovskaya Street"
}
length = len(student)
skills_value = student["skills"]
is_list = isinstance(skills_value, list)
student["skills"].append("SQL")
keys = student.keys()
values = student.values()
student_tuples = list(student.items())
print(student)
del student["marital_status"]
del student