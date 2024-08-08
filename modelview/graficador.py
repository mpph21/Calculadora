import tkinter as tk
from tkinter import ttk, font, Menu
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from model.funciones_graficar import graficar_funcion, graficar_circulo, insertar_ecuacion_circulo
from view.botones_graficar import crear_pestana_botones, botones_basicos, botones_trigo, botones_log, botones_calculo, botones_varios, ModernButton

def insertar_funcion(entry, funcion):
    entry.delete(0, tk.END)
    entry.insert(0, funcion)

def abrir_ventana_graficar(ventana):
    ventana_graficar = tk.Toplevel(ventana)
    ventana_graficar.title("Graficador Avanzado")
    ventana_graficar.geometry("1300x750")
    ventana_graficar.configure(bg='#2E2E2E')  # Fondo oscuro

    # Frame para la gráfica
    frame_grafica = tk.Frame(ventana_graficar, bg='#2E2E2E')
    frame_grafica.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Frame para la entrada y controles
    frame_entrada = tk.Frame(ventana_graficar, bg='#2E2E2E')
    frame_entrada.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Crear figura y ejes para la gráfica
    fig, ax = plt.subplots(figsize=(8, 6))
    canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    # Crear la barra de herramientas para la figura
    toolbar = NavigationToolbar2Tk(canvas, frame_grafica)
    toolbar.update()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    # Configuración de fuentes
    button_font = font.Font(family="Times New Roman", size=14, weight="bold")
    entry_font = font.Font(family="Times New Roman", size=16)
    label_font = font.Font(family="Times New Roman", size=14, weight="bold")

    # Entrada para la función
    tk.Label(frame_entrada, text="Función f(x):", font=label_font, fg="white", bg='#2E2E2E').grid(row=0, column=0, padx=5, pady=(0, 5), sticky='w')
    funcion_entry = tk.Entry(frame_entrada, width=50, font=entry_font, bg="#4A4A4A", fg="white", insertbackground='white')
    funcion_entry.grid(row=1, column=0, padx=5, pady=(0, 10), sticky='ew')

    # Botón para graficar la función
    ModernButton(frame_entrada, text="Graficar Función", command=lambda: graficar_funcion(funcion_entry, ax, canvas, fig), font=button_font).grid(row=2, column=0, padx=5, pady=(0, 10), sticky='ew')

    # Configuración del menú
    menu_bar = Menu(ventana_graficar)
    ventana_graficar.config(menu=menu_bar)

    funciones_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Funciones", menu=funciones_menu)

    # Opciones del menú de funciones
    funciones_menu.add_command(label="Seno", command=lambda: insertar_funcion(funcion_entry, "sin(x)"))
    funciones_menu.add_command(label="Coseno", command=lambda: insertar_funcion(funcion_entry, "cos(x)"))
    funciones_menu.add_command(label="Tangente", command=lambda: insertar_funcion(funcion_entry, "tan(x)"))
    funciones_menu.add_command(label="Logaritmo Natural", command=lambda: insertar_funcion(funcion_entry, "ln(x)"))
    funciones_menu.add_command(label="Logaritmo Base 10", command=lambda: insertar_funcion(funcion_entry, "log(x)"))
    funciones_menu.add_command(label="Exponencial", command=lambda: insertar_funcion(funcion_entry, "exp(x)"))
    funciones_menu.add_command(label="Derivada", command=lambda: insertar_funcion(funcion_entry, "diff(f(x), x)"))
    funciones_menu.add_command(label="Integral", command=lambda: insertar_funcion(funcion_entry, "integrate(f(x), x)"))
    funciones_menu.add_command(label="Límite", command=lambda: insertar_funcion(funcion_entry, "limit(f(x), x, a)"))
    funciones_menu.add_command(label="Círculo", command=lambda: insertar_ecuacion_circulo(funcion_entry, 0, 0, 5))

    # Crear las pestañas de botones
    notebook = ttk.Notebook(frame_entrada)
    notebook.grid(row=3, column=0, padx=5, pady=(10, 5), sticky='nsew')

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TNotebook", background="#2E2E2E")
    style.configure("TNotebook.Tab", background="#4A4A4A", foreground="white")
    style.map("TNotebook.Tab", background=[("selected", "#2E2E2E")], foreground=[("selected", "white")])

    tab_basico = crear_pestana_botones(notebook, funcion_entry, botones_basicos, '#D02090', 4, 5, font=button_font)
    notebook.add(tab_basico, text="Básico")

    tab_trigo = crear_pestana_botones(notebook, funcion_entry, botones_trigo, '#D02090', 2, 3, font=button_font)
    notebook.add(tab_trigo, text="Trigonometría")

    tab_log = crear_pestana_botones(notebook, funcion_entry, botones_log, '#D02090', 2, 3, font=button_font)
    notebook.add(tab_log, text="Log/Exp")

    tab_calculo = crear_pestana_botones(notebook, funcion_entry, botones_calculo, '#D02090', 2, 3, font=button_font)
    notebook.add(tab_calculo, text="Cálculo")

    tab_varios = crear_pestana_botones(notebook, funcion_entry, botones_varios, '#D02090', 2, 3, font=button_font)
    notebook.add(tab_varios, text="Varios")

    # Ajustar el grid
    frame_entrada.grid_rowconfigure(3, weight=1)
    frame_entrada.grid_columnconfigure(0, weight=1)

    # Graficar la función en cada cambio en la entrada
    funcion_entry.bind("<KeyRelease>", lambda event: graficar_funcion(funcion_entry, ax, canvas, fig))

    return ventana_graficar
