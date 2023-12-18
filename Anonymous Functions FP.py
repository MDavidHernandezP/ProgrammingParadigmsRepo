"""
Class Examples
"""
# Define a function that returns the sum of the square of two numbers.
def hipo(num1, num2):
    return (num1 * num1) + (num2 * num2)

print(hipo(2, 3))

# Using anonymous function.
suma = lambda x, y: x ** 2 + y ** 2
print(suma(2,3))

"""
Task
"""
# Exercise 1: Filter and transform with lambda functions.
numbers = [1,2,3,4,5]
even_lambda = list(filter(lambda x: x % 2 != 0, numbers))
squared_lambda = list(map(lambda x: x ** 2, even_lambda))
sum_lambda = sum(squared_lambda)
print(sum_lambda)

# Exercise 2: Sorting a list of Tuples. 
tuples = [("Juan", 25), ("Pablo", 30), ("Jose", 20)] 
sorted_lambda = sorted(tuples, key = lambda x: x[1])
print(sorted_lambda)

tuples = [("Jhon", 25), ("Mary", 30), ("Charlie", 20)]    # Probando con otros nombres.
sorted_lambda = sorted(tuples, key = lambda x: x[1])
print(sorted_lambda)