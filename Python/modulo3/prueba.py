# print("Prueba Uno")

# #validaciones true and false
# var = 0  # Asignando 0 a var
# print(var == 0)

# var = 1  # Asignando 1 a var
# print(var == 0)

# #ejemplos
# var = 55  # Asignando 0 a var
# print(var == 0)

# var = 99  # Asignando 1 a var
# print(var == 0)

# var = 100  # Asignando 0 a var
# print(var == 100)

# var = 101  # Asignando 1 a var
# print(var == 101)

# var = -5  # Asignando 0 a var
# print(var == 0)

# var = +123  # Asignando 1 a var
# print(var == +123)


# #otro ejemplo
# # Se leen dos números
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))
 
# # Elige el número más grande
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2
 
# # Imprime el resultado
# print("El número más grande es:", larger_number)

# #otro ejemplo
# # Se leen tres números
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))
# number3 = int(input("Ingresa el tercer número: "))
 
# # Asumimos temporalmente que el primer número
# # es el más grande.
# # Lo verificaremos pronto.
# largest_number = number1
 
# # Comprobamos si el segundo número es más grande que el mayor número actual
# # y actualiza el número más grande si es necesario.
# if number2 > largest_number:
#     largest_number = number2
 
# # Comprobamos si el tercer número es más grande que el mayor número actual
# # y actualiza el número más grande si es necesario.
# if number3 > largest_number:
#     largest_number = number3
 
# # Imprime el resultado.
# print("El número más grande es:", largest_number)

#funcion max
# Se leen tres números.
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))
# number3 = int(input("Ingresa el tercer número: "))
 

# largest_number = max(number1, number2, number3)
 
# # Imprime el resultado
# print("El número más grande es:", largest_number)

# text= str(input("Ingrese la palabra: " ))

# if text == "espatifilo":
#     print("No, ¡quiero un gran Espatifilo!")

# elif text == "pelargonio":
#     print("¡Espatifilo!, ¡No pelargonio!")

# else:
#     print("Si, ¡El Espatifilo! es la mejor planta de todos los tiempos!")

#ejemplo importante if
# income = float(input("Introduce el ingreso anual: "))

# if income < 85528:
# 	tax = income * 0.18 - 556.02
# else:
# 	tax = (income - 85528) * 0.32 + 14839.02

# if tax < 0.0:
# 	tax = 0.0

# tax = round(tax, 0)
# print("El impuesto es:", tax, "pesos")

#Año bisiesto
# year = int(input("Introduce un año: "))

# if year < 1582:
# 	print("No esta dentro del período del calendario Gregoriano")
# else:
# 	if year % 4 != 0:
# 		print("Año Común")
# 	elif year % 100 != 0:
# 		print("Año Bisiesto")
# 	elif year % 400 != 0:
# 		print("Año Común")
# 	else:
# 		print("Año Bisiesto")

#maneras de declarar variables numericas
# x, y, z = 5, 10, 8
 
# print(x > z)
# print((y - 5) == x)


#OTRO EJEMPLO
# x = "1"
 
# if x == 1:
#     print("one")
# elif x == "1":
#     if int(x) > 1:
#         print("two")
#     elif int(x) < 1:
#         print("three")
#     else:
#         print("four")
# if int(x) == 1:
#     print("five")
# else:
#     print("six")
 
 
 #BUCLE INFINITO
#  while True:
#     print("Estoy atrapado dentro de un bucle.")


#conteo numeros pares e impares
# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.
 
# odd_numbers = 0
# even_numbers = 0
 
# # Lee el primer número.
# number = int(input("Introduce un número o escribe 0 para detener: "))
 
# # 0 termina la ejecución.
# while number != 0:
#     # Verificar si el número es impar.
#     if number % 2 == 1:
#         # Incrementar el contador de números impares odd_numbers.
#         odd_numbers += 1
#     else:
#         # Incrementar el contador de números pares even_numbers.
#         even_numbers += 1
#     # Leer el siguiente número.
#     number = int(input("Introduce un número o escribe 0 para detener: "))
 
