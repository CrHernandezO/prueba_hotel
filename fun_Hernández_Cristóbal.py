import os
import time
import numpy
#recuerda instalar el numpy
hotel = numpy.zeros((2,5),int)
lista_identificador=[]
lista_nombred=[]
lista_nombrem=[]
lista_rut=[]
lista_habitacion=[]
lista_dias=[]

def validar_opcion():
    while True:
        global contadorid
        contadorid=0
        contadorid+=1
        try:
            opc= int(input("Escoga una opción del Menú (1-4): "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("ERROR! Escoga una opción correcta")
        except:
            print("ERROR! La opción debe ser un número entero")

def ver_hotel():
    contador = 1
    print("Habitaciónes")
    for x in range(2):
        print(f"Fila{(x+1)}: ",end=" ")
        for y in range(5):
            print(f"Habitación {contador}: {hotel[x][y]} ", end=" ")
            contador += 1
        print("\n")

def identificador():
    print(f"Su identificador es: {contadorid}")
    lista_identificador.append(contadorid)

def validar_habitacion():
    while True:
        try:
            habitacion= int(input("Escoga una Habitación (1-10): "))
            if habitacion in(1,2,3,4,5,6,7,8,9,10):
                lista_habitacion.append(habitacion)
                return habitacion
            else:
                print("ERROR! Escoga una Habitación correcta")
        except:
            print("ERROR! La opciín debe ser un número entero")
def verificar_habitaciones_disponibles(habitacion):
    contador= 1
    for x in range(2):
        for y in range(5):
            if hotel[x][y] == 0:
                if habitacion >= 1 and habitacion<=10:
                    lista_habitacion.append(contador)
            contador+= 1
        return habitacion

def validar_dias():
    while True:
        try:
            dias = int(input("Ingrese número de días: "))
            if dias >=1:
                lista_dias.append(dias)
                return dias
            else:
                print("ERROR! NÚMERO DE DÍAS NO DISPONIBLE!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_largo_rut():
    while True:
        try:
            rut=int(input("Ingrese rut (sin puntos ni dígito verificador): "))
            if len(str(rut))>=7 and len(str(rut))<=8:
                lista_rut.append(rut)
                return rut
            else:
                print("Ingrese rut de un largo de 7 o 8 digitos")
        except:
            print("ERROR! INGRESE NUMERO ENTERO")
        

def validar_nombre_duenio():
    while True:
        nombred = input("Ingrese nombre del dueño: ")
        if len(nombred.strip()) >= 3 and nombred.isalpha():
            lista_nombred.append(nombred)
            return nombred
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_nombre_mascota():
    while True:
        nombrem = input("Ingrese nombre de la Mascota: ")
        if len(nombrem.strip()) >= 3 and nombrem.isalpha():
            lista_nombrem.append(nombrem)
            return nombrem
        else:
            print("ERROR! NOMBRE DE LA MASCOTA TIENE QUE TENER 3 O MÁS LETRAS")
     
def validar_cantidad_prod():
    while True:
        try:
            can = int(input("Ingrese cantidad: "))
            if can >= 0:
                return can
            else:
                print("ERROR! CANTIDAD DEBE SER 0 O POSITIVA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def buscar_mascota():
    rut=validar_largo_rut()
    if rut in lista_rut:
        for x in range(len(lista_rut)):
            if len(lista_rut) == x:
                posicion = x
            print(lista_habitacion(posicion))
            print(lista_nombred(posicion))
            print(lista_nombrem(posicion))
            print(lista_rut(posicion))

    else:
        print("SU RUT NO ES VALIDO")
def retirar_mascota():
    rut=validar_largo_rut()
    if rut in lista_rut:
        for x in range(len(lista_rut)):
            if len(lista_rut) == x:
                posicion = x
                print("SU TOTAL A PAGAR ES:",lista_dias(posicion,posicion*15000))
            break
    else:
        print("SU RUT NO ES VALIDO")