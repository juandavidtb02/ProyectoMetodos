import numpy as np
import matplotlib.pyplot as plt
from sympy import Poly,symbols,lambdify
def generar_grafico(function):
    plt.clf()
    # Genera valores de x
    x = np.linspace(-5, 5, 400)
    x_symbol = symbols('x')
    # Calcula los valores de y usando la función
    func_np = lambdify(x_symbol, function, 'numpy')

    # Calcula los valores de y usando la función de NumPy
    y = func_np(x)

    # Encuentra las raíces de la ecuación
    roots = np.roots(Poly(function, x_symbol).all_coeffs())

    # Filtra solo las raíces reales
    real_roots = [root for root in roots if np.isreal(root)]

    # Crea el gráfico
    plt.plot(x, y, label=f'y = {function}')
    plt.xlabel('y')
    plt.ylabel('x')
    plt.title('Gráfico de la función')
    plt.grid(True)
    plt.legend()

    # Establece los límites en el eje y
    plt.ylim(-5, 5)

    # Agrega ejes X e Y
    plt.axhline(0, color='black', linewidth=0.7)  # Eje horizontal (Y)
    plt.axvline(0, color='black', linewidth=0.7)  # Eje vertical (X)

    # Marca los puntos donde cruza el eje X
    for root in real_roots:
        plt.scatter(root.real, 0, color='red', marker='o', label='Raíz')
        print("Raiz: " + str(root.real))
    plt.legend()

    # Guarda el gráfico como un archivo de imagen
    plt.savefig('grafico.png')
