import tkinter as tk
from model.funciones import *
from view.historial_calculos import *
from modelview.graficador import abrir_ventana_graficar
from modelview.calculadora_modelview import CalculadoraModelView, window_manager
from modelview.calculadora_modelview import window_manager


def crear_botones(ventana, pantalla, calculadora):
    boton_config = {
        "bg": "#E0E0E0",
        "activebackground": "#BDBDBD",
        "bd": 0,
        "font": ('Arial', 16)
    }

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

    botones = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        (".", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ("^", 1, 5), ("Historial", 6, 0, 6), ("Graficar", 6, 5)
    ]
    for (text, row, column, *span) in botones:
            if text == "=":
                btn = tk.Button(ventana, text=text, command=result, **boton_config)
            elif text in {"+", "-", "*", "/", "^"}:
                btn = tk.Button(ventana, text=text, command=lambda t=text: operacion(t), **boton_config)
            elif text == "Historial":
                btn = tk.Button(ventana, text=text, command=lambda: window_manager.open_window('historial', ver_historial_calculos, ventana), **boton_config)
                btn.grid(row=row, column=column, columnspan=span[0], sticky="nsew")
                continue
            elif text == "Graficar":
                btn = tk.Button(ventana, text=text, command=lambda: window_manager.open_window('graficar', abrir_ventana_graficar, ventana), **boton_config)
            else:
                btn = tk.Button(ventana, text=text, command=lambda t=text: mostrar_en_pantalla(t), **boton_config)
            btn.grid(row=row, column=column, sticky="nsew")

    borrar = tk.Button(ventana, text="Borrar", command=lambda: pantalla.delete(0, tk.END), bg="#FF5733", fg="#FFFFFF", bd=0)
    borrar.grid(row=5, column=0, columnspan=4, sticky="nsew")
    