import csv
import calendar

def change_date(date):
	weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	d = date.split('/')
	day = calendar.weekday(d[2],d[0],d[1])
	return day

def uber(filepath):
	with open(filepath, 'r', encoding='utf-8') as fp:
		for line in fp:
			f = line.strip().split(',')
			date = f[1]
			day = change_date(date)

			result = f"{f[0]},{day}  {f[2]},{f[3]}"
			print(result)


filepath = "./uber_exp.txt"
uber(filepath)