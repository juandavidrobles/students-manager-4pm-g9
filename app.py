import funciones

estudiantes = funciones.cargar_estudiantes()

while True:

  seleccion = funciones.mostrar_menu_y_obtener_seleccion()

  if seleccion == "1":
    funciones.mostrar_numero_estudiantes(estudiantes)

  elif seleccion == "2":
    estudiante = funciones.crear_estudiante()
    estudiantes.append(estudiante)
    funciones.actualizar_data_estudiantes(estudiantes)
    print("Estudiante añadido exitosamente.")

  elif seleccion == "3":
    nombreABuscar = input('Ingrese el nombre del estudiante a buscar')
    estudianteEncontrado = funciones.buscar_estudiante_por_nombre(nombreABuscar, estudiantes)
    if estudianteEncontrado == None:
      print("El nombre ingresado no se encuentra en la base de datos.")
    else:
      print(estudianteEncontrado)

  elif seleccion == "4":
    respuesta = None
    while respuesta != "y":
      documentoAEliminar = input("Documento del estudiante a eliminar: ")
      estudianteAEliminar = funciones.buscar_estudiante_por_documento(documentoAEliminar, estudiantes)
      if (estudianteAEliminar == None):
        print('Estudiante no encontrado')
      else:
        respuesta = input("¿Este es el usuario que desea eliminar? (y/n)")
        if respuesta == "y":
          estudiantes.remove(estudianteAEliminar)
          funciones.actualizar_data_estudiantes(estudiantes)
          print("Estudiante eliminado con éxito.")
          # break
  elif seleccion == '5':
    print(funciones.buscar_estudiante_por_documento(input('documento a buscar:'), estudiantes) or 'Estudiante no encontrado')
  elif seleccion == '6':
    print('Hasta luego')
    break
   
