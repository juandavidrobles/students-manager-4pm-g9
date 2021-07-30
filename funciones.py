def mostrar_menu_y_obtener_seleccion():
  print("\n")
  print("                     Menú principal")
  print("\n   1. Mostrar cuantos estudiantes hay en la base de datos")
  print("\n              2. Agregar un nuevo estudiante")
  print("\n             3. Buscar un estudiante por nombre")
  print("\n    4. Eliminar un estudiante por número de documento")
  print("\n          5. Buscar un estudiante por documento    ")
  print("\n                    6. Salir    ")
  seleccion = input("\n    Ingresa tu seleccion: ")
  return seleccion

def mostrar_numero_estudiantes(estudiantes):
  if len(estudiantes) == 0:
    print("La lista de estudiantes esta vacia")
  else:
    print("El numero de estudiantes en la lista es de: ", len(estudiantes))

def crear_estudiante():
  nombre = input("Digita un nombre: ")
  apellido = input("Digita el apellido: ")
  documento = input("Digita el documento: ")
  sexo = input("Digita el sexo: ")
  estudiante = {"nombre":nombre, "apellido":apellido, "documento":documento, "sexo":sexo}
  return estudiante

def buscar_estudiante_por_nombre(nombre_a_buscar, estudiantes):

  for estudiante in estudiantes:
    if estudiante["nombre"].lower() == nombre_a_buscar.lower():
      return estudiante

def buscar_estudiante_por_documento(documento_a_buscar, estudiantes):
  for estudiante in estudiantes:
    if (estudiante['documento'] == documento_a_buscar):
      return estudiante