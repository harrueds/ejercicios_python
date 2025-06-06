def solicitar_datos():
    try:
        maximo = float(input("Ingresa el número máximo: "))
        porcentaje = float(input("Ingresa el porcentaje (entre 0 y 100): "))
        if porcentaje < 0 or porcentaje > 100:
            print("El porcentaje debe estar entre 0 y 100.")
            return None, None
        return maximo, porcentaje
    except ValueError:
        print("Por favor, ingresa números válidos.")
        return None, None


def funcion_lineal(p1, p2, x):
    x1, y1 = p1
    x2, y2 = p2
    if x2 - x1 == 0:
        return None  # evitar división por cero
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m * x + b


def main():
    maximo, porcentaje = solicitar_datos()
    if maximo is None or porcentaje is None:
        return

    x = (porcentaje / 100.0) * maximo

    if porcentaje == 60:
        y = funcion_lineal((0, 2.0), (0.6 * maximo, 4.0), x)
        print(f"Valor de y para porcentaje {porcentaje}%: {y}")
    elif porcentaje > 60:
        y = funcion_lineal((0.6 * maximo, 4.0), (maximo, 7.0), x)
        print(f"Valor de y para porcentaje {porcentaje}%: {y}")
    else:
        print("Porcentaje menor a 60%, no se define función para ese caso.")


if __name__ == "__main__":
    main()


"""porcentaje=float(input("Ingrese el procentaje de exigencia:"))
max=float(input("Ingrese el puntaje máximo:"))
opcion=float(input("Ingrese su opción:\n1.- Tabla completa\t2.-Solamente un untaje"))

if """
