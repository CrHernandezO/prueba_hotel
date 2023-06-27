import fun_Hernández_Cristóbal as fn

while True:
    fn.time.sleep(3)
    fn.os.system('cls')
    print("Bienvenido a \"Mascota Segura\" \n")
    print("""Menú
        1.Grabar Mascota
        2.Buscar Mascota
        3.Retirar Mascota
        4.Salir
        """)
    opc=fn.validar_opcion()
    if opc==1:
        fn.validar_largo_rut()
        fn.validar_nombre_duenio()
        fn.identificador()
        fn.validar_nombre_mascota()
        fn.validar_dias()
        fn.ver_hotel()
        habitacion=fn.validar_habitacion()
        fn.verificar_habitaciones_disponibles(habitacion)
    elif opc==2:
        fn.buscar_mascota()
    elif opc==3:
        fn.retirar_mascota()
    elif opc==4:
        print("Gracias por Hospedarse en el Hotel \"Mascota Segura\"")