print("Calculadora simple\n")
print("Esta calculadora realiza las operaciones básicas entre dos números enteros o decimales")
while True:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    opcion = int(input("Ingrese:\n1 para suma\n2 para resta\n3 para multiplicación\n4 para división\nSu opción: "))
    if opcion == 1:
        resultado = num1 + num2
        break
    elif opcion == 2:
        resultado = num1 - num2
        break
    elif opcion == 3:
        resultado = num1 * num2
        break
    elif opcion == 4:
        while num2 == 0:
            print("El divisor no puede ser cero")
            num2 = float(input("Ingrese un divisor válido: "))
        resultado = num1 / num2
        break
    else:
        print("Opción no válida")
        break
print("El resultado es:",resultado)