# # Imprimir resultados.
# print("Conteo de números impares:", odd_numbers)
# print("Conteo de números pares:", even_numbers)


# OTRO EJEMPLO 
# largest_number = -999999999
 
# # Ingresa el primer valor.
# number = int(input("Introduce un número o escribe -1 para detener: "))
 
# # Si el número no es igual a -1, continuaremos
# while number != -1:
#     # ¿Es el número más grande que el valor de largest_number?
#     if number > largest_number:
#         # Sí si, se actualiza largest_number.
#         largest_number = number
#     # Ingresa el siguiente número.
#     number = int(input("Introduce un número o escribe -1 para detener: "))
 
# # Imprime el número más grande.
# print("El número más grande es:", largest_number)


#OTRO EJEMPLO
# counter = 5
# while counter != 0:
#     print("Dentro del bucle.", counter)
#     counter -= 1
# print("Fuera del bucle.", counter)


#Otro ejemplo
# secret_number = 777

# print(
# """
# +================================+
# | ¡Bienvenido a mi juego, muggle!|
# | Introduce un número entero     |
# | y adivina qué número he        |
# | elegido para ti.               |
# |¿Cuál es el número secreto?     |
# +================================+
# """)

# number = int(input("¿Cuál es el número secreto?   "))

# while number != 777:
    
#     print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
#     number = int(input("¿Cuál es el número secreto?   "))
    
# print("¡Bien hecho, muggle! Eres libre ahora.")


#CICLO FOR
#OTRO EJEMPLO
# for i in range(100):
#     print("el numero es: " , i)
#     i+=1
#     pass


# for i in range(10):
#     print("El valor de i es", i)


# for i in range(2, 8):
#     print("El valor de i es", i)

# for i in range(2, 8, 3):
#     print("El valor de i es", i)

#POR LA POTENCIA
# power = 1
# for expo in range(16):
#     print("2 a la potencia de", expo, "es", power)
#     power *= 2

#tabla multiplicar con for
#num =2
#for mul in range(11):
#print (num,"*",mul,"es",(num*mul))

#ejemplo
# import time

# for i in  range(1,6):
#     print(i,"Mississippi")
#     time.sleep(1)
# print()
# print("Lista o no, aquí vengo!")

#FUNCION BREAK
# break - ejemplo

# print("La instrucción break:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")


# # continue - ejemplo

# print("\nLa instrucción continue:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")


# #ejemplo
# largest_number = -99999999
# counter = 0

# while True:
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("El número más grande es", largest_number)
# else:
#     print("No has ingresado ningún número.")



# largest_number = -99999999
# counter = 0

# number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

# while number != -1:
#     if number == -1:
#         continue
#     counter += 1

#     if number > largest_number:
#         largest_number = number
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))


# #ejemplo chpacabras
# palabra_s="chupacabra"

# while True:
#     palabra = input("Ingresa una palabra o 'chupacabra' para finalizar el programa: ")
#     if palabra == "chupacabra":
#         print("Has dejado el bucle con éxito.")
#         break
# else:
#     print("")


# elimina Vocales de palabras y ponerlas de forma horizontas

# user_word = input("Ingresa una palabra: ")

# user_word = user_word.upper()

# for letter in user_word:
#     if letter in ['A', 'E', 'I', 'O', 'U']:
#         continue
#     print(letter)


# elimina Vocales de palabras y ponerla de forma vertical

# user_word = input("Ingresa una palabra: ")

# user_word = user_word.upper()

# word_without_vowels = ""

# for letter in user_word:
#     if letter in ['A', 'E', 'I', 'O', 'U']:
#         continue
#     else:
#         word_without_vowels += letter

# print("La palabra sin vocales es:", word_without_vowels)


# ###########
# i = 1
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)

###
# i = 5
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)

###
# for i in range(5):
#     print(i)
# else:
#     print("else:", i)

# ###
# i = 111
# for i in range(2, 1):
#     print(i)
# else:
#     print("else:", i)

# blocks = int(input("Ingrese la cantidad de bloques que tienen los constructores: "))

