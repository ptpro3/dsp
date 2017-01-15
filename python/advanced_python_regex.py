import pandas
import re

data = pandas.read_csv('faculty.csv')

degree_dict = {}
for index, row in data.iterrows():
	s_read = re.sub('[\d]','',row[' degree'])
	degree_list = s_read.split()
	for s in degree_list:
		key = re.sub('[\W]','',s)
		if key in degree_dict:
			degree_dict[key] += 1
		else:
			degree_dict[key] = 1
print degree_dict

title_dict = {}
for index, row in data.iterrows():
	s = row[' title']
#	for s in title_list:
#		key = re.sub('[\W]','',s)
	if s in title_dict:
		title_dict[s] += 1
	else:
		title_dict[s] = 1
print title_dict

email_list = []
for index, row in data.iterrows():
	s = row[' email']
	email_list.append(s)
print email_list

email_dict = {}
for email in email_list:
	email_break = email.split('@')
	email_domain = email_break[1]
	if email_domain in email_dict:
		email_dict[email_domain] += 1
	else:
		email_dict[email_domain] = 1
print email_dict