# A dictionary is a collection of key-value pairs.
student = {
    "name": "Rahul",
    "age": 25,
    "courses": ["Math", "Computer Science"],
    "graduated": True
}
print(f"student = {student}")

#print different parts of dictionary
print(f"name of student = {student['name']}")
print(f"age of student = {student['age']}")
print(f"what courses did the student have = {student['courses']}")
print(f"did student graduate = {student['graduated']}")

#add GPA key to dictionary student
student ['gpa'] = 9.1
print(f"student = {student}")

#looping over dictionary :method 1
print("method 1")
for key in student:
    print(f"key = {key}, value = {student[key]}")

print("_"*100)
#looping over dictionary method:2
print("method 2")
for key in student.keys():
    print(f"key = {key}, value = {student[key]}")

print("_"*100)
#looping over dictionary method:3
print("method 3")
for key, value in student.items():
    print(f"key = {key}, value = {value}")

# Nested Dictionaries
# Dictionaries can contain other dictionaries, allowing for complex data structures.
students_dictionary = {
    "student1": {"name": "Rahul", "age": 25, "GPA": 8},
    "student2": {"name": "Atheendra", "age": 24, "GPA": 9},
}

# List of Dictionaries
students_list = [
{"name": "Rahul", "age": 25, "GPA": 8},
{"name": "Atheendra", "age": 24, "GPA": 9}
]


print("_"*100)
print("student 1 details:")
print(f"name = {students_dictionary['student1']['name']}")
print(f"age = {students_dictionary['student1']['age']}")
print(f"GPA = {students_dictionary['student1']['GPA']}")

print("student 2 details:")
print(f"name = {students_dictionary['student2']['name']}")
print(f"age = {students_dictionary['student2']['age']}")
print(f"GPA = {students_dictionary['student2']['GPA']}")

print("_"*100)
print("method 2")
for student in students_dictionary:
    print(f"name = {students_dictionary[student]['name']}")
    print(f"age = {students_dictionary[student]['age']}")
    print(f"gpa = {students_dictionary[student]['GPA']}")


# List of Dictionaries
students_list = [
{"name": "Rahul", "age": 25, "GPA": 8},
{"name": "Atheendra", "age": 24, "GPA": 9}
]

print("_"*100)
print("method 1")
for student in students_list:
    print(f"name = {student['name']}")
    print(f"age = {student['age']}")
    print(f"gpa = {student['GPA']}")

print("_"*100)
print("method 2")
for i in range(len(students_list)):
    print(f"name = {students_list[i]['name']}")
    print(f"age = {students_list[i]['age']}")
    print(f"gpa = {students_list[i]['GPA']}")


print("_"*100)
print("method 3")
print("_"*100)
for index, student in enumerate(students_list):
    print(f"name of student number{index + 1} = {students_list[index]['name']}. Also equal to {student['name']}")
    print(f"age of student number{index + 1} = {students_list[index]['age']}. Also equal to {student['age']}")
    print(f"gpa of student number{index + 1} = {students_list[index]['GPA']}.Also equal to {student['GPA']}")


