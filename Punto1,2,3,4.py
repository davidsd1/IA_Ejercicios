# 1. Función que imprime los números impares en un rango de manera inversa
def imprimir_impares_inverso(inicio, fin):
    for num in range(fin, inicio - 1, -1):
        if num % 2 != 0:
            print(num)

# 2. Función que organiza el código anterior para que la impresión sea horizontal separada por comas
def imprimir_impares_inverso_horizontal(inicio, fin):
    impares = [str(num) for num in range(fin, inicio - 1, -1) if num % 2 != 0]
    print(', '.join(impares))

# 3. Función para crear una matriz triangular con 1s
def matriz_triangular(n):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            matriz[i][j] = 1
    for fila in matriz:
        print(fila)

# 4. Función para crear un triángulo invertido de asteriscos
def triangulo_invertido(n):
    for i in range(n):
        print(' ' * i + '*' * (2 * (n - i) - 1))

# Llamadas a las funciones para ejecutarlas

# 1. Imprimir los números impares en un rango inverso
print("Impares en orden inverso:")
imprimir_impares_inverso(1, 20)
print()  # Salto de línea para separación

# 2. Imprimir los números impares en un rango inverso de manera horizontal separados por comas
print("Impares en orden inverso separados por comas:")
imprimir_impares_inverso_horizontal(1, 20)
print()  # Salto de línea para separación

# 3. Crear y mostrar una matriz triangular
print("Matriz triangular de 1s:")
matriz_triangular(6)
print()  # Salto de línea para separación

# 4. Crear y mostrar un triángulo invertido de asteriscos
print("Triángulo invertido:")
triangulo_invertido(5)
