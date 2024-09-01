A = []  #Establecer variable para la matriz 1 o A
B = []  #Establecer variable para la matriz 2 o B
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

def criterio_oper (matriz1 : list, matriz2 : list) -> bool:     # establecer la funcion
    if len(matriz1[0]) == len(matriz2):     # criterio para producto de matrices: numero de columnas de la primera matriz es igual al numero de las filas de la segunda matriz
        return True     # retorno de la condicion verdadera
    
    elif len(matriz1[0]) != len(matriz2):   # caso en donde el criterio no se cumple
        return False    # retorno de la condicion falsa

def matriz_mult (matriz1 : list, matriz2 : list) -> list:       # establecer la funcion
    matriz_mult = []    # definir la matriz resultante de la operacion
    fila = []           # establecer fila para asignar los datos
    dato_ij = 0         # establecer el dato a asignar 

    for i in range (len(matriz1)):  # recorrer las filas de la primera matriz
        for j in range (len(matriz2[0])):   # recorrer las columnas de la segunda matriz
            for h in range (len(matriz2)):  # recorrer las filas de la segunda matriz
                dato_ij += (int(matriz1[i][h]) * int(matriz2[h][j]))    # se asigna un valor al dato a partir de la sumatoria de las multiplicaciones de las filas por las columnas
            fila.append(dato_ij)    # se agrega el dato a la fila
            dato_ij = 0     # se reestablece el valor del dato a 0 
        matriz_mult.append(fila)    # una vez llenada la fila con los datos, se agrega a la matriz de multiplicacion
        fila = []           # se reestablece el valor de la fila

    return matriz_mult  # retorno de la multiplicacion de matrices

if __name__ == "__main__":
    try:    # definir los posibles errores de ingreso de datos

        A = matriz(A)   # se establece la primera matriz aplicando la funcion matriz a esta variable

        print (f"La matriz A resultante es: ")  # se imprime la matriz
        for i in range(len(A)):
            print(A[i])

        B = matriz(B)   # se establece la segunda matriz aplicando la funcion matriz a esta variable
        
        print (f"La matriz B resultante es: ")  # se imprime la matriz
        for i in range(len(B)):
            print(B[i])
        
        orden_mult : int = int(input("¿En que orden desea multiplicar las matrices? \n 1. A * B \n 2. B * A \n"))   # seleccion del orden de operacion, A * B, B * A
        if orden_mult == 1:     # seleccion de la operacion A * B
            criterio = criterio_oper(A, B)  # evaluacion del criterio para la multiplicacion de matrices

            while not criterio:     # condicion falsa para el criterio
                edit = str(input("Las columnas de A no coinciden con las filas de B, digite que matriz desea editar: \n A o B: "))  # seleccion de la matriz a cambiar
                if edit == "A":     # seleccion de la primera matriz
                    A = []  # se reestablece la variable para la matriz
                    A = matriz(A)   # se aplica de nuevo la funcion
                
                elif edit == "B":   # seleccion de la segunda matriz 
                    B = []  # se reestablece la variable para la matriz
                    B = matriz(B)   # se aplica de nuevo la funcion
                criterio = criterio_oper(A, B)  # se vuelve a aplicar el criterio de igualdad

                print (f"La matriz A resultante es: ")  # impresion de la primera matriz
                for i in range(len(A)):
                    print(A[i])
                        
                print (f"La matriz B resultante es: ")  # impresion de la segunda matriz
                for i in range(len(B)):
                    print(B[i])

            if criterio:    # condicion verdadera para el criterio
                C = []  # se establece la variable para el resultado de la operacion
                C = matriz_mult(A, B)   # se realiza la operacion

            print("La matriz resultante de A * B es: ")     # se imprime la matriz resultante
            for i in range (len(C)):
                print(C[i])
                
        elif orden_mult == 2:   # seleccion de la operacion B * A
            criterio = criterio_oper(B, A)  # evaluacion del criterio para la multiplicacion de matrices

            while not criterio:     # condicion falsa para el criterio
                edit = str(input("Las columnas de B no coinciden con las filas de A, digite que matriz desea editar: \n A o B: "))  # seleccion de la matriz a cambiar
                if edit == "A":     # seleccion de la primera matriz
                    A = []  # se reestablece la variable para la matriz
                    A = matriz(A)   # se aplica de nuevo la funcion
                
                elif edit == "B":   # seleccion de la segunda matriz 
                    B = []  # se reestablece la variable para la matriz
                    B = matriz(B)   # se aplica de nuevo la funcion
                criterio = criterio_oper(B, A)  # se vuelve a aplicar el criterio de igualdad

                print (f"La matriz A resultante es: ")  # impresion de la primera matriz
                for i in range(len(A)):
                    print(A[i])
                        
                print (f"La matriz B resultante es: ")  # impresion de la segunda matriz
                for i in range(len(B)):
                    print(B[i])

            if criterio:    # condicion verdadera para el criterio
                C = []  # se establece la variable para el resultado de la operacion
                C = matriz_mult(B, A)   # se realiza la operacion

            print("La matriz resultante de B * A es: ")     # se imprime la matriz resultante
            for i in range (len(C)):
                print(C[i])

    except ValueError:  # al agregar un dato diferente de un numero, se realiza la impresion del mensaje
        print("El valor ingresado no se trata de un numero entero")