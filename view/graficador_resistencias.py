# graficador_resistencias.py
import tkinter as tk
from tkinter import ttk
from model.funciones_resistencias import calcular_resistencia
from PIL import Image, ImageTk

def crear_tab_resistencias(notebook):
    tab_resistencias = ttk.Frame(notebook)
    
    # Etiquetas para seleccionar bandas
    ttk.Label(tab_resistencias, text="Banda 1").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(tab_resistencias, text="Banda 2").grid(row=1, column=0, padx=5, pady=5)
    ttk.Label(tab_resistencias, text="Multiplicador").grid(row=2, column=0, padx=5, pady=5)
    ttk.Label(tab_resistencias, text="Tolerancia").grid(row=3, column=0, padx=5, pady=5)

    # Opciones de colores
    colores = ['Negro', 'Marrón', 'Rojo', 'Naranja', 'Amarillo', 'Verde', 'Azul', 'Violeta', 'Gris', 'Blanco', 'Oro', 'Plata']
    
    # Combobox para cada banda
    banda1_cb = ttk.Combobox(tab_resistencias, values=colores[:10])
    banda2_cb = ttk.Combobox(tab_resistencias, values=colores[:10])
    banda3_cb = ttk.Combobox(tab_resistencias, values=colores)
    tolerancia_cb = ttk.Combobox(tab_resistencias, values=colores[-4:])
    
    banda1_cb.grid(row=0, column=1, padx=5, pady=5)
    banda2_cb.grid(row=1, column=1, padx=5, pady=5)
    banda3_cb.grid(row=2, column=1, padx=5, pady=5)
    tolerancia_cb.grid(row=3, column=1, padx=5, pady=5)
    
    resultado_label = ttk.Label(tab_resistencias, text="Valor de la Resistencia:")
    resultado_label.grid(row=4, column=0, columnspan=2, padx=5, pady=10)
    
    def calcular():
        banda1 = banda1_cb.get()
        banda2 = banda2_cb.get()
        banda3 = banda3_cb.get()
        tolerancia = tolerancia_cb.get()
        
        if banda1 and banda2 and banda3 and tolerancia:
            valor, tol = calcular_resistencia(banda1, banda2, banda3, tolerancia)
            resultado_label.config(text=f"Resistencia: {valor} Ω ± {tol}%")
        else:
            resultado_label.config(text="Selecciona todas las bandas")
    
    calcular_btn = ttk.Button(tab_resistencias, text="Calcular", command=calcular)
    calcular_btn.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

    image = Image.open("Resis.jpeg")  # Cambia por el nombre de tu imagen
    image = image.resize((400, 200), Image.Resampling.LANCZOS)
  # Ajusta el tamaño según sea necesario
    img = ImageTk.PhotoImage(image)

    # Crear un label para mostrar la imagen
    image_label = ttk.Label(tab_resistencias, image=img)
    image_label.image = img  # Necesario para evitar que la imagen sea eliminada por el garbage collector
    image_label.grid(row=6, column=0, columnspan=2, padx=5, pady=10)


    return tab_resistencias
