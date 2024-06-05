# def hi(name):
#     print("Hola,", name)
 
# hi("Greg")

# def hi_all(name_1, name_2):
#     print("Hola,", name_2)
#     print("Hola,", name_1)
 
# hi_all("Sebastián", "Konrad")




# imprimir direccion paciente

# def address(street, city, postal_code):
#     print("Tu dirección es:", street,"St.,", city, postal_code)
 
# s = input("Calle: ")
# p_c = input("Código Postal: ")
# c = input("Ciudad: ")
# address(s, c, p_c)


# # Ejemplo 1
# def subtra(a, b):
#     print(a - b)
 
# subtra(5, 2) # salida: 3
# subtra(2, 5) # salida: -3
 
 
# # Ejemplo 2
# def subtra(a, b):
#     print(a - b)
 
# subtra(a=5, b=2) # salida: 3
# subtra(b=2, a=5) # salida: 3
 
# # Ex. 3
# def subtra(a, b):
#     print(a - b)
 
# subtra(5, b=2) # salida: 3
# subtra(5, 2) # salida: 3

# def intro(a="James Bond", b="Bond"):
#      print("Mi nombre es", b + ".", a + ".")
 
# intro()

# def intro(a="James Bond", b="Bond"):
#     print("Mi nombre es", b + ".", a + ".")
 
# intro(b="Sean Connery")

# def intro(a, b="Bond"):
#     print("Mi nombre es", b + ".", a + ".")
 
# intro("Susan")

# def happy_new_year(wishes = True):
#     print("Tres...")
#     print("Dos...")
#     print("Uno...")
#     if not wishes:
#         return
 
#     print("¡Feliz año nuevo!")
# happy_new_year()

#Return
# def boring_function():
#     print("'Modo aburrimiento' ON.")
#     return 123
 
# print("¡Esta lección es interesante!")
# boring_function()
# print("Esta lección es aburrida...")


# def strange_function(n):
#     if(n % 2 == 0):
#         return True
# print(strange_function(2))
# print(strange_function(1))


#cuenta regresiva
# def strange_list_fun(n):
#     strange_list = []
    
#     for i in range(0, n):
#         strange_list.insert(0, i)
    
#     return strange_list

# print(strange_list_fun(5))

#YEAR
# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr,"-> ",end="")
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Fallido")

# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# def days_in_month(year,month):
#     if year < 1582 or month < 1 or month > 12:
#         return None
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     res  = days[month - 1]
#     if month == 2 and is_year_leap(year):
#         res = 29
#     return res

# test_years = [1900, 2000, 2016, 1987]
# test_months = [ 2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr,mo,"-> ",end="")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Fallido")

# #MESES DIA Y AÑO
# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# def days_in_month(year, month):
#     if month < 1 or month > 12:
#         return None
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     res = days[month - 1]
#     if month == 2 and is_year_leap(year):
#         res = 29
#     return res

# def day_of_year(year, month, day):
#     if month < 1 or month > 12:
#         return None
#     dim = days_in_month(year, month)
#     if dim is None or day < 1 or day > dim:
#         return None
#     day_of_year = sum(days_in_month(year, m) for m in range(1, month)) + day
#     return day_of_year

# # Prueba de la función
# print(day_of_year(2000, 12, 31))  # Debe devolver 366
# print(day_of_year(2001, 2, 28))   # Debe devolver 59
# print(day_of_year(2004, 2, 29))   # Debe devolver 60
# print(day_of_year(2000, 13, 1))   # Debe devolver None
# print(day_of_year(2000, 2, 30))   # Debe devolver None
# print(day_of_year(2021, 4, 15))   # Debe devolver 105


# #NUMERO PRIMO
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# # Prueba de la función is_prime
# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()

# #MILLAS
# def liters_100km_to_miles_gallon(liters):
#     miles_per_100km = 100 * 1000 / 1609.344
#     gallons = liters / 3.785411784
#     mpg = miles_per_100km / gallons
#     return mpg

# def miles_gallon_to_liters_100km(miles):
#     km_per_gallon = miles * 1.609344
#     liters_per_100km = 100 / (km_per_gallon / 3.785411784)
#     return liters_per_100km

