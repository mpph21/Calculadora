import tkinter as tk
from model.funciones import *
from model.historial import agregar_al_historial 
from modelview.calculadora_modelview import CalculadoraModelView

def agregar_funciones_avanzadas(ventana, pantalla, calculadora):
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
        ("√x", 1, 5, lambda: operacion_avanzada(raiz_cuadrada)),
        ("sin", 2, 5, lambda: operacion_avanzada(seno)),
        ("cos", 3, 5, lambda: operacion_avanzada(coseno)),
        ("tan", 4, 5, lambda: operacion_avanzada(tangente))
    ]

    for (text, row, column, command) in botones_avanzados:
        btn = tk.Button(ventana, text=text, command=command, bg="#E0E0E0", activebackground="#BDBDBD", width=4, bd=0, font=('Arial', 12))
        btn.grid(row=row, column=column, sticky="nsew")

