from pathlib import Path

header = None
filename = Path('data.csv')
filedata = filename.read_bytes()
data = {}

for x in filedata.decode().splitlines():
    #print(">", x.split(";"))
    line = x.split(';')

    if header is None:
        header = line
        continue

    data[line[0]] = line[1:]
    print(line, line[1:])


def promedio(trimestre):
    suma = 0
    for k, v in data.items():
        suma += float(v[trimestre-1].replace(',', '.'))
    print('trimestre', trimestre, 'promedio', suma / len(data.keys()))

promedio(1)
promedio(2)