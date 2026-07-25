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