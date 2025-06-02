# Simulación de la carrera entre la tortuga y la liebre.
# Ambos comienzan en la posición 1 y deben avanzar hasta la meta en la posición 70.
# En cada segundo (tic del reloj), sus posiciones cambian según reglas aleatorias.
# Si se encuentran en la misma posición, se imprime "OUCH!!!".
# Gana el primero que llegue o supere la posición 70.

import random
import time

def mover_tortuga(opcion, posicion):
    if 1 <= opcion <= 5:
        posicion += 3
    elif 6 <= opcion <= 7:
        posicion -= 6
    elif 8 <= opcion <= 10:
        posicion += 1
    return max(1, min(posicion, 70))


def mover_liebre(opcion, posicion):
    if opcion in (3, 4):
        posicion += 9
    elif opcion == 5:
        posicion -= 12
    elif 6 <= opcion <= 8:
        posicion += 1
    elif 9 <= opcion <= 10:
        posicion -= 2
    return max(1, min(posicion, 70))


def imprimir_pista(tortuga, liebre):
    pista = ['_'] * 70
    if tortuga == liebre:
        pista[tortuga - 1] = 'OUCH!'
    else:
        pista[tortuga - 1] = 'T'
        pista[liebre - 1] = 'H'

    print("|", end="")
    for casilla in pista:
        print(f"{casilla}" if isinstance(casilla, str) else "_", end="")
    print("|")


def correr_carrera(num):
    tortuga = 1
    liebre = 1

    print(f"\n🏁 PUM!!!\nY ARRANCA LA CARRERA {num}!!!\n")
    print(f"POSICIÓN INICIAL TORTUGA: {tortuga}")
    print(f"POSICIÓN INICIAL LIEBRE: {liebre}\n")

    for _ in range(60):
        reloj = random.randint(1, 10)
        print(f"Ajustar las posiciones en {reloj} para ambos!")

        tortuga = mover_tortuga(reloj, tortuga)
        liebre = mover_liebre(reloj, liebre)

        imprimir_pista(tortuga, liebre)
        print()
        time.sleep(0.3)

        if tortuga >= 70 or liebre >= 70:
            break

    if tortuga >= 70 and liebre >= 70:
        print("🏁 Es un empate!!!")
    elif tortuga >= 70:
        print("🐢 LA TORTUGA GANA!!! YAY!!!")
    elif liebre >= 70:
        print("🐇 La Liebre gana. ¡Qué mal!")


def menu_principal():
    carrera_num = 1
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Iniciar nueva carrera")
        print("2. Salir")
        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            correr_carrera(carrera_num)
            carrera_num += 1
        elif opcion == "2":
            print("¡Gracias por jugar! 🏁")
            break
        else:
            print("Opción no válida. Intentalo de nuevo.")


if __name__ == "__main__":
    menu_principal()
