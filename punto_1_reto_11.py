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

def criterio_oper (matriz1 : list, matriz2 : list) -> bool: #definir la funcion
    if len(matriz2) == len(matriz1) and len(matriz2[0]) == len(matriz1[0]):     # criterio para operacion de suma o resta de funciones: mismo numero de filas y columnas
        return True     # retorno de condicion verdadera
    
    elif len(matriz2) != len(matriz1) or len(matriz2[0]) != len(matriz1[0]):    # caso en que las filas o las columnas no coinciden entre si
        return False    # retorno de condicion falsa

def suma_matriz (matriz1 : list, matriz2 : list) -> list:   #establecer una funcion
    suma_matriz = []    #establecer una variable como resultado de la operacion
    fila = []           #establecer una variable para poder asignar los datos

    for i in range(len(matriz1)):           #recorrido por las filas (se utiliza la matriz1 pero podria ser cualquiera, ya que tienen la misma dimension)
        for j in range(len(matriz1[0])):    #recorrido por las columnas
            fila.append(int(matriz1[i][j]) + int(matriz2[i][j]))    #agregar a la fila el dato de la suma
        suma_matriz.append(fila)    # una vez recorrida la fila y llenada con el numero de datos a sumar, se agrega la fila a la matriz
        fila = []   # se reestablece la variable fila para agregar nuevos datos
    return suma_matriz  # retorno de la operacion de suma de matrices 

def resta_matriz (matriz1 : list, matriz2 : list) -> list:
    resta_matriz = []   #establecer una variable como resultado de la operacion
    fila = []           #establecer una variable para poder asignar los datos
    
    for i in range(len(matriz1)):           #recorrido por las filas (se utiliza la matriz1 pero podria ser cualquiera, ya que tienen la misma dimension)
        for j in range(len(matriz1[0])):    #recorrido por las columnas
            fila.append(int(matriz1[i][j]) - int(matriz2[i][j]))    #agregar a la fila el dato de la resta
        resta_matriz.append(fila)   # una vez recorrida la fila y llenada con el numero de datos a restar, se agrega la fila a la matriz
        fila = []   # se reestablece la variable fila para agregar nuevos datos
    return resta_matriz # retorno de la operacion de resta de matrices

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
        
        criterio = criterio_oper(A, B)  # las matrices pasan por el criterio de igualdad de filas y columnas

        while not criterio:     # condicion falsa para el criterio
            edit = str(input("Las dimensiones entre las matrices no coinciden, digite que matriz desea editar: \n A o B: "))    # seleccion de la matriz a cambiar 
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

            operacion = int(input("La suma/resta de las matrices se realiza dato a dato, por favor ingrese que operacion desea realizar: \n 1. Suma \n 2. Resta \n"))   # seleccion de la operacion a realizar entre las matrices
            C = []  # se establece una matriz a la cual asignar la operacion

            if operacion == 1:  # seleccion de la operacion suma
                C = suma_matriz(A, B)   # se establece la matriz aplicando la funcion de suma

                print("La matriz resultante de A + B es: ")     # impresion de la matriz de suma
                for i in range (len(C)):
                    print(C[i])

            elif operacion == 2:    # seleccion de la operacion resta
                C = resta_matriz(A, B)  # se establece la matriz aplicando la funcion de resta

                print("La matriz resultante de A - B es: ")     # impresion de la matriz de resta
                for i in range (len(C)):
                    print(C[i])

    except ValueError:  # al agregar un dato diferente de un numero, se realiza la impresion del mensaje
        print("El valor ingresado no se trata de un numero entero")