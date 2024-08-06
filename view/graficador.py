import tkinter as tk
from tkinter import ttk, messagebox, font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def abrir_ventana_graficar(ventana):
    ventana_graficar = tk.Toplevel(ventana)
    ventana_graficar.title("Graficador Avanzado")
    ventana_graficar.geometry("1300x750")

    # Frame para la gráfica (izquierda)
    frame_grafica = tk.Frame(ventana_graficar)
    frame_grafica.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Frame para la entrada de función y teclado (derecha)
    frame_entrada = tk.Frame(ventana_graficar)
    frame_entrada.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Crear figura y canvas para la gráfica
    fig, ax = plt.subplots(figsize=(8, 6))
    canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    # Añadir la barra de herramientas
    toolbar = NavigationToolbar2Tk(canvas, frame_grafica)
    toolbar.update()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    # Estilos
    button_font = font.Font(family="Times New Roman", size=14, weight="bold")
    entry_font = font.Font(family="Times New Roman", size=16)
    label_font = font.Font(family="Times New Roman", size=14, weight="bold")

    # Campo de entrada para la función
    tk.Label(frame_entrada, text="Función f(x):", font=label_font).pack(pady=(0, 5))
    funcion_entry = tk.Entry(frame_entrada, width=50, font=entry_font)
    funcion_entry.pack(pady=(0, 10), fill=tk.X)

    def insertar_texto(texto):
        funcion_entry.insert(tk.END, texto)

    def verificar_sintaxis(funcion):
        paren_abiertos = funcion.count('(')
        paren_cerrados = funcion.count(')')
        if paren_abiertos != paren_cerrados:
            return "Los paréntesis no están balanceados."
        return None

    def graficar_funcion():
        ax.clear()
        x_vals = np.linspace(-10, 10, 400)
        x = sp.Symbol('x')

        # Definir parámetros adicionales
        parametros = {'m': 1, 'b': 0}  # Puedes agregar más parámetros aquí

        funcion = funcion_entry.get()
        
        # Verificar errores de sintaxis
        error = verificar_sintaxis(funcion)
        if error:
            messagebox.showerror("Error", error)
            return

        try:
            # Convertir la función en una expresión simbólica
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

    def on_entry_change(event):
        graficar_funcion()

    # Estilo moderno para botones
    class ModernButton(tk.Button):
        def __init__(self, master, **kw):
            tk.Button.__init__(self, master=master, **kw)
            self.config(
                relief=tk.FLAT,
                bg="#2196F3",  # Azul
                fg="white",
                activebackground="#1976D2",  # Azul más oscuro
                activeforeground="white",
                highlightthickness=0,
                bd=0,
                padx=12,
                pady=6,
                font=button_font
            )
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)
            self.config(text=self.cget("text").lower())  # Convertir texto a minúsculas

        def on_enter(self, e):
            self['background'] = '#1976D2'

        def on_leave(self, e):
            self['background'] = '#2196F3'

    # Botón para graficar
    ModernButton(frame_entrada, text="Graficar", command=graficar_funcion).pack(fill=tk.X, pady=10)

    # Notebook para organizar los botones en pestañas
    notebook = ttk.Notebook(frame_entrada)
    notebook.pack(fill=tk.BOTH, expand=True, pady=10)

    # Función para crear botones modernos
    def crear_boton(parent, text, command, color='#2196F3', hover_color='#1976D2'):
        btn = ModernButton(parent, text=text, command=command, bg=color, activebackground=hover_color)
        btn.config(width=8, height=2)  # Ajuste de tamaño del botón
        return btn

    # Función para crear pestañas de botones
    def crear_pestana_botones(parent, botones, color, filas, columnas):
        frame = ttk.Frame(parent)
        for i, (texto, comando) in enumerate(botones):
            crear_boton(frame, texto, comando, color).grid(row=i//columnas, column=i%columnas, padx=4, pady=4, sticky="nsew")
        for i in range(filas):
            frame.grid_rowconfigure(i, weight=1)
        for i in range(columnas):
            frame.grid_columnconfigure(i, weight=1)
        return frame

    # Pestaña: Números y Operadores Básicos
    botones_basicos = [
        ('7', lambda: insertar_texto('7')), ('8', lambda: insertar_texto('8')), ('9', lambda: insertar_texto('9')), ('+', lambda: insertar_texto('+')), ('/', lambda: insertar_texto('/')),
        ('4', lambda: insertar_texto('4')), ('5', lambda: insertar_texto('5')), ('6', lambda: insertar_texto('6')), ('-', lambda: insertar_texto('-')), ('*', lambda: insertar_texto('*')),
        ('1', lambda: insertar_texto('1')), ('2', lambda: insertar_texto('2')), ('3', lambda: insertar_texto('3')), ('=', lambda: insertar_texto('=')), ('^', lambda: insertar_texto('^')),
        ('0', lambda: insertar_texto('0')), ('.', lambda: insertar_texto('.')), ('(', lambda: insertar_texto('(')), (')', lambda: insertar_texto(')')), ('C', lambda: funcion_entry.delete(0, tk.END))
    ]
    tab_basico = crear_pestana_botones(notebook, botones_basicos, '#2196F3', 4, 5)
    notebook.add(tab_basico, text="Básico")

    # Pestaña: Funciones Trigonométricas
    botones_trigo = [('sin', lambda: insertar_texto('sin(')), ('cos', lambda: insertar_texto('cos(')), ('tan', lambda: insertar_texto('tan(')),
                     ('asin', lambda: insertar_texto('asin(')), ('acos', lambda: insertar_texto('acos(')), ('atan', lambda: insertar_texto('atan('))]
    tab_trigo = crear_pestana_botones(notebook, botones_trigo, '#2196F3', 2, 3)
    notebook.add(tab_trigo, text="Trigonometría")

    # Pestaña: Logaritmos y Exponenciales
    botones_log = [('ln', lambda: insertar_texto('ln(')), ('log', lambda: insertar_texto('log(')), ('log2', lambda: insertar_texto('log2(')),
                   ('e', lambda: insertar_texto('e')), ('10^', lambda: insertar_texto('10^')), ('exp', lambda: insertar_texto('exp('))]
    tab_log = crear_pestana_botones(notebook, botones_log, '#2196F3', 2, 3)
    notebook.add(tab_log, text="Log/Exp")

    # Pestaña: Cálculo
    botones_calculo = [('d/dx', lambda: insertar_texto('d/dx(')), ('∫', lambda: insertar_texto('∫(')), ('lim', lambda: insertar_texto('lim(')),
                       ('sum', lambda: insertar_texto('sum(')), ('prod', lambda: insertar_texto('prod(')), ('diff', lambda: insertar_texto('diff('))]
    tab_calculo = crear_pestana_botones(notebook, botones_calculo, '#2196F3', 2, 3)
    notebook.add(tab_calculo, text="Cálculo")

    # Pestaña: Símbolos Matemáticos
    botones_simbolos = [(s, lambda s=s: insertar_texto(s)) for s in ['∞', '≠', '∧', '∨', '→', '↮', '×', '∥', '⊥', '∈', '⊂', '≪', '[', ']', '{', '}', '&', '@', '#', '$']]
    tab_simbolos = crear_pestana_botones(notebook, botones_simbolos, '#2196F3', 4, 5)
    notebook.add(tab_simbolos, text="Símbolos")

    # Pestaña: Constantes y Otros
    botones_otros = [('π', lambda: insertar_texto('π')), ('e', lambda: insertar_texto('e')), ('%', lambda: insertar_texto('%')), ('!', lambda: insertar_texto('!')),
                     ('°', lambda: insertar_texto('°')), ('≤', lambda: insertar_texto('≤')), ('≥', lambda: insertar_texto('≥')), (':', lambda: insertar_texto(':')),
                     (';', lambda: insertar_texto(';')), ("'", lambda: insertar_texto("'")), ('"', lambda: insertar_texto('"')), ('<', lambda: insertar_texto('<')),
                     ('>', lambda: insertar_texto('>')), ('←', lambda: insertar_texto('←')), ('...', lambda: insertar_texto('...'))]
    tab_otros = crear_pestana_botones(notebook, botones_otros, '#2196F3', 3, 5)
    notebook.add(tab_otros, text="Otros")

    # Pestaña: Teclado ABC
    botones_abc = [(l.lower(), lambda l=l: insertar_texto(l.lower())) for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    tab_abc = crear_pestana_botones(notebook, botones_abc, '#2196F3', 4, 7)
    notebook.add(tab_abc, text="ABC")

    funcion_entry.bind("<KeyRelease>", on_entry_change)
    
    return ventana_graficar
