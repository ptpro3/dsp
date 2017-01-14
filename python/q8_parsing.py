import pandas

data = pandas.read_csv('football.csv')
data['Goals Diff'] = abs(data['Goals'] - data['Goals Allowed'])
print data[data['Goals Diff'] == min(data['Goals Diff'])]['Team']

# Aston_Villa