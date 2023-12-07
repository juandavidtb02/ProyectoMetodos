from sympy import symbols

def ea(xr_n, xr_a):
    return abs((xr_n - xr_a) / xr_n) * 100


def biseccion(xi,xu):
  return (xi+xu)/2

def f(value,funcion):
  x = symbols('x')
  return funcion.subs(x, value)

def iterar_biseccion(xi,xu,obj,funcion):

  xr_list = []
  xi_list = []
  xu_list = []
  ea_list = []
  et_list = []
  i = 0
  i_list = []
  i_list.append(i)

  xr = (xi+xu)/2
  ea_value = 100
  ea_list.append(ea_value)


  xr_list.append(xr)
  xi_list.append(xi)
  xu_list.append(xu)
  while ea_value > obj:

    if f(xr,funcion)*f(xi,funcion) < 0:
      xu = xr
    elif f(xr,funcion)*f(xi,funcion) > 0:
      xi = xr
    else:
      ea_value = 0

    xr = biseccion(xi,xu)
    ea_value = ea(xr,xr_list[i])
    ea_list.append(ea_value)
    # et = abs(0.4181006 - xr)
    # et_list.append(et)
    i = i + 1
    i_list.append(i)
    xr_list.append(xr)
    xi_list.append(xi)
    xu_list.append(xu)

  headers = ["i","xr", "xu", "xi","ea (%)"]
  return i_list, xr_list, xu_list, xi_list, ea_list


