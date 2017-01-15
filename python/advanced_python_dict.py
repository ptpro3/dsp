import pandas
import re

data = pandas.read_csv('faculty.csv')

faculty_dict = {}
for index, row in data.iterrows():
	name_string = row['name']
	name_list = name_string.split()
	last_name = name_list[-1]
	info_list = [row[' degree'], row[' title'], row[' email']]
	if last_name in faculty_dict:
		faculty_dict[last_name].append(info_list)
	else:
		faculty_dict[last_name] = info_list
# print sorted(faculty_dict.items())[0:3]

professor_dict = {}
for index, row in data.iterrows():
	name_string = row['name']
	name_list = name_string.split()
	name = (name_list[0], name_list[-1])
	professor_dict[name] = [row[' degree'], row[' title'], row[' email']]
# print sorted(professor_dict.items())[0:3]

print sorted(professor_dict.items(), key = lambda x: x[0][1])[0:3]