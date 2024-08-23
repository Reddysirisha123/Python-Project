import pandas as pd

myclass = {
    "Name": ["Rishabh", "Sanjana Nayak", "Shaina Michael", "Monali", "Chaitanya", "Anish",
             "Nandey", "Rishabh", "Adarsh", "Simran", "Anish", "Siddharth", "Atheendra", "Aayushi"],
    "Age": [22, 24, 23, 25, 27, 26, 22, 24, 25, 23, 26, 27, 28, 24],
    "GPA": [3.8, 3.9, 3.7, 3.5, 3.6, 3.8, 3.4, 3.9, 3.2, 3.7, 3.5, 3.6, 3.9, 3.8],
    "Major": ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering",
              "Computer Science", "Data Science", "Computer Science", "Data Science",
              "Mechanical Engineering", "Electrical Engineering", "Civil Engineering",
              "Mechanical Engineering", "Computer Science", "Data Science"]
}

data_frame = pd.DataFrame(myclass)
print(data_frame)

print ("looping over columns")
for column in data_frame.columns:
    print(f"column name = {column}")
    print(f"column value = {data_frame[column]}")

print("_"*100)
print ("looping over rows")
for index, row in data_frame.iterrows():
    print(f"Student Number = {index + 1}")
    print(f"Name = {row['Name']}\n Age = {row['Age']}; GPA = {row['GPA']}; Major = {row['Major']}")

print("_"*100)
print("statistics of age")
print(f"Minium Age of Students = {min(data_frame['Age'])}")
print(f"Maximum Age of Students = {max(data_frame['Age'])}")
print(f"Mode Age of Students = {data_frame['Age'].mode()[0]}")
print(f"Median Age of Students = {data_frame['Age'].median()}")
print(f"Mean Age of Students = {data_frame['Age'].mean()}")

print("_"*100)
print("statistics of GPA")
print(f"Minium Age of Students = {min(data_frame['GPA'])}")
print(f"Maximum Age of Students = {max(data_frame['GPA'])}")
print(f"Mode Age of Students = {data_frame['GPA'].mode()[0]}")
print(f"Median Age of Students = {data_frame['GPA'].median()}")
print(f"Mean Age of Students = {data_frame['GPA'].mean()}")