# # Pruebas de las funciones
# print(liters_100km_to_miles_gallon(3.9))  # Debe devolver aproximadamente 60.31
# print(liters_100km_to_miles_gallon(7.5))  # Debe devolver aproximadamente 31.36
# print(liters_100km_to_miles_gallon(10.))  # Debe devolver aproximadamente 23.52
# print(miles_gallon_to_liters_100km(60.3))  # Debe devolver aproximadamente 3.9
# print(miles_gallon_to_liters_100km(31.4))  # Debe devolver aproximadamente 7.5
# print(miles_gallon_to_liters_100km(23.5))  # Debe devolver aproximadamente 10.0


# #revision quizz
# def hi():
#     return
#     print("¡Hola!")
 
# hi()


# def is_int(data):
#     if type(data) == int:
#         return True
#     elif type(data) == float:
#         return False
 
# print(is_int(5))
# print(is_int(5.0))
# print(is_int("5"))


#LISTA DE DOS EN DOS
# def even_num_lst(ran):
#     lst = []
#     for num in range(ran):
#         if num % 2 == 0:
#             lst.append(num)
#     return lst
 
# print(even_num_lst(11))


# #LISTA EXPONENCIAL
# def list_updater(lst):
#     upd_list = []
#     for elem in lst:
#         elem **= 2
#         upd_list.append(elem)
#     return upd_list
 
# foo = [1, 2, 3, 4, 5]
# print(list_updater(foo))

#alcances
# def my_function():
#     print("¿Conozco a la variable?", var)


# var = 1
# my_function()
# print(var)


# #CON GLOBAL
# def my_function():
#     global var
#     var = 2
#     print("¿Conozco a aquella variable?", var)


# var = 1
# my_function()
# print(var)

#otro ejemplo
# def my_function(n):
#     print("Yo recibí", n)
#     n += 1
#     print("Ahora tengo", n)


# var = 1
# my_function(var)
# print(var)

# #lista
# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     my_list_1 = [0, 1]
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)
 
 
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)


#RESUMEN DE SECCION
# var = 2
 
 
# def mult_by_var(x):
#     return x * var
 
 
# print(mult_by_var(7)) # salida: 14


# def mult(x):
#     var = 5
#     return x * var
 
 
# print(mult(7)) # salida: 35


# def adding(x):
#     var = 7
#     return x + var
 
 
# print(adding(4)) # salida: 11
# print(var) # NameError


# var = 2
# print(var) # salida: 2
 
 
# def return_var():
#     global var
#     var = 5
#     return var
 
 
# print(return_var()) # salida: 5
# print(var) # salida: 5

# def is_a_triangle(a, b, c):
#     if a + b <= c:
#         return False
#     if b + c <= a:
#         return False
#     if c + a <= b:
#         return False
#     return True


# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))

# #TEOREMA DE PITAGORAS
# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# a = float(input('Ingresa la longitud del primer lado: '))
# b = float(input('Ingresa la longitud del segundo lado: '))
# c = float(input('Ingresa la longitud del tercer lado: '))

# if is_a_triangle(a, b, c):
#     print('Si, si puede ser un triángulo.')
# else:
#     print('No, no puede ser un triángulo.')


# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
 
 
# def is_a_right_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return False
#     if c > a and c > b:
#         return c ** 2 == a ** 2 + b ** 2 if a > b and a > c:
#     if a > b and a > c:
#         return a ** 2 == b ** 2 + c ** 2
# print(is_a_right_triangle(5, 3, 4))
# print(is_a_right_triangle(1, 3, 4))


#factorial
# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
 
#     product = 1
#     for i in range(2, n + 1):
#         product *= i
#     return product
 
 
# for n in range(1, 6): # probando
#     print(n, factorial_function(n))


# #numero fibonacci
# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
 
#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum
 
 
# for n in range(1, 10): # probando
#     print(n, "->", fib(n))

# #RECURSIVIDAD
# def fib(n):
#     if n < 1:
#          return None
#     if n < 3:
#         return 1

#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum


# for n in range(1, 10):
#     print(n, "->", fib(n))


#TUPLA
# my_tuple = (1, 10, 100, 1000)

# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[1:])
# print(my_tuple[:-2])

# for elem in my_tuple:
#     print(elem)


# my_tuple = (1, 10, 100)

# t1 = my_tuple + (1000, 10000)
# t2 = my_tuple * 3

# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)

#DICCIONARIO
# dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
# words = ['gato', 'león', 'caballo']
 
# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "no está en el diccionario")

# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
# for key in dictionary.keys():
#     print(key, "->", dictionary[key])

# #INSERTAR CON UPDATE
# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
# dictionary.update({"pato": "canard"})
# print(dictionary)


