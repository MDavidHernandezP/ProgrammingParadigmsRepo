# Código ejemplificando Names, Scopes, and Bindings.
"""
Name: Identifiers that allow us to refer to variables, constants, functions, types, operations, and so on.
Binding: An association of a name with an object.
Scope: The lifetime of a binding of a name to an object.
"""

# Name
variable_name = 25    # Variable name with global scope
list_name = [1, 2, 3, 4, 5]    # List name with global scope

def function_name(argument):    # Function name
    local_variable = 5    # Variable with local scope
    return argument ** local_variable

result = function_name(variable_name)    # Output
print(result)