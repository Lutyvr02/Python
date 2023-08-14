estudiantes = [
    {
        'nombre': 'juan',
        'apellido': 'perez',
        'notas': {
            'MAT': 30,
            'QMC': 30,
            'FIS': 30,
            'LAB': 30
        },
        'extras': [2, 3, 1, 1, 1],
        'asistencia': 90
    },
    {
        'nombre': 'ana',
        'apellido': 'rivera',
        'notas': {
            'MAT': 98,
            'QMC': 98,
            'FIS': 98,
            'LAB': 98
        },
        'extras': [1],
        'asistencia': 100
    }
]


class Evaluador:
    def __init__(self, lista_estudiantes, min_asistencia, max_extras):
        self.lista_estudiantes = lista_estudiantes
        self.min_asistencia = min_asistencia
        self.max_extras = max_extras

    def calcular_promedios(self):
        lista_notas = []

        for estudiante in self.lista_estudiantes:
            nombre_completo = f"{estudiante['nombre'].capitalize()} {estudiante['apellido'].capitalize()}"
            notas = estudiante.get('notas', {})
            asistencia = estudiante.get('asistencia', 0)
            extras = sum(estudiante.get('extras', []))
            
            if not notas or asistencia < self.min_asistencia:
                promedio_final = 0
            else:
                promedio_final = sum(notas.values()) / len(notas)
                promedio_final = min(promedio_final + extras, 100)
            
            lista_notas.append({'nombre completo': nombre_completo, 'promedio': promedio_final})
        
        return lista_notas

    def obtener_mejor_estudiante(self):
        mejor_estudiante = None

        for estudiante in self.lista_estudiantes:
            nombre_completo = f"{estudiante['nombre'].capitalize()} {estudiante['apellido'].capitalize()}"
            notas = estudiante.get('notas', {})
            asistencia = estudiante.get('asistencia', 0)
            extras = sum(estudiante.get('extras', []))

            if not notas or asistencia < self.min_asistencia:
                continue
            
            promedio_final = sum(notas.values()) / len(notas)
            promedio_final = min(promedio_final + extras, 100)
            
            if mejor_estudiante is None or promedio_final > mejor_estudiante['promedio']:
                mejor_estudiante = {'nombre completo': nombre_completo, 'promedio': promedio_final}
        
        return mejor_estudiante

    def salvar_datos(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("Nombre Completo|Asistencia|MAT|FIS|QMC|LAB|Total Extras|Promedio Final|Observación\n")
            
            for estudiante in self.lista_estudiantes:
                nombre_completo = f"{estudiante['nombre'].capitalize()} {estudiante['apellido'].capitalize()}"
                notas = estudiante.get('notas', {})
                asistencia = estudiante.get('asistencia', 0)
                extras = sum(estudiante.get('extras', []))
                
                if not notas or asistencia < self.min_asistencia:
                    promedio_final = 0
                    observacion = "REPROBADO"
                else:
                    promedio_final = sum(notas.values()) / len(notas)
                    promedio_final = min(promedio_final + extras, 100)
                    observacion = "APROBADO" if promedio_final > 50 else "REPROBADO"
                
                archivo.write(f"{nombre_completo}|{asistencia}|{notas.get('MAT', 0)}|{notas.get('FIS', 0)}|{notas.get('QMC', 0)}|{notas.get('LAB', 0)}|{extras}|{promedio_final:.2f}|{observacion}\n")

        print(f'Datos guardados en el archivo {nombre_archivo}')    


# -----------------------------------------#
# ----> NO MODIFICAR DESDE AQUI! <---------#
# -----------------------------------------#
def comparar_archivo_notas(archivo):
    with open('notas.csv', 'r') as archivo_correcto:
        correcto_str = archivo_correcto.read()

    with open(archivo, 'r') as archivo:
        archivo_str = archivo.read()

    return correcto_str == archivo_str


if __name__ == '__main__':
    # datos iniciales
    nombre_archivo = 'notas.csv'
    notas_correcto = [{'nombre completo': 'Juan Perez', 'promedio': 35.0}, {'nombre completo': 'Ana Rivera', 'promedio': 99.0}]
    mejor_correcto = {'nombre completo': 'Ana Rivera', 'promedio': 99.0}

    # Instanciar evaluador
    evaluador = Evaluador(lista_estudiantes=estudiantes, min_asistencia=80, max_extras=5)
    # calcular promedios
    notas = evaluador.calcular_promedios()
    print(f'calcular_promedios: {notas}')
    if notas == notas_correcto:
        print('Calculo de promedios correcto!')
    else:
        print(f'ERROR, lista de promedios esperada: {notas_correcto}')
    # obtener mejor estudiante
    mejor = evaluador.obtener_mejor_estudiante()
    print(f'obtener_mejor_estudiante: {mejor}')
    if mejor == mejor_correcto:
        print('Mejor estudiante correcto!')
    else:
        print(f'ERROR, mejor estudiante esperado: {mejor_correcto}')
    # salvar datos en archivo
    evaluador.salvar_datos(nombre_archivo)
    if comparar_archivo_notas(nombre_archivo):
        print('Generacion de archivo correcta')
    else:
        print('Generacion de archivos incorrecta, ver archivo "ejemplo_notas.csv"')
