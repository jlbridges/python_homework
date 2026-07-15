import traceback
import os
import csv
import custom_module
from datetime import datetime


# task 2
def read_employees():
    empty_dict = {}
    empty_list = []

    try:
        with open("../csv/employees.csv", "r") as f:
            read_csv = csv.reader(f, delimiter=",")
            # print(type(read_csv))
            # print(dir(read_csv))
            empty_dict["fields"] = next(read_csv)
            for line in read_csv:
                empty_list.append(line)
            # print(empty_dict)
            # print(empty_list)
        empty_dict["rows"] = empty_list

        # id_index = empty_dict['fields'].index('employee_id')
        # print(empty_dict['rows'][0][name_index])
        # print(empty_dict['rows'][0][id_index])
        return empty_dict

    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")


employees = read_employees()


# task 3
def column_index(field):

    return employees["fields"].index(field)

#task 4
def first_name(row_num):
    column = column_index('first_name')
    return employees['rows'][row_num][column]
get_first_name = first_name(4)

print(get_first_name)


# task 5
def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches

#task 6
def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]
        )
    )
    return matches

# task 7
def sort_by_last_name():
    last_name_index = column_index("last_name")

    employees["rows"].sort(key=lambda row: (row[last_name_index]))

    return employees["rows"]

#task 8
def employee_dict(row):
    result = dict(zip(employees["fields"], row))
    del result["employee_id"]
    return result

# task 9
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        result[emp_id] = employee_dict(row)
    return result




# task 10
def get_this_value():
    return os.getenv("THISVALUE")

#task 11
def set_that_secret(new_secret):
    make_secret = custom_module.set_secret(new_secret)
    return make_secret
new_secret = set_that_secret('python rocks')
print(custom_module.secret)
#task 12
def get_minutes():
    minute_dicts = {}

    csv_directory = os.listdir("../csv")
    minutes_files = tuple([i for i in csv_directory if "minutes" in i])

    for file in minutes_files:
        with open(f"../csv/{file}") as f:
            minutes = {}
            read_csv = csv.reader(f, delimiter=",")

            minutes["fields"] = next(read_csv)
            minutes["rows"] = [tuple(line) for line in read_csv]

            minute_dicts[file] = minutes

    return minute_dicts

#task 12
def read_minutes():
    minutes = get_minutes()
    minutes1 = minutes["minutes1.csv"]
    minutes2 = minutes["minutes2.csv"]
    return minutes1, minutes2
#task 12
minutes1, minutes2 = read_minutes()



#task 13
def create_minutes_set():
    minutes1_set = set(minutes1["rows"])
    minutes2_set = set(minutes2["rows"])

    return minutes1_set.union(minutes2_set)
#task 13
minutes_set = create_minutes_set()

# task 14
def create_minutes_list():
    minute_list = list(
        map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set)
    )
    return minute_list
#task 14
minutes_list = create_minutes_list()


#task 15
def write_sorted_list():
    # Sort minutes_list in ascending order of datetime.
    sorted_list = sorted(minutes_list, key=lambda x: x[1])

    sorted_list_converted = list(map(lambda x:(x[0], str(datetime.strftime(x[1], "%B %d, %Y"))), sorted_list))

    try:
        with open('./minutes.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(minutes1['fields'])
            for item in sorted_list_converted:
                writer.writerow(item)
        return sorted_list_converted
    except Exception as e:
        print(e)

#task 3
employee_id_column = column_index("employee_id")




#task 15
write_sorted_list()