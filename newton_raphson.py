from sympy import symbols,diff

def g(value,funcion):
  x = symbols('x')
  derivada = diff(funcion, x)
  return (derivada.subs(x, value))

def f(value,funcion):
  x = symbols('x')
  return funcion.subs(x, value)

def newton_raphson(x0, E,funcion):
    iterations = []
    x_values = []
    error_values = []

    x = x0 - (f(x0,funcion) / g(x0,funcion))
    error = (abs(x - x0) / abs(x)) * 100
    x_ant = x0

    iterations.append(0)
    x_values.append(x)
    error_values.append(error)

    iteration = 1

    while error > E:
        x_ant = x
        x = x - (f(x,funcion) / g(x,funcion))
        error = (abs(x - x_ant) / abs(x)) * 100

        iterations.append(iteration)
        x_values.append(x)
        error_values.append(error)

        iteration += 1

    return iterations,x_values,error_values