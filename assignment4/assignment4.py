import pandas as pd
import csv


people_dict = {'Name': ['Alice', 'Bob', 'Charlie'],
               'Age': [25,30,35],
               'City': ['New York', 'Los Angeles', 'Chicago']
               }
task1_data_frame= pd.DataFrame(people_dict)

print(task1_data_frame)

task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)


task1_older = task1_with_salary.copy()
task1_older['Age'] = [v+1 for v in task1_older['Age']]
print(task1_older)


task1_older.to_csv('employees.csv', index=False)

task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

json_employees = pd.read_json('additional_employees.json')
print(json_employees)



more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

first_three = more_employees.head(3)

last_two = more_employees.tail(2)

employee_shape = more_employees.shape

print(more_employees.info(verbose=False))

dirty_data = pd.read_csv('dirty_data.csv')
print(dirty_data)

clean_data = dirty_data.copy().drop_duplicates()
print('data cleaned')
print(clean_data)

clean_data['Age'] = pd.to_numeric(clean_data['Age'],errors = "coerce")

clean_data["Salary"] = clean_data["Salary"].replace("unknown", pd.NA)

clean_data['Salary'] = pd.to_numeric(clean_data['Salary'],errors = "coerce")
print('data even more cleaned ')
print(clean_data)

mean_score = clean_data['Age'].mean()
clean_data['Age'] = clean_data['Age'].fillna(mean_score)

median_score = clean_data['Salary'].median()
clean_data["Salary"] = clean_data["Salary"].fillna(median_score)

clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], format ='mixed', errors="coerce")

clean_data["Name"] = clean_data["Name"].str.strip().str.upper()

clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print('cleanest data ever')
print(clean_data)

