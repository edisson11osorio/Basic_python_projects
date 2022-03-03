 #!/usr/bin/python3
import random


def adivina_el_numero_computadora(x):
    print(f"seleciona un numero entre 1 y {x} para que la computadora lo intente divinar ")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior

        respuesta = input(f"mi prediccion es {prediccion}. si es muy alta seleccione (A). si es muy baja selccione (B). si es correcta selecione (C)").lower()

        if respuesta == "a":
            limite_superior = prediccion -1
        elif respuesta == "b":
            limite_inferior = prediccion +1

    print(f"!siiiii la computadora adivino el numero correctamente {prediccion}")


adivina_el_numero_computadora(10)
            
