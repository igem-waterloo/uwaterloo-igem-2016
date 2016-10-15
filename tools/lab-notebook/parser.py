from dateutil.parser import parse
import json

with open('task_list.txt', 'r') as f:
	data = [line.split('\t')for line in f.read().split('\n')]

parsed_data = {}
day = ''

for line in data:
	if '2016' in line[0]:
		day = parse(' '.join(line[0].split(' ')[1:]))
		day = day.strftime('%b') + str(day.day)
		parsed_data[day] = []
	elif ':00' in line[0]:
		parsed_data[day].append(line[4])

with open('tasks.json', 'w') as f:
	f.write('var notes = ' + json.dumps(parsed_data))



