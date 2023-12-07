from sympy import symbols, sympify

def funcion(funcion_str):
    x = symbols('x')

    try:
        funcion = sympify(funcion_str)
        return funcion

    except (SyntaxError, TypeError):
        return "Error: La función ingresada no es válida."