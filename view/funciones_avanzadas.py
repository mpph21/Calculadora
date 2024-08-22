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
            # Verifica que el cálculo y el resultado sean correctos
            calculo_str = f"{func.__name__}({valor})"
            print(f"Guardando en historial: {calculo_str} = {resultado}")
            agregar_al_historial(calculo_str, resultado)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {str(e)}")

    botones_avanzados = [
        ("√x", 1, 4, lambda: operacion_avanzada(raiz_cuadrada)),
        ("sin", 2, 4, lambda: operacion_avanzada(seno)),
        ("cos", 3, 4, lambda: operacion_avanzada(coseno)),
        ("tan", 4, 4, lambda: operacion_avanzada(tangente))
    ]

    for (text, row, column, command) in botones_avanzados:
        btn = tk.Button(ventana, text=text, command=command, bg="#E0E0E0", activebackground="#BDBDBD", width=4, bd=0, font=('Arial', 16))
        btn.grid(row=row, column=column, sticky="nsew")
