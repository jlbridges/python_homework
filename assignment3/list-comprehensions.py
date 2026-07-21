import csv
try:
    with open('../csv/employees.csv', 'r') as f:
        read_file = csv.reader(f)
        #print(list(read_file))
        next(read_file)
        # for line in list(read_file):
        #     print(line[1])
        names = [f'{line[1]} {line[2]}' for line in list(read_file)]
        print(names)
        new_names = [name for name in names if 'e' in name]
        print(new_names)
except FileNotFoundError:
    print('file not found')
