import pandas as pd

data = pd.read_csv('faculty.csv')

email_list = []
for index, row in data.iterrows():
	s = row[' email']
	email_list.append(s)
df_emails = pd.DataFrame(email_list)
df_emails.to_csv('emails.csv', header=False, index=False)