import tkinter as tk
from tkinter import Entry, Label, Button, Menu, Toplevel, ttk
from PIL import Image, ImageTk
from metodo_grafico import generar_grafico
from convertir_funcion import funcion
from biseccion import iterar_biseccion
from newton_raphson import newton_raphson

def obtener_resultado():
    funcion_str = entrada_funcion.get()
    resultado = funcion(funcion_str)

    # Mostrar el resultado
    etiqueta_resultado.config(text=f"El resultado es: {resultado}")

    # Crear el menú
    menu = Menu(ventana, tearoff=0)
    menu.add_command(label="Metodo grafico", command=mostrar_grafico)
    menu.add_command(label="Metodo biseccion", command=opcion_2_menu)
    menu.add_command(label="Metodo Newton-Raphson", command=opcion_3_menu)

    # Mostrar el menú en las coordenadas actuales del ratón
    menu.post(ventana.winfo_pointerx(), ventana.winfo_pointery())

def mostrar_grafico():
    funcion_str = entrada_funcion.get()
    resultado = funcion(funcion_str)

    # Generar y mostrar el gráfico
    generar_grafico(resultado)
    mostrar_imagen_tkinter()

def mostrar_tabla_resultados(i_list, xr_list, xu_list, xi_list, ea_list):
    # Crear una nueva ventana para la tabla
    ventana_tabla = Toplevel(ventana)
    ventana_tabla.title("Resultados de Bisección")

    # Crear el widget Treeview para la tabla
    tabla_resultados = ttk.Treeview(ventana_tabla)

    # Configurar las columnas de la tabla
    tabla_resultados["columns"] = ("i", "xr", "xu", "xi", "ea (%)")

    # Configurar las cabeceras de las columnas
    tabla_resultados.heading("i", text="i")
    tabla_resultados.heading("xr", text="xr")
    tabla_resultados.heading("xu", text="xu")
    tabla_resultados.heading("xi", text="xi")
    tabla_resultados.heading("ea (%)", text="ea (%)")

    # Agregar los datos a la tabla
    for i in range(len(i_list)):
        tabla_resultados.insert("", i, values=(i_list[i], xr_list[i], xu_list[i], xi_list[i], ea_list[i]))

    # Mostrar la tabla
    tabla_resultados.pack()

def mostrar_tabla(xi,xu,obj):
    resultado = funcion(entrada_funcion.get())

    # Obtener los resultados de la función iterar_biseccion
    i_list, xr_list, xu_list, xi_list, ea_list = iterar_biseccion(float(xi), float(xu), float(obj), resultado)

    # Mostrar la tabla con los resultados
    mostrar_tabla_resultados(i_list, xr_list, xu_list, xi_list, ea_list)

def mostrar_tabla_punto(x,e):
    resultado = funcion(entrada_funcion.get())
    iterations,x_values,error_values = newton_raphson(float(x), float(e), resultado)

    # Crear una nueva ventana para la tabla
    ventana_tabla = Toplevel(ventana)
    ventana_tabla.title("Resultados de Newton-Raphson")

    # Crear el widget Treeview para la tabla
    tabla_resultados = ttk.Treeview(ventana_tabla)

    # Configurar las columnas de la tabla
    tabla_resultados["columns"] = ("i", "x", "Error")

    # Configurar las cabeceras de las columnas
    tabla_resultados.heading("i", text="i")
    tabla_resultados.heading("x", text="x")
    tabla_resultados.heading("Error", text="Error")

    # Agregar los datos a la tabla
    for i in range(len(iterations)):
        tabla_resultados.insert("", i, values=(iterations[i],x_values[i],error_values[i]))

    # Mostrar la tabla
    tabla_resultados.pack()

def opcion_3_menu():
    ventana_opcion_3 = Toplevel(ventana)
    ventana_opcion_3.title("Metodo Newton - Raphson")

    # Crear elementos de la interfaz para la opción 2
    label1 = Label(ventana_opcion_3, text="x0")
    label1.pack()
    entry1 = Entry(ventana_opcion_3)
    entry1.pack()

    label2 = Label(ventana_opcion_3, text="E")
    label2.pack()
    entry2 = Entry(ventana_opcion_3)
    entry2.pack()

    boton_calcular_opcion_3 = Button(ventana_opcion_3, text="Calcular",command=lambda: mostrar_tabla_punto(entry1.get(), entry2.get()))
    boton_calcular_opcion_3.pack()

def opcion_2_menu():
    ventana_opcion_2 = Toplevel(ventana)
    ventana_opcion_2.title("Biseccion")

    # Crear elementos de la interfaz para la opción 2
    label1 = Label(ventana_opcion_2, text="Xi")
    label1.pack()
    entry1 = Entry(ventana_opcion_2)
    entry1.pack()

    label2 = Label(ventana_opcion_2, text="Xu")
    label2.pack()
    entry2 = Entry(ventana_opcion_2)
    entry2.pack()

    label3 = Label(ventana_opcion_2, text="Objetivo")
    label3.pack()
    entry3 = Entry(ventana_opcion_2)
    entry3.pack()

    boton_calcular_opcion_2 = Button(ventana_opcion_2, text="Calcular", command=lambda: mostrar_tabla(entry1.get(), entry2.get(), entry3.get()))
    boton_calcular_opcion_2.pack()






def mostrar_imagen_tkinter():
    # Abrir la imagen con PIL
    imagen = Image.open('grafico.png')

    # Mostrar la imagen en una ventana Tkinter
    ventana_grafico = tk.Toplevel()
    ventana_grafico.title("Gráfico de la Función")

    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta_imagen = tk.Label(ventana_grafico, image=imagen_tk)
    etiqueta_imagen.pack()

    # Iniciar el bucle de eventos
    ventana_grafico.mainloop()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Proyecto de Métodos Numéricos")

# Añadir márgenes a la ventana
ventana.geometry("400x200")
ventana.configure(padx=20, pady=20)

# Crear elementos de la interfaz
etiqueta_funcion = Label(ventana, text="Ingresa la función en términos de 'x':")
etiqueta_funcion.pack()

entrada_funcion = Entry(ventana, width=30)
entrada_funcion.pack(pady=10)

boton_calcular = Button(ventana, text="Calcular", command=obtener_resultado)
boton_calcular.pack(pady=10)

etiqueta_resultado = Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()
