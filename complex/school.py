from pathlib import Path
from utils import catch_int, float_helper

data = {}
header = None
lines = Path('school_data.csv').read_bytes()


def get_score(clazz, trimester):
	return data[clazz][trimester-1]


def get_average(trimester):
	total = 0
	for key in data.keys():
		total += get_score(key, trimester)
	return total / len(data.keys())


for line in lines.decode().splitlines():
	line_data = line.split(';')
	if header is None:
		header = line_data
		continue
	data[line_data[0]] = [float_helper(x) for x in line_data[1:]]


def run():
	trimester_value = catch_int('Por favor, ingrese el trimestre que '
								'desea consultar', True)
	average = round(get_average(trimester_value or 1), 2)
	message = '\n > El promedio del trimestr "{}", es: {}\n'\
			  .format(trimester_value, average)
	print(message)


if __name__ == '__main__':
	run()
