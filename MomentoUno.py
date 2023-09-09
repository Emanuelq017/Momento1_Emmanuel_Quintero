
usuarios = []
ciclas = [ 
          ["015"],
          ["183"],
          ["123"],
          ["367"]]

prestamos = []



def RegistrarUsuarios():
    tarjet = input("Ingrese su numero de tarjeta: ")
    name = input("Ingrese su nombre: ")
    lastName = input("Ingrese su apellido: ")
    email = input("Ingrese su correo electronico: ")
    nuevoUsuario = [tarjet,name,lastName,email]
    usuarios.append(nuevoUsuario)
    print("Usuario registrado con exito")



def ListarCicla():
 for cicla in ciclas:
        print("")
        print(f"Serial de cicla: {cicla[0]}")


def PrestarCicla():
    print("")
    tarjet = input("Indique su numero de tarjeta: ")

    for i in range(0, len(usuarios)):
        user = usuarios[i]
        if tarjet in user:
            i = len(usuarios)
            marca = True
        else:
            marca = False
    if marca:
        print("*********************************")
        print("Seleccione la bibiclera de su interes")
        ListarCicla()
        print("")
        serial = input("Indique el serial de la cicla a elegir --> ")
        if serial == "015" or "183" or "123" or "367":
            print("")
            origen = input("Indique el origen de la cicla: ")
            destino = input("Indique el destino final de la cicla: ")
            nuevoPrestamo = [tarjet, serial, origen, destino]
            prestamos.append(nuevoPrestamo)
            print(prestamos)
            print(ciclas)
            lista_a_eliminar = [serial]
            ciclas.remove(lista_a_eliminar)
            print("Prestamo realizado exitosamente")
            print(ciclas)
            
    else:
        print("La tarjeta no esta registrada en el sistema")
    menu()


def ListarUsuarios():
    for usuario in usuarios:
        print(f"Tarjeta: {usuario[0]}")
        print(f"Nombre: {usuario[1]}")
        print(f"Apellido: {usuario[2]}")
        print(f"Email: {usuario[3]}")

def ListarPrestamos():
     
     for prestamo in prestamos:
        print(f"Tarjeta: {prestamo[0]}")
        print(f"serial: {prestamo[1]}")
        print(f"origen: {prestamo[2]}")
        print(f"destino: {prestamo[3]}")

def menu():
    i = 1
    while i == 1:
        print("")
        print("__________CICLAS POR LA CIUDAD__________")
        print("")
        print("digite 1 para registarse")
        print("digite 2 para Prestar una cicla")
        print("digite 3 para Listar los usuarios")
        print("digite 4 para Listar prestamos")
        print("digite 5 para salir")
        print("")
        opcion = input("---> ")
        print("")
        if opcion == "1":
            RegistrarUsuarios()
        elif opcion == "2":
            PrestarCicla()
        elif opcion == "3":
            ListarUsuarios()
        elif opcion == "4":
            ListarPrestamos()
        elif opcion == "5":
            i=0


menu()

