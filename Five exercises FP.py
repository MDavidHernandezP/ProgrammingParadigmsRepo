# Import math para el ejercicio 5 que estuvo insano.
import math

# Exercise 1: Find Prime Numbers.
listilla = [2, 3, 4, 5, 6, 7, 8, 9]
prime = lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1))
prime_lambda = list(filter(prime, listilla))
print(prime_lambda)

# Exercise 2: Map and Calculate Average.
listilla2 = [1, 2, 3, 4, 5] 
squared_lambda = sum(list(map(lambda x: x ** 2, listilla2))) / len(listilla2)
print(squared_lambda)

# Exercise 3: Sorting a List of Dictionaries.
personitas = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 20}]
sorted_lambda = sorted(personitas, key = lambda x: x['age'])
print(sorted_lambda)

# Exercise 4: Filtering Strings.
stranger_things = ["apple", "banana", "cherry", "date", "fig"]
filter_lambda = lambda x: (y for y in x if 'a' in y)
print(list(filter_lambda(stranger_things)))

# Exercise 5: Calculate Factorials
listilla3 = [1, 2, 3, 4, 5]
factorial_lambda = lambda x: [math.factorial(i) for i in listilla3]
print(factorial_lambda(listilla3))