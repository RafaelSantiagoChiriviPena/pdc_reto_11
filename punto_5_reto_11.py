mat = []    # se define una matriz (lista) vacia

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

def suma_fila (matriz : list) -> int:   # se define la funcion
    suma = 0    # se asigna un valor a la variable de la suma

    fila = int(input("Que fila de la matriz desea sumar: "))    # ingreso de la fila a sumar
    while fila > len(matriz)+1 or fila < 1: # restriccion para el numero de la fila
        fila = int(input("No existe la fila ingresada, por favor intentelo de nuevo"))  
        
    for j in range(len(matriz[0])):     # recorrido por el numero de datos en las filas (recorrido por las columnas)
        suma += int(matriz[fila-1][j])  # suma al valor el dato entero de los datos de la fila seleccionada

    return suma     # retorno de la suma de la fila

if __name__ == "__main__":
    try:    # definir los posibles errores para el ingreso de datos
        mat = matriz(mat)   # se establece la matriz en la variable a partir de la funcion matriz

        print (f"La matriz resultante es: ")    # se imprime la matriz
        for i in range(len(mat)):
            print(mat[i])
            
        sum_fila = suma_fila(mat) # se realiza la suma de la fila
        print(f"La suma de los datos de la columna seleccionada es {sum_fila}")  # se imprime la suma de los datos de la fila

    except ValueError:  # al agregar un dato diferente de un numero, se realiza la impresion del mensaje
        print("El valor ingresado no se trata de un numero entero")