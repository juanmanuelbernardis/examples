
# dependencias
import argparse
from pathlib import Path
from utils import catch_int, float_helper

# diccionario em el cual persistiremos los datos cargados desde el archivo.
data = {}


def get_score(clazz, trimester):
	"""Función que devuelve el valor de una asignatura para un trimestre
	   determinado."""
	return data[clazz][trimester-1]


def get_average(trimester, verbose=False):
	"""Funcción que cálcula el promedio de un trimestre determinado."""

	def _verbose(message):
		"""Función que imprime en pantalla si el modo verbose está activo."""
		if verbose is True:
			print(message)

	# total acumulado de notas.
	total = 0

	# total de asignaturas.
	total_clazz = len(data.keys())

	# si el argumento `verbose` es `True`, imprimimos el titulo de las 
	# asignaturas.
	_verbose('\nAsignaturas:')

	# recorremos las asignatura.
	for key in data.keys():
		# calculamos el valor de la asignatura.
		score = get_score(key, trimester)

		# si el argumento `verbose` es `True`, imprimimos los datos de la
		# asignatura.
		_verbose('- {} {} {}'.format(key, '.' * (32 - len(key)), score))

		# sumamos el valor de la asignatura al acumulado.
		total += score

	# si el argumento `verbose` es `True`, imprimimos el valor acumulados de 
	# las asignaturas.
	_verbose('--')
	_verbose(' Total de {} puntos sobre {} materia(s).'
		     .format(total, total_clazz))

	# calculamos el promedio y lo retornamos.
	return total / total_clazz


def read_file(filename=None):
	"""Función que lee el archivo utilizado como base de datos."""

	# cabecera del archivo.
	header = None

	# leemos el contenido del archivo en bytes.
	lines = Path(filename or 'school_data.csv').read_bytes()

	# recorremos las líneas del archivos, previa decodificación del mismo de
	# bytes a string.
	for line in lines.decode().splitlines():
		# convertimos el string en una lista, usando el caracter `;` como
		# separador.
		line_data = line.split(';')

		# si la variable `header` es igual a `None`, le asignamos el valor de
		# la primer línea y continuamos.
		if header is None:
			header = line_data
			continue

		# agregamos al diccionario las asignaturas, donde la clave es el nombre
		# de la asignatura y el valor una lista con las notas de cada trimestre.
		data[line_data[0]] = [float_helper(x) for x in line_data[1:]]


def run(args):
	"""Función que inicia el programa."""

	# verificamos si existe el argumento `trimester`, de no existir solicitamos
	# el ingreso del mismo.
	if args.trimester is None:
		trimester_value = catch_int('Por favor, ingrese el trimestre que '
									'desea consultar', True)
	else:
		trimester_value = args.trimester

	# establecemos un limite sobre la cantidad de los trimestres.
	trimester_value = max(min(trimester_value, 3), 1)

	try:
		# leemos el archivo `school_data.csv` y lo cargamos dentro de la
		# variable `data`, la cual se comporta cómo un diccionario.
		read_file(args.filename)

		# calculamos el promedio.
		average = round(get_average(trimester_value, args.verbose), 2)

		# definimos el mensaje de salida.
		message = '\n > El promedio del trimestre "{}", es: {} pts.\n'\
			      .format(trimester_value, average)

	except Exception as e:
		# en caso de que se produzca un error, lo capturamos y definimos el
		# mensaje de salida.
		message = 'Se produjo un error no controlado: %s' % str(e)

	# imprimimos el mensaje de salida en pantalla.
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

	# definimos la lista de argumentos que puede recibir el programa.
	parser = argparse.ArgumentParser()
	parser.add_argument('trimester', type=str,
						help='Trimestre a calcular.')
	parser.add_argument('-f', '--filename', type=str, default=None,
						help='Archivo a cargar.')
	parser.add_argument('-v', '--verbose', action='store_true',
						help='Muestra la lista de asignaturas.')

	# capturamos los argumentos.
	args = parser.parse_args()

	# verificamos el modo de impresión e iniciamos el programa.
	if args.trimester == "all":
		# anulamos el modo `verbose`.
		args.verbose = False

		# mostramos todos los trimestres.
		for t in range(1, 4):
			# ingresamos el valor del trimeste
			args.trimester = t

			# mostramos el trimestre ingresado.
			run(args)
			
	else:
		# convertimos el string a un integer
		args.trimester = int(args.trimester)

		# mostramos el trimestre ingresado.
		run(args)
