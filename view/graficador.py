import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

def abrir_ventana_graficar(ventana):
    ventana_graficar = tk.Toplevel(ventana)
    ventana_graficar.title("Graficar")
    ventana_graficar.geometry("800x600")

    # Frame para los botones (izquierda)
    frame_botones = tk.Frame(ventana_graficar)
    frame_botones.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

    # Frame para la gráfica y entrada de parámetros (derecha)
    frame_grafica = tk.Frame(ventana_graficar)
    frame_grafica.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Crear figura y canvas para la gráfica
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    # Frame para entrada de parámetros
    frame_parametros = tk.Frame(frame_grafica)
    frame_parametros.pack(fill=tk.X, pady=10)

    def graficar_funcion(funcion, titulo, params=None):
        ax.clear()
        x = np.linspace(-10, 10, 400)
        if params:
            y = funcion(x, params)
        else:
            y = funcion(x)
        ax.plot(x, y)
        ax.set_title(titulo)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.grid(True)  # Añadir cuadrícula
        canvas.draw()

    def mostrar_parametros(tipo_funcion):
        for widget in frame_parametros.winfo_children():
            widget.destroy()

        if tipo_funcion in ["seno", "coseno", "tangente"]:
            tk.Label(frame_parametros, text="A (amplitud):").pack(side=tk.LEFT)
            a_entry = tk.Entry(frame_parametros)
            a_entry.pack(side=tk.LEFT)
            tk.Label(frame_parametros, text="ω (frecuencia):").pack(side=tk.LEFT)
            w_entry = tk.Entry(frame_parametros)
            w_entry.pack(side=tk.LEFT)
            tk.Label(frame_parametros, text="φ (fase):").pack(side=tk.LEFT)
            p_entry = tk.Entry(frame_parametros)
            p_entry.pack(side=tk.LEFT)
            
            if tipo_funcion == "seno":
                tk.Button(frame_parametros, text="Graficar", command=lambda: graficar_funcion(
                    lambda x, params: params['A'] * np.sin(params['w'] * x + params['p']),
                    "Gráfica del Seno",
                    {'A': float(a_entry.get()), 'w': float(w_entry.get()), 'p': float(p_entry.get())}
                )).pack(side=tk.LEFT)
            elif tipo_funcion == "coseno":
                tk.Button(frame_parametros, text="Graficar", command=lambda: graficar_funcion(
                    lambda x, params: params['A'] * np.cos(params['w'] * x + params['p']),
                    "Gráfica del Coseno",
                    {'A': float(a_entry.get()), 'w': float(w_entry.get()), 'p': float(p_entry.get())}
                )).pack(side=tk.LEFT)
            elif tipo_funcion == "tangente":
                tk.Button(frame_parametros, text="Graficar", command=lambda: graficar_funcion(
                    lambda x, params: params['A'] * np.tan(params['w'] * x + params['p']),
                    "Gráfica de la Tangente",
                    {'A': float(a_entry.get()), 'w': float(w_entry.get()), 'p': float(p_entry.get())}
                )).pack(side=tk.LEFT)

        elif tipo_funcion == "lineal":
            tk.Label(frame_parametros, text="m:").pack(side=tk.LEFT)
            m_entry = tk.Entry(frame_parametros)
            m_entry.pack(side=tk.LEFT)
            tk.Label(frame_parametros, text="b:").pack(side=tk.LEFT)
            b_entry = tk.Entry(frame_parametros)
            b_entry.pack(side=tk.LEFT)
            tk.Button(frame_parametros, text="Graficar", command=lambda: graficar_funcion(
                lambda x, p: p['m']*x + p['b'],
                "Gráfica Lineal (mx + b)",
                {'m': float(m_entry.get()), 'b': float(b_entry.get())}
            )).pack(side=tk.LEFT)

        elif tipo_funcion == "cuadratica":
            tk.Label(frame_parametros, text="a:").pack(side=tk.LEFT)
            a_entry = tk.Entry(frame_parametros)
            a_entry.pack(side=tk.LEFT)
            tk.Label(frame_parametros, text="b:").pack(side=tk.LEFT)
            b_entry = tk.Entry(frame_parametros)
            b_entry.pack(side=tk.LEFT)
            tk.Label(frame_parametros, text="c:").pack(side=tk.LEFT)
            c_entry = tk.Entry(frame_parametros)
            c_entry.pack(side=tk.LEFT)
            tk.Button(frame_parametros, text="Graficar", command=lambda: graficar_funcion(
                lambda x, p: p['a']*x**2 + p['b']*x + p['c'],
                "Gráfica Cuadrática (ax^2 + bx + c)",
                {'a': float(a_entry.get()), 'b': float(b_entry.get()), 'c': float(c_entry.get())}
            )).pack(side=tk.LEFT)

        elif tipo_funcion == "exponencial":
            tk.Label(frame_parametros, text="A:").pack(side=tk.LEFT)
            a_entry = tk.Entry(frame_parametros)
            a_entry.pack(side=tk.LEFT)
            tk.Label(frame_parametros, text="Base:").pack(side=tk.LEFT)
            base_entry = tk.Entry(frame_parametros)
            base_entry.pack(side=tk.LEFT)
            tk.Label(frame_parametros, text="B:").pack(side=tk.LEFT)
            b_entry = tk.Entry(frame_parametros)
            b_entry.pack(side=tk.LEFT)
            tk.Label(frame_parametros, text="C:").pack(side=tk.LEFT)
            c_entry = tk.Entry(frame_parametros)
            c_entry.pack(side=tk.LEFT)
            tk.Button(frame_parametros, text="Graficar", command=lambda: graficar_funcion(
                lambda x, p: p['A'] * np.power(p['base'], p['B']*x) + p['C'],
                "Gráfica Exponencial (A * base^(Bx) + C)",
                {'A': float(a_entry.get()), 'base': float(base_entry.get()), 
                'B': float(b_entry.get()), 'C': float(c_entry.get())}
            )).pack(side=tk.LEFT)

        elif tipo_funcion == "logaritmica":
            tk.Label(frame_parametros, text="A:").pack(side=tk.LEFT)
            a_entry = tk.Entry(frame_parametros)
            a_entry.pack(side=tk.LEFT)
            tk.Label(frame_parametros, text="Base:").pack(side=tk.LEFT)
            base_entry = tk.Entry(frame_parametros)
            base_entry.pack(side=tk.LEFT)
            tk.Label(frame_parametros, text="B:").pack(side=tk.LEFT)
            b_entry = tk.Entry(frame_parametros)
            b_entry.pack(side=tk.LEFT)
            tk.Label(frame_parametros, text="C:").pack(side=tk.LEFT)
            c_entry = tk.Entry(frame_parametros)
            c_entry.pack(side=tk.LEFT)
            tk.Button(frame_parametros, text="Graficar", command=lambda: graficar_funcion(
                lambda x, p: p['A'] * (np.log(p['B']*x) / np.log(p['base'])) + p['C'],
                "Gráfica Logarítmica (A * log_base(Bx) + C)",
                {'A': float(a_entry.get()), 'base': float(base_entry.get()), 
                'B': float(b_entry.get()), 'C': float(c_entry.get())}
            )).pack(side=tk.LEFT)
            
    funciones = [
        ("Lineal", lambda: mostrar_parametros("lineal")),
        ("Cuadrática", lambda: mostrar_parametros("cuadratica")),
        ("Seno", lambda: mostrar_parametros("seno")),
        ("Coseno", lambda: mostrar_parametros("coseno")),
        ("Tangente", lambda: mostrar_parametros("tangente")),
        ("Exponencial", lambda: mostrar_parametros("exponencial")),
        ("Logarítmica", lambda: mostrar_parametros("logaritmica"))
    ]

    for texto, comando in funciones:
        tk.Button(frame_botones, text=texto, command=comando).pack(fill=tk.X, pady=5)

    return ventana_graficar