
BASE_DIRECTIVO_ALTO = 3000000
BASE_DIRECTIVO_MEDIO = 2500000
BASE_OPERATIVO = 1750000
BASE_AUXILIAR = 1300000

def calcular_total_con_bonificacion(base_salario, tipo_puesto, nivel_rendimiento):
    bonificacion = 0
    descripcion_rendimiento = ""

    if tipo_puesto == "directivo":
        if nivel_rendimiento == 1:
            bonificacion = base_salario * 0.20
            descripcion_rendimiento = "Desempeño excelente"
        elif nivel_rendimiento == 2:
            bonificacion = base_salario * 0.10
            descripcion_rendimiento = "Desempeño medio"
    elif tipo_puesto == "operativo":
        if nivel_rendimiento == 1:
            bonificacion = base_salario * 0.15
            descripcion_rendimiento = "Desempeño alto"
        elif nivel_rendimiento == 2:
            bonificacion = base_salario * 0.05
            descripcion_rendimiento = "Desempeño medio"
    elif tipo_puesto == "auxiliar":
        descripcion_rendimiento = "Desempeño bajo "
    else:
        descripcion_rendimiento = " no válido"

    total_a_pagar = base_salario + bonificacion
    mostrar_resumen(base_salario, bonificacion, total_a_pagar, tipo_puesto, descripcion_rendimiento)

def mostrar_resumen(base_salario, bonificacion, total_a_pagar, tipo_puesto, descripcion_rendimiento):
    print("----- Detalle de Pago -----")
    print(f"Cargo: {tipo_puesto.capitalize()}")
    print(f"Descripción del Rendimiento: {descripcion_rendimiento}")
    print(f"Salario Base: ${base_salario}")
    print(f"Bonificación: ${bonificacion}")
    print(f"Total a Recibir: ${total_a_pagar}")
    print("---------------------------")

tipo_puesto = input("Digite el cargo (directivo, operativo, auxiliar): ").lower()

base_salario = 0
if tipo_puesto == "directivo":
    base_salario = int(input(f"Introduzca el salario base : "))
elif tipo_puesto == "operativo":
    base_salario = int(input(f"Introduzca el salario base : "))
elif tipo_puesto == "auxiliar":
    base_salario = int(input(f"Introduzca el salario base : "))
else:
    print("Cargo seleccionado no es válido")
    exit()

print("Elija el nivel de rendimiento:")
print("1. Alto")
print("2. Medio")
print("3. Bajo")
nivel_rendimiento = int(input("Digite el número correspondiente al rendimiento: "))

calcular_total_con_bonificacion(base_salario, tipo_puesto, nivel_rendimiento)
