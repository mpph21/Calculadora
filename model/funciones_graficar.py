import numpy as np
import sympy as sp
import tkinter as tk
from matplotlib import pyplot as plt
from tkinter import messagebox
from model.client_experience import balancear_parentesis

# Variable global para llevar la cuenta de los puntos
num_puntos = 0
puntos_agregados = []

def insertar_texto(entry, texto):
    entry.insert(tk.END, texto)
    contenido = entry.get()
    contenido_balanceado = balancear_parentesis(contenido)
    entry.delete(0, tk.END)
    entry.insert(0, contenido_balanceado)

def on_click(event, ax, canvas, coordenadas_widget):
    global num_puntos

    if event.inaxes == ax:
        if num_puntos < 10:
            x, y = event.xdata, event.ydata
            ax.plot(x, y, 'bo', markersize=5)
            canvas.draw()

            # Actualizar el widget de texto con las coordenadas
            coordenadas_widget.config(state=tk.NORMAL)
            coordenadas_widget.insert(tk.END, f"({x:.2f}, {y:.2f})\n")
            coordenadas_widget.config(state=tk.DISABLED)

            num_puntos += 1
        else:
            # Mostrar un mensaje de alerta si se ha alcanzado el límite de 10 puntos
            tk.messagebox.showinfo("Límite alcanzado", "Se ha alcanzado el límite de 10 puntos.")

def graficar_funcion(funcion_entry, ax, canvas, fig):
    ax.clear()
    x_vals = np.linspace(-10, 10, 400)  # Valores de x
    x, y = sp.symbols('x y')
    
    funcion = funcion_entry.get()  # Obtener la función desde la entrada
    
    try:
        if funcion.startswith('integrate('):
            inner_func = funcion[funcion.index('(')+1:funcion.rindex(',')]
            f = sp.sympify(inner_func)
            F = sp.integrate(f, x)
            F_lambdified = sp.lambdify(x, F, modules=['numpy', 'sympy'])
            y_vals = F_lambdified(x_vals) - F_lambdified(0)
        
        elif funcion.startswith('diff('):
            inner_func = funcion[funcion.index('(')+1:funcion.rindex(',')]
            f = sp.sympify(inner_func)
            df = sp.diff(f, x)
            df_lambdified = sp.lambdify(x, df, modules=['numpy', 'sympy'])
            y_vals = df_lambdified(x_vals)
        
        elif funcion.startswith('limit('):
            # Para límites, graficamos la función original
            inner_func = funcion[funcion.index('(')+1:funcion.index(',')]
            f = sp.sympify(inner_func)
            f_lambdified = sp.lambdify(x, f, modules=['numpy', 'sympy'])
            y_vals = f_lambdified(x_vals)
            # Calculamos el límite
            limit_point = sp.sympify(funcion[funcion.rindex(',')+1:funcion.rindex(')')])
            limit_value = sp.limit(f, x, limit_point)
            ax.plot(limit_point, limit_value, 'ro', markersize=10)  # Marcamos el punto del límite
        
        else:
            if '=' in funcion and 'y' in funcion:
                h, k, r = extraer_parametros_circulo(funcion)
                graficar_circulo(h, k, r, ax, canvas, fig)
                return
            else:
                # Graficar polinomios
                f = sp.sympify(funcion)
                f_lambdified = sp.lambdify(x, f, modules=['numpy', 'sympy'])
                y_vals = f_lambdified(x_vals)
        
        ax.plot(x_vals, y_vals, color='#FF69B4', linestyle='-', markersize=5, alpha=0.7)
        
        ax.set_title("Gráfica de la Función")
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.grid(True)
        ax.axhline(y=0, color='black', linestyle='-', linewidth=1.5)
        ax.axvline(x=0, color='black', linestyle='-', linewidth=1.5)
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')
        canvas.draw()
    except (sp.SympifyError, TypeError, ValueError) as e:
        # No hacer nada, se manejará el error en la función que llama a graficar_funcion
        pass

def graficar_funcion_boton(funcion_entry, ax, canvas, fig, coordenadas_widget):
    try:
        graficar_funcion(funcion_entry, ax, canvas, fig)
    except (sp.SympifyError, TypeError, ValueError) as e:
        # Mostrar un mensaje de error más amigable
        messagebox.showerror("Error", f"Error en la función: {e}")
        print(f"Error en la función: {e}")  # Para depuración, asegura que se esté capturando la excepción
        # Restablecer la gráfica y el widget de coordenadas a un estado conocido
        ax.clear()
        ax.set_title("Gráfica de la Función")
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.grid(True)
        ax.axhline(y=0, color='black', linestyle='-', linewidth=1.5)
        ax.axvline(x=0, color='black', linestyle='-', linewidth=1.5)
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')
        canvas.draw()
        # Limpiar el widget de texto de coordenadas
        coordenadas_widget.config(state=tk.NORMAL)
        coordenadas_widget.delete("1.0", tk.END)
        coordenadas_widget.config(state=tk.DISABLED)


def insertar_ecuacion_circulo(entry, h, k, r):
    ecuacion = f'(x-{h})**2 + (y-{k})**2 = {r}**2'
    entry.delete(0, tk.END)
    entry.insert(0, ecuacion)

def extraer_parametros_circulo(funcion):
    try:
        # Eliminar espacios en blanco y dividir en las dos partes de la ecuación
        funcion = funcion.replace(' ', '')
        left_side, right_side = funcion.split('=')
        
        # Obtener los valores de h, k y r
        x_term, y_term = left_side.split('+')
        
        # Extraer los valores
        h = float(x_term.split('-')[1].split(')')[0])
        k = float(y_term.split('-')[1].split(')')[0])
        r = float(sp.sqrt(sp.sympify(right_side)))
        
        return h, k, r
    except Exception as e:
        raise ValueError(f"Error al extraer parámetros: {e}")

def graficar_circulo(h, k, r, ax, canvas, fig):
    ax.clear()
    theta = np.linspace(0, 2 * np.pi, 1000)
    x_vals = h + r * np.cos(theta)
    y_vals = k + r * np.sin(theta)
    
    ax.plot(x_vals, y_vals, color='#FF69B4', linestyle='-', markersize=5, alpha=0.7)
    ax.set_aspect('equal', 'box')
    ax.set_title("Gráfica del Círculo")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    ax.axhline(y=0, color='black', linestyle='-', linewidth=1.5)
    ax.axvline(x=0, color='black', linestyle='-', linewidth=1.5)
    
    # Ajustar los límites de los ejes
    ax.set_xlim(h - r - 1, h + r + 1)
    ax.set_ylim(k - r - 1, k + r + 1)
    
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    canvas.draw()
