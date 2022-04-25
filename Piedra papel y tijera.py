jugador1= ""
print("Bienvenido a Piedra, Papel y Tijeras: ")

print(" jugador 1 Escoje una opción: ")
print("1) para piedra")
print("2) para papel")
print("3) para tijera")
opcion = int(input("Jugador 1 elige una opción "))

if opcion == 1:
    elijeusuario1 = "Piedra"
elif opcion == 2:
    elijeusuario1 = "Papel"
elif opcion == 3:
    elijeusuario1 = "Tijera"
print("Usuario 1 elegiste: ", elijeusuario1)

jugador2 = ""
print("Es turno del Jugador 2")

print(" jugador 2 Escoje una opción: ")
print("1) para piedra")
print("2) para papel")
print("3) para tijera")
opcion2 = int(input("Jugador 1 elige una opción "))

if opcion2 == 1:
    elijeusuario2 = "Piedra"
elif opcion2 == 2:
    elijeusuario2 = "Papel"
elif opcion2 == 3:
    elijeusuario2 = "Tijera"
print("Usuario 2 elegiste: ", elijeusuario2)

print("Calculando...")
if elijeusuario1 == "Piedra" and elijeusuario2 == "Papel":
    print ("Felicidades, ganaste Jugador 2 Papel envuelve piedra")
elif elijeusuario1 == "Papel" and elijeusuario2 == "Tijera":
    print ("Felicidades, ganaste jugador 2, la tijera corta el papel")
elif elijeusuario1 == "Tijera" and elijeusuario2 == "Piedra":
    print ("Felicidades, ganaste jugador 2, la piedra rompe la tijera")
elif elijeusuario1 == "Papel" and elijeusuario2 == "Piedra":
    print("Felicidades, ganaste Jugador 1 Papel envuelve piedra")
elif elijeusuario1 == "Tijera" and elijeusuario2 == "Papel":
    print("Felicidades, ganaste Jugador 1 la tijera corta el papel")
elif elijeusuario1 == "Piedra" and elijeusuario2 == "Tijera":
    print("Felicidades, ganaste Jugador 1 la piedra parte la tijera")
elif elijeusuario1 == elijeusuario2:
    print("El resultado es un empate")
print("Gracias por jugar")
