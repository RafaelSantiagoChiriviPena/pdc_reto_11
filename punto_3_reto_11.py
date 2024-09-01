matriz_tras = []    # establecer la variable para la matriz
traspuesta = []     # establecer la variable para la matriz traspuesta

def matriz (matriz : list) -> list:     #Definir la funcion
    filas : int = int(input("Ingrese la cantidad de filas para la matriz: "))   #ingresar el numero de filas para la matriz
    while filas < 1:    # restriccion del numero de filas para ser mayor que 0
        filas = int(input("El valor ingresado no es valido, intentelo de nuevo: "))

    columnas : int = int(input("Ingrese la cantidad de columnas para la matriz: ")) # ingresar el numero de columnas para la matriz
    while columnas < 1:     # resstriccion del numero de filas para ser mayor que 0 
        columnas = int(input("El valor ingresado no es valido, intentelo de nuevo: "))
        
    matriz = []     #establecer una variable para poder asignar las filas
    fila = []       #establecer una variable para poder asignar los datos

    for i in range(filas): #recorrido por las filas
        for j in range(columnas):   #recorrido por las columnas 
            dato_ij : int = int(input(f"Ingrese el valor para el dato ({i + 1} , {j + 1} ): ")) # ingresar el dato segun la ubicacion dada (i,j)
            fila.append(dato_ij)    # asignacion del dato ingresado a la fila
        matriz.append(fila)     # una vez recorrida la fila y llenada con los el numero de datos estipulados en las columnas, se agrega la fila a la matriz
        fila = []   # se reestablece la variable de fila para agregar nuevos datos

    return matriz   # retorno de la funcion, una matriz

def traspuesta (matriz : list) -> list:     # definir la funcion
    traspuesta = []     # establecer la variable de la matriz
    fila = []           # establecer la fila para asignar los datos

    for i in range(len(matriz[0])):     # recorrer las columnas 
        for j in range(len(matriz)):    # recorrer las filas
            fila.append(matriz[j][i])   # asignar el dato traspuesto (fila -> columna ; columna -> fila) a la fila
        traspuesta.append(fila)         # una vez recorrida la fila, se asigna a la matriz
        fila = []   # se reestablece la fila para agregar nuevos datos

    return traspuesta   # retorno de la matriz traspuesta

if __name__ == "__main__":
    try:    # definir los posibles errores de ingreso de datos
        matriz_tras = matriz(matriz_tras)   # se establece la matriz a la que obtener su traspuesta mediante la funcion matriz
        
        print (f"La matriz resultante es: ")    # se imprime la matriz
        for i in range(len(matriz_tras)):
            print(matriz_tras[i])

        tras = traspuesta(matriz_tras)      # se realiza la operacion de traspuesta a la matriz y se asigna a una nueva variable

        print("La matriz traspuesta se explica como el cambio de posicion en los elementos de a(ij) -> a(ji), y cambiando la dimension de n*m a m*n")
        print (f"La matriz traspuesta resultante es: ") # se imprime la matriz traspuesta resultante
        for i in range(len(tras)):
            print(tras[i])

    except ValueError:  # al agregar un dato diferente de un numero, se realiza la impresion del mensaje
        print("El valor ingresado no se trata de un numero entero")