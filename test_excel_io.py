#test opening csv file

import csv

with open('Exercise_data.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
       # print row
       class_name = row[0]
       class_type = row[1]
       class_level = row[2]
       class_name + " " + class_type + " " +class_level

# parsing_list = []

# with open("Exercise_data.txt") as my_file:
#     for line in my_file:
#         print line


# for line in my_file:
#     parsing_list.append(line)

#print parsing_list



# from openpyxl import *

# wb = open_workbook('Exercise_data.xls')
# for sheet in wb.sheets():
#     number_of_rows = sheet.nrows
#     number_of_columns = sheet.ncols

#     items = []

#     rows = []
#     for row in range(1, number_of_rows):
#         values = []
#         for col in range(number_of_columns):
#             value  = (sheet.cell(row,col).value)
#             try:
#                 value = str(int(value))
#             except ValueError:
#                 pass
#             finally:
#                 values.append(value)
#         item = Arm(*values)
#         items.append(item)

# for item in items:
#     print item

