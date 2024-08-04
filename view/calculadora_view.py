import tkinter as tk
from model.funciones import *
from modelview.calculadora_modelview import CalculadoraModelView
from model.historial import agregar_al_historial, obtener_historial, borrar_historial

def create_calculator_ui():
    ventana = tk.Tk()
    ventana.configure(bg='white')
    pantalla = tk.Entry(ventana, width=30, bd=7, justify="right")
    pantalla.grid(row=0, column=0, columnspan=10)
    pantalla.insert(tk.END, '0')

    calculadora = CalculadoraModelView()

    def mostrar_en_pantalla(valor):
        current_text = pantalla.get()
        if current_text == '0':
            pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, valor)

    def operacion(simbolo):
        calculadora.operacion = simbolo
        calculadora.valor_a = float(pantalla.get())
        pantalla.delete(0, tk.END)

    def result():
        valor_b = float(pantalla.get())
        resultado = calculadora.resultado(valor_b)
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, resultado)

    def tecla_presionada(event):
        key = event.keysym

        if key in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            mostrar_en_pantalla(key)
        elif key == 'period':
            if '.' not in pantalla.get():
                mostrar_en_pantalla('.')
        elif key == 'equal':
            result()
        elif key == 'plus':
            operacion('+')
        elif key == 'minus':
            operacion('-')
        elif key == 'asterisk':
            operacion('*')
        elif key == 'slash':
            operacion('/')
        elif key == 'Return':
            result()
        elif key == 'c':
            pantalla.delete(0, tk.END)
        elif key == 'h':
            ver_historial()
        elif key == 'BackSpace':
            current_text = pantalla.get()
            pantalla.delete(len(current_text)-1, tk.END)
        elif key == 'Delete':
            pantalla.delete(0, tk.END)

    ventana.bind('<Key>', tecla_presionada)

    def ver_historial():
        historial_window = tk.Toplevel(ventana)
        historial_window.title("Historial de Cálculos")
        historial_window.geometry("300x200")

        historial = obtener_historial()
        historial_text = "\n".join([f"{i+1}. {resultado}" for i, resultado in enumerate(historial)])
        historial_label = tk.Label(historial_window, text=historial_text)
        historial_label.pack()

        btn_borrar_historial = tk.Button(historial_window, text="Borrar Historial", command=lambda: (borrar_historial(), actualizar_historial_label(historial_window, historial_label)))
        btn_borrar_historial.pack()

    def actualizar_historial_label(historial_window, historial_label):
        historial = obtener_historial()
        historial_text = "\n".join([f"{i+1}. {resultado}" for i, resultado in enumerate(historial)])
        historial_label.config(text=historial_text)

    boton_config = {
        "bg": "#E0E0E0",
        "activebackground": "#BDBDBD",
        "width": 4,
        "bd": 0,
        "font": ('Arial', 12)
    }

    botones = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        (".", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ("^", 1, 5), ("Historial", 6, 0), ("Graficar", 6, 5)
    ]

    for (text, row, column) in botones:
        if text == "=":
            btn = tk.Button(ventana, text=text, command=result, **boton_config)
        elif text in {"+", "-", "*", "/", "^"}:
            btn = tk.Button(ventana, text=text, command=lambda t=text: operacion(t), **boton_config)
        elif text == "Historial":
            btn = tk.Button(ventana, text=text, command=ver_historial, **boton_config)
        else:
            btn = tk.Button(ventana, text=text, command=lambda t=text: mostrar_en_pantalla(t), **boton_config)
        btn.grid(row=row, column=column)

    borrar = tk.Button(ventana, text="Borrar", width=26, command=lambda: pantalla.delete(0, tk.END), bg="#FF5733", fg="#FFFFFF", bd=0)
    borrar.grid(row=5, column=0, columnspan=4)

    def operacion_avanzada(func):
        try:
            valor = float(pantalla.get())
            resultado = func(valor)
            pantalla.delete(0, tk.END)
            pantalla.insert(tk.END, resultado)
            agregar_al_historial(resultado)
        except Exception as e:
            pantalla.insert(tk.END, "Error")

    botones_avanzados = [
        ("√x", 2, 5, lambda: operacion_avanzada(raiz_cuadrada)),
        ("sin", 3, 5, lambda: operacion_avanzada(seno)),
        ("cos", 4, 5, lambda: operacion_avanzada(coseno)),
        ("tan", 5, 5, lambda: operacion_avanzada(tangente))
    ]

    for (text, row, column, command) in botones_avanzados:
        btn = tk.Button(ventana, text=text, command=command, **boton_config)
        btn.grid(row=row, column=column)

    ventana.mainloop()
