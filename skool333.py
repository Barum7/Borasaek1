class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []
        self.asistencia = 0
    
    def agregar_nota(self, nota):
        self.notas.append(nota)
    
    def agregar_asistencia(self, asistencia):
        self.asistencia = asistencia
    
    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        promedio = sum(self.notas) / len(self.notas)
        return promedio
    
    def determinar_estado(self):
        if self.calcular_promedio() >= 3 and self.asistencia >= 25:
            return "Aprobado"
        else:
            return "Desaprobado"
    
    def sugerir_plan_accion(self):
        if self.calcular_promedio() < 3:
            return "Mejorar notass"
        elif self.asistencia < 25:
            return "Asistir más a clases"
        else:
            return "Mantener la trayectoria"

nombre = input("Ingrese el nombre del estudiante: ")
asistencia = float(input("Ingrese la asistencia del estudiante (escala de 0 a 50): "))
cantidad_notas = int(input("Ingrese la cantidad de notas que desea asignar al estudiante: "))


estudiante = Estudiante(nombre)

for i in range(cantidad_notas):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    estudiante.agregar_nota(nota)

estudiante.agregar_asistencia(asistencia)

print("\nInformación del Estudiante:")
print("Nombre:", estudiante.nombre)
print("Notas:", estudiante.notas)
print("Promedio:", estudiante.calcular_promedio())
print("Asistencia:", estudiante.asistencia)
print("Estado:", estudiante.determinar_estado())
print("Plan de acción:", estudiante.sugerir_plan_accion())