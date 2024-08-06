import tkinter as tk
from tkinter import ttk, font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from model.funciones_graficar import graficar_funcion
from view.botones_graficar import crear_pestana_botones, botones_basicos, botones_trigo, botones_log, botones_calculo, botones_varios, ModernButton

def abrir_ventana_graficar(ventana):
    ventana_graficar = tk.Toplevel(ventana)
    ventana_graficar.title("Graficador Avanzado")
    ventana_graficar.geometry("1300x750")

    frame_grafica = tk.Frame(ventana_graficar)
    frame_grafica.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    frame_entrada = tk.Frame(ventana_graficar)
    frame_entrada.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    fig, ax = plt.subplots(figsize=(8, 6))
    canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    toolbar = NavigationToolbar2Tk(canvas, frame_grafica)
    toolbar.update()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    button_font = font.Font(family="Times New Roman", size=14, weight="bold")
    entry_font = font.Font(family="Times New Roman", size=16)
    label_font = font.Font(family="Times New Roman", size=14, weight="bold")

    tk.Label(frame_entrada, text="Función f(x):", font=label_font).pack(pady=(0, 5))
    funcion_entry = tk.Entry(frame_entrada, width=50, font=entry_font)
    funcion_entry.pack(pady=(0, 10), fill=tk.X)

    ModernButton(frame_entrada, text="Graficar", command=lambda: graficar_funcion(funcion_entry, ax, canvas, fig), font=button_font).pack(pady=(0, 10))

    notebook = ttk.Notebook(frame_entrada)
    notebook.pack(expand=True, fill=tk.BOTH)

    tab_basico = crear_pestana_botones(notebook, funcion_entry, botones_basicos, '#2196F3', 4, 5, font=button_font)
    notebook.add(tab_basico, text="Básico")

    tab_trigo = crear_pestana_botones(notebook, funcion_entry, botones_trigo, '#2196F3', 2, 3, font=button_font)
    notebook.add(tab_trigo, text="Trigonometría")

    tab_log = crear_pestana_botones(notebook, funcion_entry, botones_log, '#2196F3', 2, 3, font=button_font)
    notebook.add(tab_log, text="Log/Exp")

    tab_calculo = crear_pestana_botones(notebook, funcion_entry, botones_calculo, '#2196F3', 2, 3, font=button_font)
    notebook.add(tab_calculo, text="Cálculo")

    tab_varios = crear_pestana_botones(notebook, funcion_entry, botones_varios, '#2196F3', 2, 3, font=button_font)
    notebook.add(tab_varios, text="Varios")

    funcion_entry.bind("<KeyRelease>", lambda event: graficar_funcion(funcion_entry, ax, canvas, fig))

    return ventana_graficar