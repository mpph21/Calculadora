import tkinter as tk
from model.funciones import *
from model.historial import agregar_al_historial 
from modelview.calculadora_modelview import CalculadoraModelView

def agregar_funciones_avanzadas(ventana, pantalla, calculadora):
    def operacion_avanzada(func): #func es una funcion de operacion avanzada en el model
        try:
            valor = float(pantalla.get()) #obtiene el valor en la pantalla actual
            resultado = func(valor) #llama a la funcion func y la opera con el valor de la pantalla obtenido
            pantalla.delete(0, tk.END) #borra el texto que haya en la pantalla
            pantalla.insert(tk.END, resultado) # inserta en la pantalla el resultado del calculo hecho
            agregar_al_historial(resultado) #llama a la funcion historial para guardarlo
        except Exception as e:
            pantalla.insert(tk.END, "Error, asegurate de que sea un número")

    botones_avanzados = [ #cada boton está asociado con una funcion matematica avanzada del model
        ("√x", 1, 4, lambda: operacion_avanzada(raiz_cuadrada)), #lambda son funciones anónimas
        ("sin", 2, 4, lambda: operacion_avanzada(seno)), #al oprimir el boton se llama a operacion avanzada con el argumento seno
        ("cos", 3, 4, lambda: operacion_avanzada(coseno)),
        ("tan", 4, 4, lambda: operacion_avanzada(tangente))
    ]

    for (text, row, column, command) in botones_avanzados:
        btn = tk.Button(ventana, text=text, command=command, bg="#E0E0E0", activebackground="#BDBDBD", width=4, bd=0, font=('Arial', 16))
        btn.grid(row=row, column=column, sticky="nsew")

