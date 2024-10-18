# 5. Función que imprime y guarda una figura de diamante en un archivo de texto
def figura_diamante(archivo):
    n = 5
    # Abrir archivo en modo escritura
    with open(archivo, 'w') as f:
        # Parte superior del diamante
        for i in range(n):
            linea = ' ' * (n - i - 1) + '*' * (2 * i + 1)
            print(linea)  # Imprimir en pantalla
            f.write(linea + '\n')  # Escribir en archivo
        
        # Parte inferior del diamante
        for i in range(n - 2, -1, -1):
            linea = ' ' * (n - i - 1) + '*' * (2 * i + 1)
            print(linea)  # Imprimir en pantalla
            f.write(linea + '\n')  # Escribir en archivo

# Llamada para imprimir en pantalla y generar el archivo
figura_diamante('figura_diamante.txt')
