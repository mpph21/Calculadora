import numpy as np
import sympy as sp
import tkinter as tk
from matplotlib import pyplot as plt
from tkinter import messagebox

def insertar_texto(entry, texto):
    entry.insert(tk.END, texto)

def verificar_sintaxis(funcion):
    paren_abiertos = funcion.count('(')
    paren_cerrados = funcion.count(')')
    if paren_abiertos != paren_cerrados:
        return "Los paréntesis no están balanceados."
    return None

def graficar_funcion(funcion_entry, ax, canvas, fig):
    ax.clear()
    x_vals = np.linspace(-10, 10, 400)
    x = sp.Symbol('x')

    parametros = {'m': 1, 'b': 0}  # Puedes agregar más parámetros aquí

    funcion = funcion_entry.get()
    
    error = verificar_sintaxis(funcion)
    if error:
        messagebox.showerror("Error", error)
        return

    try:
        f = sp.sympify(funcion, locals=parametros)
        f_lambdified = sp.lambdify(x, f, 'numpy')
        y_vals = f_lambdified(x_vals)
        ax.plot(x_vals, y_vals, color='#FF69B4', linestyle='-', markersize=5, alpha=0.7)

        ax.set_title("Gráfica de la Función")
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.grid(True)
        ax.axhline(y=0, color='white', linestyle='-', linewidth=1.5)
        ax.axvline(x=0, color='white', linestyle='-', linewidth=1.5)
        fig.patch.set_facecolor('#222222')
        ax.set_facecolor('#222222')
        canvas.draw()
    except (sp.SympifyError, TypeError, ValueError) as e:
        messagebox.showerror("Error", f"Error en la función: {e}")