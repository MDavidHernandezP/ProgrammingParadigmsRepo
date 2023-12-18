# 5. Case: Word LLenght Counter.
length_counter = lambda sentence: list(map(len, sentence.split()))    # Usando split para que detecte los espacios de la oración.
# Entonces utiliza el len para que cheque la longitud de cada palabra.
print(length_counter('Esbirrito te quiere'))    # Aplicando la función lambda, pasándole la oración.

# 7. Case: Sum of Squares.
mi_lista=[1,2,3,4,5,6]    # Lista de números.
#La funcion de lambda itera en cada numero en la lista de numeros y si es par lo eleva al cuadrado
sumEven = lambda numbers: sum([num**2 for num in numbers if num % 2 == 0])
print(sumEven(mi_lista))    # Imprimiendo la suma de los números pares al cuadrado.