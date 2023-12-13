# Se crea un diccionario vacío llamado 'agenda' para almacenar los contactos.
agenda = {}

# Se inicia un bucle infinito para mostrar el menú de la agenda de forma continua.
while True:
    # Se imprime el menú de la agenda.
    print("----- AGENDA -----")
    print("1. Agregar/Cambiar")
    print("2. Buscar")
    print("3. Eliminar")
    print("4. Mostrar ítems")
    print("5. Salir")
    print("------------------")

    # Se solicita al usuario que seleccione una opción del menú.
    opcion = input("Seleccione una opción: ")

    # Si el usuario selecciona la opción 1...
    if opcion == "1":
        # Se solicita al usuario que ingrese el nombre del contacto y su número de teléfono.
        nombre = input("Ingrese el nombre del compañero: ")
        telefono = input("Ingrese el número de teléfono: ")

        # Si el nombre ya existe en la agenda...
        if nombre in agenda:
            # Se informa al usuario que el nombre ya existe y se muestra el número de teléfono actual.
            print("El nombre ya existe en la agenda.")
            print("Teléfono:", agenda[nombre])
            # Se pregunta al usuario si desea cambiar el número de teléfono.
            cambiar = input("¿Desea cambiar el número de teléfono? (s/n): ")

            # Si el usuario desea cambiar el número de teléfono...
            if cambiar.lower() == "s":
                # Se cambia el número de teléfono en la agenda.
                agenda[nombre] = telefono
                # Se informa al usuario que el número de teléfono ha sido cambiado.
                print("Número de teléfono cambiado exitosamente.")
        # Si el nombre no existe en la agenda...
        else:
            # Se agrega el nuevo contacto a la agenda.
            agenda[nombre] = telefono
            # Se informa al usuario que el contacto ha sido agregado.
            print("Contacto agregado exitosamente.")

    # Si el usuario selecciona la opción 2...
    elif opcion == "2":
        # Se solicita al usuario que ingrese una cadena de caracteres para la búsqueda.
        cadena = input("Ingrese una cadena de caracteres: ")
        # Se informa al usuario que se buscarán los contactos que coincidan con la cadena.
        print("Contactos que coinciden con la cadena:", cadena)
        # Se buscan los contactos cuyo nombre comienza con la cadena ingresada y se muestran.
        for nombre, telefono in agenda.items():
            if nombre.startswith(cadena):
                print(nombre, "-", telefono)

    # Si el usuario selecciona la opción 3...
    elif opcion == "3":
        # Se solicita al usuario que ingrese el nombre del contacto a eliminar.
        nombre = input("Ingrese el nombre del compañero: ")
        # Si el nombre existe en la agenda...
        if nombre in agenda:
            # Se pregunta al usuario si desea eliminar el contacto.
            eliminar = input("¿Desea eliminar este contacto? (s/n): ")
            # Si el usuario desea eliminar el contacto...
            if eliminar.lower() == "s":
                # Se elimina el contacto de la agenda.
                del agenda[nombre]
                # Se informa al usuario que el contacto ha sido eliminado.
                print("Contacto eliminado exitosamente.")
        # Si el nombre no existe en la agenda...
        else:
            # Se informa al usuario que el nombre no existe.
            print("El nombre no existe en la agenda.")

    # Si el usuario selecciona la opción 4...
    elif opcion == "4":
        # Se informa al usuario que se mostrarán todos los contactos.
        print("----- CONTACTOS -----")
        # Se muestran todos los contactos en la agenda.
        for nombre, telefono in agenda.items():
            print(nombre, "-", telefono)
        print("---------------------")

    # Si el usuario selecciona la opción 5...
    elif opcion == "5":
        # Se  cerrará y se termina el bucle.
        print("Agenda cerrada.")
        break

    # Si el usuario selecciona una opción inválida...
    else:
        # Se informa al usuario que la opción es inválida y se le pide que seleccione una opción válida.
        print("Opción inválida. Por favor seleccione una opción válida.")