# height = 0
# total_blocks = 0

# while total_blocks <= blocks:
#     height += 1
#     total_blocks += height

# print("La altura de la pirámide es:", height - 1)


# c0 = int(input("Ingrese un número natural: "))
# steps = 0

# while c0 != 1:
#     print(c0)
#     if c0 % 2 == 0:
#         c0 //= 2
#     else:
#         c0 = 3 * c0 + 1
#     steps += 1

# print(1)  # Imprimir el último valor, que siempre será 1
# print("Pasos =", steps)



# var = 17
# var_right = var >> 1
# var_left = var << 2
# print(var, var_left, var_right)



# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

# numbers[0] = 111
# print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
# print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

# print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.


# var = 17
# var_right = var >> 1
# var_left = var << 2
# print(var, var_left, var_right)



# #LISTAAAAAAAAAA
# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista:", numbers)  # Imprimiendo contenido de la lista original.
 
# numbers[0] = 111
# print("Nuevo contenido de la lista: ", numbers)  # Contenido actual de la lista.




# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.
 
# numbers[0] = 111
# print("\nPrevio contenido de la lista:", numbers)  # Imprimiendo contenido de la lista anterior.
 
# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
# print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.




# #ejemplo
# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

# numbers[0] = 111
# print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
# print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

# print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.



# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

# numbers[0] = 111
# print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
# print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

# print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

# ###

# del numbers[1]  # Eliminando el segundo elemento de la lista.
# print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
# print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

# ###



# numbers = [111, 7, 2, 1]
# print(numbers[-1])

# numbers = [111, 7, 2, 1]
# print(numbers[-2])



# numbers = [1, 2, 3, 4, 5]

# # Paso 1
# numbers[2] = int(input("Ingrese un número para reemplazar al número central: "))

# # Paso 2
# numbers.pop()

# # Paso 3
# print("La longitud de la lista es:", len(numbers))




# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)

# ###

# numbers.append(4)

# print(len(numbers))
# print(numbers)

# ###

# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)

# #


#lista vacia
# my_list = []  # Creando una lista vacía.

# for i in range(5):
#     my_list.append(i + 1)

# print(my_list)

#BUCLE Y LISTA
# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in range(len(my_list)):
#     total += my_list[i]

# print(total)





# beatles = []


# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")


# del beatles[3:5]


# beatles.insert(0, "Ringo Starr")

# print("Los miembros de la banda son:", beatles)



# my_list = [8, 10, 6, 2, 4]  # lista a ordenar
# swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
# while swapped:
#     swapped = False  # no hay intercambios hasta ahora
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # ¡ocurrió el intercambio!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
# print(my_list)



# my_list = []
# swapped = True
# num = int(input("¿Cuántos elementos deseas ordenar?: "))

# for i in range(num):
#     val = float(input("Ingresa un elemento de la lista: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nOrdenada:")
# print(my_list)


# list_1 = [1]
# list_2 = list_1
# list_1[0] = 2
# print(list_2)


# # Copiando la lista completa.
# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)

# # Copiando parte de la lista.
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)



# my_list = [0, 3, 12, 8, 2]

# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)



# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]

# for i in range(1, len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]

# print(largest)


# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# #
# # Escribe tu código aquí.
# #
# print("La lista con elementos únicos:")
# print(my_list)





# EMPTY = "-"
# ROOK = "R"
# KNIGHT = "N"
# PAWN = "P"


# board = [[EMPTY for _ in range(8)] for _ in range(8)]

# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK

# board[3][2] = KNIGHT


# board[4][4] = PAWN


# for row in board:
#     print(row)





# # Cubo - un arreglo tridimensional (3x3x3)
 
# cube = [[[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':(', 'x', 'x']],
 
#         [[':)', 'x', 'x'],
#          [':(', 'x', 'x'],
#          [':)', 'x', 'x']],
 
#         [[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':)', 'x', 'x']]]
 
# print(cube)
# print(cube[0][0][0])  # output: ':('
# print(cube[2][2][0])  # output: ':)'