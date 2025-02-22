def metros_a_kilometros(metros):
    return metros / 1000

def kilometros_a_metros(kilometros):
    return kilometros * 1000

def metros_a_millas(metros):
    return metros * 0.000621371

def millas_a_metros(millas):
    return millas / 0.000621371

def metros_a_pies(metros):
    return metros * 3.28084

def pies_a_metros(pies):
    return pies / 3.28084

# Función principal
def main():
    while True:
        print("\n--- Conversor de Unidades ---")
        print("1. Metros a Kilómetros")
        print("2. Kilómetros a Metros")
        print("3. Metros a Millas")
        print("4. Millas a Metros")
        print("5. Metros a Pies")
        print("6. Pies a Metros")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            metros = float(input("Ingrese la cantidad en metros: "))
            print(f"{metros} metros son {metros_a_kilometros(metros)} kilómetros")
        elif opcion == "2":
            kilometros = float(input("Ingrese la cantidad en kilómetros: "))
            print(f"{kilometros} kilómetros son {kilometros_a_metros(kilometros)} metros")
        elif opcion == "3":
            metros = float(input("Ingrese la cantidad en metros: "))
            print(f"{metros} metros son {metros_a_millas(metros)} millas")
        elif opcion == "4":
            millas = float(input("Ingrese la cantidad en millas: "))
            print(f"{millas} millas son {millas_a_metros(millas)} metros")
        elif opcion == "5":
            metros = float(input("Ingrese la cantidad en metros: "))
            print(f"{metros} metros son {metros_a_pies(metros)} pies")
        elif opcion == "6":
            pies = float(input("Ingrese la cantidad en pies: "))
            print(f"{pies} pies son {pies_a_metros(pies)} metros")
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
