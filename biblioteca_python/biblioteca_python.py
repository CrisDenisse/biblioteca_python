import pickle

class Libro:
    """
    Clase para representar un libro en la biblioteca.

    Atributos:
    - titulo: El título del libro.
    - autor: El autor del libro.
    - cantidad: La cantidad de copias disponibles en la biblioteca.
    - disponible: Indica si el libro está disponible para préstamo.
    """
    def __init__(self, titulo, autor, cantidad=1):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad
        self.disponible = True

class Usuario:
    """
    Clase para representar un usuario de la biblioteca.

    Atributos:
    - nombre: El nombre del usuario.
    - libros_prestados: Lista de libros prestados al usuario.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

def agregar_libro(biblioteca, titulo, autor):
    """
    Agrega un libro a la biblioteca o incrementa su cantidad si ya existe.

    Parámetros:
    - biblioteca: Diccionario que contiene la información de la biblioteca.
    - titulo: El título del libro a agregar.
    - autor: El autor del libro a agregar.
    """
    for libro in biblioteca['libros']:
        if libro.titulo == titulo:
            libro.cantidad += 1
            break
    else:
        biblioteca['libros'].append(Libro(titulo, autor))
    print("Libro agregado exitosamente.")

def mostrar_libros(biblioteca):
    """
    Muestra la lista de libros en la biblioteca.
    
    Parámetros:
    - biblioteca: Diccionario que contiene la información de la biblioteca.
    """
    print("Lista de libros en la biblioteca:")
    for libro in biblioteca['libros']:
        disponibilidad = "Disponible" if libro.disponible else "No disponible"
        print(f"Título: {libro.titulo}, Autor: {libro.autor}, Cantidad: {libro.cantidad}, Disponibilidad: {disponibilidad}")

def prestar_libro(biblioteca, titulo_libro, nombre_usuario):
    """
    Permite prestar un libro a un usuario dado su título y nombre de usuario.
    
    Parámetros:
    - biblioteca: Diccionario que contiene la información de la biblioteca.
    - titulo_libro: El título del libro a prestar.
    - nombre_usuario: El nombre del usuario que quiere tomar prestado el libro.
    """
    for libro in biblioteca['libros']:
        if libro.titulo == titulo_libro:
            if libro.disponible and libro.cantidad > 0:
                for usuario in biblioteca['usuarios']:
                    if usuario.nombre == nombre_usuario:
                        usuario.libros_prestados.append(libro)
                        libro.cantidad -= 1
                        libro.disponible = False
                        print("Libro prestado exitosamente.")
                        return
                else:
                    print("Usuario no registrado.")
                    return
            else:
                print("El libro no está disponible en este momento.")
                return
    else:
        print("Libro no encontrado.")

def registrar_usuario(biblioteca, nombre):
    """
    Registra un usuario en la biblioteca.

    Parámetros:
    - biblioteca: Diccionario que contiene la información de la biblioteca.
    - nombre: El nombre del usuario a registrar.
    """
    for usuario in biblioteca['usuarios']:
        if usuario.nombre == nombre:
            print("El usuario ya está registrado.")
            return
    biblioteca['usuarios'].append(Usuario(nombre))
    print("Usuario registrado exitosamente.")

def guardar_datos(biblioteca):
    """
    Guarda los datos de la biblioteca en un archivo.

    Parámetros:
    - biblioteca: Diccionario que contiene la información de la biblioteca.
    """
    with open('datos_biblioteca.pkl', 'wb') as f:
        pickle.dump(biblioteca, f)
    print("Datos guardados correctamente.")

def cargar_datos():
    """
    Carga los datos previos de la biblioteca desde un archivo.

    Devuelve:
    - biblioteca: Diccionario que contiene la información de la biblioteca.
    """
    try:
        with open('datos_biblioteca.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {'libros': [], 'usuarios': []}

def listar_usuarios(biblioteca):
    """
    Muestra una lista de los usuarios registrados en la biblioteca.

    Parámetros:
    - biblioteca: Diccionario que contiene la información de la biblioteca.
    """
    print("Lista de usuarios registrados:")
    for usuario in biblioteca['usuarios']:
        print(usuario.nombre)

def listar_libros_usuario(biblioteca, nombre_usuario):
    """
    Muestra una lista de libros prestados a un usuario específico.

    Parámetros:
    - biblioteca: Diccionario que contiene la información de la biblioteca.
    - nombre_usuario: El nombre del usuario cuyos libros prestados se quieren listar.
    """
    for usuario in biblioteca['usuarios']:
        if usuario.nombre == nombre_usuario:
            if usuario.libros_prestados:
                print(f"Libros prestados a {nombre_usuario}:")
                for libro in usuario.libros_prestados:
                    print(libro.titulo)
            else:
                print(f"{nombre_usuario} no tiene libros prestados.")
            return
    else:
        print("Usuario no encontrado.")

def devolver_libro(biblioteca, titulo_libro, nombre_usuario):
    """
    Permite a un usuario devolver un libro prestado.

    Parámetros:
    - biblioteca: Diccionario que contiene la información de la biblioteca.
    - titulo_libro: El título del libro a devolver.
    - nombre_usuario: El nombre del usuario que quiere devolver el libro.
    """
    for usuario in biblioteca['usuarios']:
        if usuario.nombre == nombre_usuario:
            for libro in usuario.libros_prestados:
                if libro.titulo == titulo_libro:
                    usuario.libros_prestados.remove(libro)
                    for biblioteca_libro in biblioteca['libros']:
                        if biblioteca_libro.titulo == titulo_libro:
                            biblioteca_libro.cantidad += 1
                            biblioteca_libro.disponible = True
                            print("Libro devuelto exitosamente.")
                            return
                    else:
                        print("Error: libro no encontrado en la biblioteca.")
                        return
            else:
                print("Error: el usuario no tiene este libro prestado.")
                return
    else:
        print("Usuario no encontrado.")

def mostrar_menu():
    """
    Muestra el menú de opciones disponibles.
    """
    print("\n--- Menú ---")
    print("1. Agregar Libro")
    print("2. Mostrar Libros")
    print("3. Prestar Libro")
    print("4. Registrar Usuario")
    print("5. Listar Usuarios")
    print("6. Listar Libros de Usuario")
    print("7. Devolver Libro")
    print("8. Salir")

def main():
    """
    Función principal para ejecutar el sistema de gestión de biblioteca.
    """
    biblioteca = cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            agregar_libro(biblioteca, titulo, autor)
        elif opcion == "2":
            mostrar_libros(biblioteca)
        elif opcion == "3":
            titulo_libro = input("Ingrese el título del libro: ")
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            prestar_libro(biblioteca, titulo_libro, nombre_usuario)
        elif opcion == "4":
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            registrar_usuario(biblioteca, nombre_usuario)
        elif opcion == "5":
            listar_usuarios(biblioteca)
        elif opcion == "6":
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            listar_libros_usuario(biblioteca, nombre_usuario)
        elif opcion == "7":
            titulo_libro = input("Ingrese el título del libro: ")
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            devolver_libro(biblioteca, titulo_libro, nombre_usuario)
        elif opcion == "8":
            guardar_datos(biblioteca)
            print("¡Gracias por usar el sistema de gestión de biblioteca!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()