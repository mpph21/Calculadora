import tkinter as tk
from model.historial import obtener_historial, borrar_historial

def ver_historial_calculos(ventana):
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
