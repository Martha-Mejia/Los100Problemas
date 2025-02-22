# Definición de funciones para gestionar la agenda de contactos

def agregar_contacto(agenda, nombre, telefono, correo):
    contacto = {"Nombre": nombre, "Teléfono": telefono, "Correo": correo}
    agenda.append(contacto)

def mostrar_contactos(agenda):
    for i, contacto in enumerate(agenda, start=1):
        print(f"Contacto {i}:")
        print(f"Nombre: {contacto['Nombre']}")
        print(f"Teléfono: {contacto['Teléfono']}")
        print(f"Correo: {contacto['Correo']}")
        print()

def buscar_contacto(agenda, nombre):
    for contacto in agenda:
        if contacto['Nombre'].lower() == nombre.lower():
            print(f"Nombre: {contacto['Nombre']}")
            print(f"Teléfono: {contacto['Teléfono']}")
            print(f"Correo: {contacto['Correo']}")
            return
    print("Contacto no encontrado")

def eliminar_contacto(agenda, nombre):
    for contacto in agenda:
        if contacto['Nombre'].lower() == nombre.lower():
            agenda.remove(contacto)
            print("Contacto eliminado")
            return
    print("Contacto no encontrado")

# Función principal
def main():
    agenda = []
    while True:
        print("\n--- Agenda de Contactos ---")
        print("1. Agregar contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            agregar_contacto(agenda, nombre, telefono, correo)
        elif opcion == "2":
            mostrar_contactos(agenda)
        elif opcion == "3":
            nombre = input("Nombre del contacto a buscar: ")
            buscar_contacto(agenda, nombre)
        elif opcion == "4":
            nombre = input("Nombre del contacto a eliminar: ")
            eliminar_contacto(agenda, nombre)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
