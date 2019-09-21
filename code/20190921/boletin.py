from pathlib import Path

data = {}
header = None
filename = Path('data.csv')
filedata = filename.read_bytes()

# line: "Asignaturas;Trim 1;Trim 2;Trim 3"
for x in filedata.decode().splitlines():
    line = x.split(';')
    if header is None:
        header = line
        continue
    data[line[0]] = line[1:]

    
def promedio(trimestre):
    suma = 0
    for k, v in data.items():
        suma += float(v[trimestre-1].replace(',', '.'))
    print('trimestre', trimestre, 'promedio', suma / len(data.keys()))


promedio(1)
promedio(2)
