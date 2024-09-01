# pdc_reto_11
### Soy Rafael Santiago Chirivi Peña y pertenezco al grupo de "Fenomenoides", adelante se muestra nuestro logo 

<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>

### A continuacion, se muestran las soluciones propuestas a los distintos puntos de este reto
1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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
```

2. Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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
```

3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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
```

4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```python
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

def suma_columna (matriz : list) -> int:    # definir la funcion
    suma = 0    # se asigna un valor a la variable de la suma

    columna = int(input("Que columna de la matriz desea sumar: "))  # ingreso de la columna a sumar
    while columna > len(matriz[0])+1 or columna < 1:    # restriccion para la columna
        columna = int(input("No existe la columna ingresada, por favor intentelo de nuevo"))

    for i in range(len(matriz)):    # recorrido por las filas
        suma += int(matriz[i][columna-1])   # suma al valor el dato entero de los datos de la columna seleccionada

    return suma     # retorno de la suma de la columna

if __name__ == "__main__":
    try:    # definir los posibles errores para el ingreso de datos
        mat = matriz(mat)   # se establece la matriz en la variable a partir de la funcion matriz

        print (f"La matriz resultante es: ")    # se imprime la matriz
        for i in range(len(mat)):
            print(mat[i])
            
        sum_columna = suma_columna(mat) # se realiza la suma de la columna
        print(f"La suma de los datos de la columna seleccionada es {sum_columna}")  # se imprime la suma de los datos de la columna
        
    except ValueError:  # al agregar un dato diferente de un numero, se realiza la impresion del mensaje
        print("El valor ingresado no se trata de un numero entero")
```

5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```python
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
```
