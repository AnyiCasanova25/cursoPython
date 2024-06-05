# EJERCICIOS PYTHON 1

# 1. Definir una función max() que tome como argumento dos números y devuelva el
# mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero
# hacerla nosotros mismos es un muy buen ejercicio.

num1 = int(input("Digite el primer numero: " ))
num2 = int(input("Digite el segundo numero: " ))

def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print(max(num1, num2))


# 2. Definir una función max_de_tres(), que tome tres números como argumentos y
# devuelva el mayor de ellos.


num1 = int(input("Digite el primer numero: " ))
num2 = int(input("Digite el segundo numero: " ))
num3 = int(input("Digite el tercer numero: " ))

def max(num1, num2, num3):
    if num1 > num2:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3

print(max(num1, num2, num3))

# 3. Cuando se envían mensajes de texto o se tuitea, no es raro abreviar las palabras
# para ahorrar tiempo o espacio, como por ejemplo omitiendo las vocales, tal y como
# Twitter fue originalmente llamado "twttr". En un archivo llamado twttr.py, implementa
# un programa que solicite al usuario una cadena de texto y luego muestre esa misma
# cadena de texto, pero sin todas las vocales (A, E, I, O y U), ya sea que hayan sido
# ingresadas en mayúsculas o minúsculas.

# Corregir el siguiente código y comentar cual ha sido el error que genera.

# def main():
#     palabra = input("Ingrese una palabra: ")
#     resultado = twttr (palabra)
#     print ("La palabra abrevida es: " + "join(resultado)")

#     twttr(pal):
#         pal.lower()
#         sal=[]
#         for z in range(len(pal):
#         pal[z] not in ["a","e","i","o","u" "]:
#         sal.append(pal[z])
#     return sal

#     if __name__ =="__main__":
#     main();



#corregido
def main():
    palabra = input("Ingrese una palabra: ")
    resultado = twttr(palabra)
#Se corrige el join(resultado) a .join(resultado)
    print("La palabra abreviada es: " + ''.join(resultado))

def twttr(pal):
#se define pal
    pal = pal.lower()
    sal = []
#se acomodo el parentesis
    for z in range(len(pal)):
#se proporciona un if 
        if pal[z] not in ["a", "e", "i", "o", "u"]:
            sal.append(pal[z])
    return sal

if __name__ == "__main__":
    main()


# 4. Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
# contrario devuelve False.

def verificar_vocal(caracter):
    if caracter.lower() in ["a", "e", "i", "o", "u"]:
        return True
    else:
        return False

caracter = input("Digite un caracter: ")
print(verificar_vocal(caracter))


# 5. Escribir una función sum() y una función multip() que sumen y multipliquen
# respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería
# devolver 10 y multip([1,2,3,4]) debería devolver 24.

nums =[]
for i in range(4):
    num = int(input(f"Ingrese el {i+1}° número: "))
    nums.append(num)

def suma(nums):
    return sum(nums)

def multiplicacion(nums):
    resultado = 1
    for num in nums:
        resultado *= num
    return resultado

print("La suma de los numeros es : ", suma(nums))
print("La multiplicacion de los numeros es : ", multiplicacion(nums))
    




    
    
 