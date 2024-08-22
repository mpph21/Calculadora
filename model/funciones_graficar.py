import numpy as np
import sympy as sp
import tkinter as tk
from matplotlib import pyplot as plt
from tkinter import messagebox
from model.client_experience import balancear_parentesis

# Variable global para llevar la cuenta de los puntos
num_puntos = 0
puntos_agregados = []
ultimo_click = None

def insertar_texto(entry, texto):
    entry.insert(tk.END, texto)
    contenido = entry.get()
    contenido_balanceado = balancear_parentesis(contenido)
    entry.delete(0, tk.END)
    entry.insert(0, contenido_balanceado)

def on_click(event, ax, canvas, coordenadas_widget):
    global num_puntos, ultimo_click

    if event.inaxes == ax:
        if ultimo_click is None:
            # Almacenar el primer clic
            ultimo_click = (event.xdata, event.ydata)
        else:
            # Verificar si el segundo clic está lo suficientemente cerca del primero
            x1, y1 = ultimo_click
            x2, y2 = event.xdata, event.ydata
            distancia = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            if distancia < 0.1:  # Umbral de distancia para considerar los dos clics como un doble clic
                if num_puntos < 10:
                    ax.plot(x2, y2, 'bo', markersize=5)
                    canvas.draw()

                    # Actualizar el widget de texto con las coordenadas
                    coordenadas_widget.config(state=tk.NORMAL)
                    coordenadas_widget.insert(tk.END, f"({x2:.2f}, {y2:.2f})\n")
                    coordenadas_widget.config(state=tk.DISABLED)

                    num_puntos += 1
                else:
                    # Mostrar un mensaje de alerta si se ha alcanzado el límite de 10 puntos
                    tk.messagebox.showinfo("Límite alcanzado", "Se ha alcanzado el límite de 10 puntos.")
                
                # Reiniciar el último clic
                ultimo_click = None
            else:
                # Si la distancia es grande, considerar este como un nuevo primer clic
                ultimo_click = (x2, y2)

def borrar_puntos(ax, canvas, coordenadas_widget):
    # Limpiar el widget de coordenadas
    coordenadas_widget.config(state=tk.NORMAL)
    coordenadas_widget.delete('1.0', tk.END)
    coordenadas_widget.config(state=tk.DISABLED)

    # Eliminar los puntos de la gráfica
    ax.clear()
    
    # Redibujar la gráfica en blanco
    canvas.draw()

    # Reiniciar el contador de puntos y el último clic
    global num_puntos, ultimo_click
    num_puntos = 0
    ultimo_click = None
            

def graficar_funcion(funcion_entry, ax, canvas, fig):
    ax.clear()
    x_vals = np.linspace(-10, 10, 400)  # Reducido para simplificar
    x = sp.symbols('x')
    
    funcion = funcion_entry.get()  # Obtener la función desde la entrada
    
    try:
        # Definir una función lambda para manejar errores en el cálculo
        def safe_lambdify(expr):
            try:
                f_lambdified = sp.lambdify(x, expr, modules=['numpy', 'sympy'])
                return f_lambdified
            except Exception as e:
                print(f"Error al lambdificar la expresión: {e}")
                return None
        
        # Inicializar y_vals
        y_vals = np.zeros_like(x_vals)
        
        if funcion.startswith('integrate('):
            inner_func = funcion[funcion.index('(')+1:funcion.rindex(',')]
            f = sp.sympify(inner_func)
            F = sp.integrate(f, x)
            F_lambdified = safe_lambdify(F)
            if F_lambdified:
                y_vals = F_lambdified(x_vals) - F_lambdified(0)
            ax.set_title("Gráfica de la Integral")
        
        elif funcion.startswith('diff('):
            inner_func = funcion[funcion.index('(')+1:funcion.rindex(',')]
            variable = funcion[funcion.rindex(',')+1:funcion.rfind(')')]
            f = sp.sympify(inner_func)
            var = sp.symbols(variable)
            df = sp.diff(f, var)
            df_lambdified = safe_lambdify(df)
            if df_lambdified:
                y_vals = df_lambdified(x_vals)
            ax.set_title("Gráfica de la Derivada")
        
        elif funcion.startswith('limit('):
            inner_func = funcion[funcion.index('(')+1:funcion.index(',')]
            f = sp.sympify(inner_func)
            limit_point = sp.sympify(funcion[funcion.rfind(',')+1:funcion.rfind(')')])
            f_lambdified = safe_lambdify(f)
            if f_lambdified:
                y_vals = f_lambdified(x_vals)
                limit_value = sp.limit(f, x, limit_point)
                ax.plot(limit_point, limit_value, 'ro', markersize=10)  # Marcamos el punto del límite
            ax.set_title("Gráfica con Límite")
        
        elif 'log(' in funcion:
            f = sp.sympify(funcion)
            f_lambdified = safe_lambdify(f)
            if f_lambdified:
                y_vals = f_lambdified(x_vals)
            ax.set_title("Gráfica del Logaritmo")
        
        elif '=' in funcion and 'y' in funcion:
            # Extraer parámetros de la ecuación de la circunferencia
            h, k, r = extraer_parametros_circulo(funcion)
            graficar_circulo(h, k, r, ax, canvas, fig)
            return
        
        else:
            f = sp.sympify(funcion)
            f_lambdified = safe_lambdify(f)
            if f_lambdified:
                y_vals = f_lambdified(x_vals)
        
        # Verificar que x_vals y y_vals tienen la misma longitud
        if len(x_vals) != len(y_vals):
            raise ValueError("x_vals y y_vals deben tener la misma longitud.")
        
        # Graficar la función si no es circunferencia
        if '=' not in funcion or 'y' not in funcion:
            ax.plot(x_vals, y_vals, color='#FF69B4', linestyle='-', markersize=5, alpha=0.7)
        
        # Ajustar límites para los ejes
        x_min, x_max = x_vals.min(), x_vals.max()
        y_min, y_max = np.nanmin(y_vals), np.nanmax(y_vals)
        
        # Añadir un margen a los límites de y para mejorar la visualización
        y_range = y_max - y_min
        y_buffer = 0.1 * y_range if y_range != 0 else 1  # Evitar división por cero
        
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(max(y_min - y_buffer, -10), min(y_max + y_buffer, 10))
        
        ax.set_title("Gráfica de la Función")
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.grid(True)
        ax.axhline(y=0, color='black', linestyle='-', linewidth=1.5)
        ax.axvline(x=0, color='black', linestyle='-', linewidth=1.5)
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')
        plt.tight_layout()
        canvas.draw()
    except Exception as e:
        print(f"Error al graficar la función: {e}")
        ax.set_title("Error al graficar la función")
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.grid(False)
        ax.axhline(y=0, color='black', linestyle='-', linewidth=1.5)
        ax.axvline(x=0, color='black', linestyle='-', linewidth=1.5)
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')
        plt.tight_layout()
        canvas.draw()


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