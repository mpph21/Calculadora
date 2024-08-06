import tkinter as tk
from tkinter import ttk, font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from model.funciones_graficar import graficar_funcion, insertar_texto
from view.botones_graficar import crear_boton, crear_pestana_botones, ModernButton

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

    ModernButton(frame_entrada, text="Graficar", command=lambda: graficar_funcion(funcion_entry, ax, canvas, fig), font=button_font).pack(fill=tk.X, pady=10)

    notebook = ttk.Notebook(frame_entrada)
    notebook.pack(fill=tk.BOTH, expand=True, pady=10)

    botones_basicos = [
        ('7', lambda entry: insertar_texto(entry, '7')), ('8', lambda entry: insertar_texto(entry, '8')), 
        ('9', lambda entry: insertar_texto(entry, '9')), ('+', lambda entry: insertar_texto(entry, '+')), 
        ('/', lambda entry: insertar_texto(entry, '/')), ('4', lambda entry: insertar_texto(entry, '4')), 
        ('5', lambda entry: insertar_texto(entry, '5')), ('6', lambda entry: insertar_texto(entry, '6')), 
        ('-', lambda entry: insertar_texto(entry, '-')), ('*', lambda entry: insertar_texto(entry, '*')), 
        ('1', lambda entry: insertar_texto(entry, '1')), ('2', lambda entry: insertar_texto(entry, '2')), 
        ('3', lambda entry: insertar_texto(entry, '3')), ('=', lambda entry: insertar_texto(entry, '=')), 
        ('^', lambda entry: insertar_texto(entry, '^')), ('0', lambda entry: insertar_texto(entry, '0')), 
        ('.', lambda entry: insertar_texto(entry, '.')), ('(', lambda entry: insertar_texto(entry, '(')), 
        (')', lambda entry: insertar_texto(entry, ')')), ('C', lambda entry: funcion_entry.delete(0, tk.END))
    ]
    tab_basico = crear_pestana_botones(notebook, funcion_entry, botones_basicos, '#2196F3', 4, 5, font=button_font)
    notebook.add(tab_basico, text="Básico")

    botones_trigo = [
        ('sin', lambda entry: insertar_texto(entry, 'sin(')), ('cos', lambda entry: insertar_texto(entry, 'cos(')), 
        ('tan', lambda entry: insertar_texto(entry, 'tan(')), ('asin', lambda entry: insertar_texto(entry, 'asin(')), 
        ('acos', lambda entry: insertar_texto(entry, 'acos(')), ('atan', lambda entry: insertar_texto(entry, 'atan('))
    ]
    tab_trigo = crear_pestana_botones(notebook, funcion_entry, botones_trigo, '#2196F3', 2, 3, font=button_font)
    notebook.add(tab_trigo, text="Trigonometría")

    botones_log = [
        ('ln', lambda entry: insertar_texto(entry, 'ln(')), ('log', lambda entry: insertar_texto(entry, 'log(')), 
        ('log2', lambda entry: insertar_texto(entry, 'log2(')), ('e', lambda entry: insertar_texto(entry, 'e')), 
        ('10^', lambda entry: insertar_texto(entry, '10^')), ('exp', lambda entry: insertar_texto(entry, 'exp('))
    ]
    tab_log = crear_pestana_botones(notebook, funcion_entry, botones_log, '#2196F3', 2, 3, font=button_font)
    notebook.add(tab_log, text="Log/Exp")

    botones_calculo = [
        ('d/dx', lambda entry: insertar_texto(entry, 'd/dx(')), ('∫', lambda entry: insertar_texto(entry, '∫(')), 
        ('lim', lambda entry: insertar_texto(entry, 'lim(')), ('sum', lambda entry: insertar_texto(entry, 'sum(')), 
        ('prod', lambda entry: insertar_texto(entry, 'prod('))
    ]
    tab_calculo = crear_pestana_botones(notebook, funcion_entry, botones_calculo, '#2196F3', 2, 3, font=button_font)
    notebook.add(tab_calculo, text="Cálculo")

    botones_varios = [
        ('|x|', lambda entry: insertar_texto(entry, 'abs(')), ('√', lambda entry: insertar_texto(entry, 'sqrt(')), 
        ('∛', lambda entry: insertar_texto(entry, 'cbrt(')), ('π', lambda entry: insertar_texto(entry, 'pi')), 
        ('%', lambda entry: insertar_texto(entry, '%')), ('mod', lambda entry: insertar_texto(entry, 'mod('))
    ]
    tab_varios = crear_pestana_botones(notebook, funcion_entry, botones_varios, '#2196F3', 2, 3, font=button_font)
    notebook.add(tab_varios, text="Varios")

    funcion_entry.bind("<KeyRelease>", lambda event: graficar_funcion(funcion_entry, ax, canvas, fig))
    
    return ventana_graficar
