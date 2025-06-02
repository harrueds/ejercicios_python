# se ingresan los coeficientes e una ecuación cuadrática
# y devuelve las soluciones según corresponda.

a = float(input("coef cuad="))
b = float(input("coef lineal="))
c = float(input("coef libre="))
disc = b**2 - 4 * a * c
if disc == 0:
sol = -b / (2 * a)
print(f"única solución:{sol}")
elif disc < 0:
print("no hay solución")
elif disc > 0:
sol1 = (-b - disc**0.5) / (2 * a)
sol2 = (-b + disc**0.5) / (2 * a)
print(f"dos soluciones {sol1} y {sol2}")
