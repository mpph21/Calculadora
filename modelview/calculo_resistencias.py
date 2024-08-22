# calculo_resistencias.py

from tkinter import messagebox

def calcular_resistencia_serie(resistencias):
    try:
        return sum(float(r) for r in resistencias if r)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos de resistencia.")
        return None

def calcular_resistencia_paralelo(resistencias):
    try:
        inverso_total = sum(1 / float(r) for r in resistencias if r)
        return 1 / inverso_total if inverso_total != 0 else 0
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos de resistencia.")
        return None
