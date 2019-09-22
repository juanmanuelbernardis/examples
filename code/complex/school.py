import argparse
from pathlib import Path
from utils import catch_int, float_helper

data = {}


def get_score(clazz, trimester):
	return data[clazz][trimester-1]


def get_average(trimester, view=False):
	total = 0
	total_clazz = len(data.keys())
	for key in data.keys():
		score = get_score(key, trimester)
		if view is True:
			print(' - {}: {}'.format(key, score))
		total += score
	if view is True:
		print(' Total: {} de {} materias.'.format(total, total_clazz))
	return total / total_clazz


def get_clazz(clazz):
	value = data[clazz]
	print(clazz, '=>', ', '.join([str(x) for x in value]))


def read_file(filename=None):
	header = None
	lines = Path(filename or 'school_data.csv').read_bytes()
	for line in lines.decode().splitlines():
		line_data = line.split(';')
		if header is None:
			header = line_data
			continue
		data[line_data[0]] = [float_helper(x) for x in line_data[1:]]


def run(args):
	if not args.trimester:
		trimester_value = catch_int('Por favor, ingrese el trimestre que '
									'desea consultar', True)
	else:
		trimester_value = args.trimester
	try:
		read_file(args.filename)
		average = round(get_average(trimester_value, args.verbose), 2)
		message = '\n > El promedio del trimestre "{}", es: {}\n'\
			      .format(trimester_value, average)
	except Exception as e:
		message = 'Se produjo un error no controlado: %s' % str(e)
	print(message)


if __name__ == '__main__':
	"""
	Algunas formas de ejecutar el programa:
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	> python3 school.py -h
	> python3 school.py -v
	> python3 school.py -v -t 1
	> python3 school.py -v -t 1 -f ../data.csv
	> python3 school.py -t 2 -f ../data.csv	
	> python3 school.py -f ../data.csv	
	"""
	
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--trimester', type=int, default=None,
						help='Trimestre a calcular.')
	parser.add_argument('-f', '--filename', type=str, default=None,
						help='Archivo a cargar.')
	parser.add_argument('-v', '--verbose', action='store_true',
						help='Muestra la lista de asignaturas.')

	args = parser.parse_args()
	run(args)
