# Define global scope variable
global_scope_variable = "I am global scope variable"


def function_with_own_scope():
    # Define function scope variable
    function_scope_variable = "I am function scope variable"
    print(function_scope_variable)
    # We can use global scope variables in function scope
    print(global_scope_variable)

def another_function():
    print(global_scope_variable)
    # We can's use variable from scope of another function
    print(function_scope_variable)


print(global_scope_variable)
# Use global scope variable in global scope print()

# Just comment the print() to run code
print(function_scope_variable) - this will be interpreted with an error
# We can't use function scope variables in global



function_with_own_scope()
# Call the function to show that we can use global and function scope variables in function