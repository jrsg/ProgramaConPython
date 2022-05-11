import csv

with open('calificaciones.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lineas = 0
    for row in csv_reader:
        if lineas == 0:
            print('Columnas:' ", ".join(row))
        else:
            print('Datos:', row[0], row[1], row[2])

        lineas += 1
        print('Líneas procesadas', lineas)
