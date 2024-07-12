
import random
import csv

trabajadores = [
    {"nombre": "Juan Perez", },
    {"nombre": "Maria Garcia", },
    {"nombre": "Carlos Lopez", },
    {"nombre": "Ana Martinez", },
    {"nombre": "Pedro Rodriguez", },
    {"nombre": "Laura Hernandez", },
    {"nombre": "Miguel Sanchez", },
    {"nombre": "Isabel Gomez", },
    {"nombre": "Francisco Diaz", },
    {"nombre": "Elena Fernandez", }
]

def asignar_sueldos():
    for empleado in trabajadores:
        empleado['sueldo'] = random.randint(300000, 2500000)

def clasificar_sueldos():
    menor = []
    entre = []
    mayor = []

    for empleado in trabajadores:
        sueldo = empleado.get('sueldo',0)
        if sueldo < 800000:
            menor.append(empleado)
        elif sueldo <= 2000000:
            entre.append(empleado)
        else:
            mayor.append(empleado)

    print("1. Sueldos menores a $800.000 TOTAL:", len(menor))
    print("2. Sueldos entre $800.000 y $2.000.000 TOTAL:", len(entre))
    print("3. Sueldos mayores a $2.000.000 TOTAL:", len(mayor))

    print("\nSueldos menores a $800.000")
    print("Nombre empleado\t\tSueldo")
    for emp in menor:
        print(f"{emp['nombre']}\t\t${emp['sueldo']}")

    print("\nSueldos entre $800.000 y $2.000.000")
    print("Nombre empleado\t\tSueldo")
    for emp in entre:
        print(f"{emp['nombre']}\t\t${emp['sueldo']}")

    print("\nSueldos mayores a $2.000.000")
    print("Nombre empleado\t\tSueldo")
    for emp in mayor:
        print(f"{emp['nombre']}\t\t${emp['sueldo']}")

def ver_estadisticas():
    total_sueldos = sum(emp['sueldo'] for emp in trabajadores)
    print(f"\nTOTAL SUELDOS: ${total_sueldos}")

    

def generar_reporte():
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido'])
        
        for emp in trabajadores:
            salud = emp['sueldo'] * 0.07
            afp = emp['sueldo'] * 0.12
            sueldo_liquido = emp['sueldo'] - salud - afp
            
            writer.writerow([emp['nombre'], emp['sueldo'], salud, afp, sueldo_liquido])

def main():
    print("Bienvenido al sistema de análisis de sueldos de Planing Solutions")
    while True:
        print("\nMENU:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            asignar_sueldos()
            print("Se han asignado sueldos aleatorios...")
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            generar_reporte()
            print("Reporte de sueldos generado en reporte_sueldos.csv")
        elif opcion == '5':
            print("Finalizando programa...")
            print("Desarrollado por Jose Romero")
            print("RUT 22.009.306-9")
            break
        else:
            print("Opción inválida. Debe seleccionar una opción entre 1 y 5.")

if __name__ == "__main__":
    main()
