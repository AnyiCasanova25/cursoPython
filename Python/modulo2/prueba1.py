print("!Hola,Mundo¡")

# La funcion sep y end
print("Mi", "nombre", "es", sep="_", end="*")
print("Anyi", "Casanova.", sep="*", end="*\n")

#Ejercicio
print("Programming","Essentials","in", sep="***", end="...")
print("Python")

#Ejercicio Flecha
print("    *     "*2)
print("   * *    "*2)
print("  *   *   "*2)
print(" *     *  "*2)
print("***   *** "*2)
print("  *   *   "*2)
print("  *   *   "*2)
print("  *****   "*2)


#Valores hexadecimales
print(0x123)

print(0.0000000000000000000001)

#Valore booleanos
print(True > False)
print(True < False)

#suma
print(2+2)

#otro ejemplo suma
a=5
b=3
print(a+b)

#Exponenciacion
print(2 ** 3) #entero por enetero = entero
print(2 ** 3.) #entero por flotante =flotante
print(2. ** 3) #flotante por entero = flotante
print(2. ** 3.)#flotante por flotante =flotante

#division
print(6 / 3)#entero por enetero = flotante, esta es la excepcion a la regla.
print(6 / 3.)#entero por flotante =flotante
print(6. / 3)#flotante por entero = flotante
print(6. / 3.)#flotante por flotante =flotante

#division entera = floor division
print(6 // 3)#entero por enetero = entero
print(6 // 3.)#entero por flotante =flotante
print(6. // 3)#flotante por entero = flotante
print(6. // 3.)#flotante por flotante =flotante
#nota= redondea hacia abajo.

#numeros negativos 
print(-6 // 4)
print(6. // -4)

#residuo modulo
print(14 % 4)

#suma
print(-4 + 4)
print(-4. + 8)

#El operador de resta, operadores unarios y binarios
print(-4 - 4)
print(4. - 8)
print(-1.1)

#mas ejemplos exponenciales
print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))

#Operadores y paréntesis
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

#ejercicio manzanas
juan =3
maria=5
adan=6
total_manzanas=(juan+maria+adan)
print("juan:" ,juan,"\nmaria:",maria,"\nadan:",adan)
print("El total de las manzanas es:",total_manzanas)


#ejercicio kilometros
kilometers = 12.25
miles = 7.38

calcular_km = miles*1.61
calcular_m =kilometers/1.62

print(miles, "millas son", calcular_km, "kilómetros")
print(kilometers, "kilómetros son",calcular_m, "millas")

#convertido de entero a float
x =  2
x = float(x)
print("x =", x)

#funcion imput 
print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")

#otro ejemplo a la potencia
anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

##hipotenusa
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)

#version mas corta
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es:", (leg_a**2 + leg_b**2) ** .5)

#ejercicio info 
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")

#otro ejemplo
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#otroo ejercicio de cateto
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))

#otro ejemplo eso es todo amigos
a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))

suma= a+b
resta=a-b
division=a/b
multiplicacion=a*b

print("\n¡Eso es todo, amigos!")
print("suma:",suma,"\nresta:",resta,"\ndivision:",division,"\nmultiplicacion:",multiplicacion)


