 #!/usr/bin/python3
import random  #modulo ramdom 

def adivina_el_numero(x): # Funcion 
 
    # Mensage de bienvenida
    print("===================")
    print("Bienvenido al juego")
    print("===================")

    numero_aleatorio = random.randint(1, x) # Numero aletatorio generado entre 1 y x 

    prediccion = 0

    while prediccion != numero_aleatorio:
        # El usuario ingresa un numero
        prediccion = int(input(f"adivina el numero entre 1 y {x}: ")) #f-string

        if prediccion < numero_aleatorio:
            print("el numero es muy pequeño ")
        elif prediccion > numero_aleatorio:
            print("el numero es demaciado grande ")
    print(f"!felicidades adivinaste el numero {numero_aleatorio} correctamente ") #f-string


adivina_el_numero(15) #Llamar a la funcion