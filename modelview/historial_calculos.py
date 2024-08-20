import tkinter as tk
from model.historial import obtener_historial, borrar_historial
from model.client_experience import confirmar_borrar_historial

def ver_historial_calculos(ventana):
    historial_window = tk.Toplevel(ventana)
    historial_window.title("Historial de Cálculos")
    historial_window.geometry("400x300")
    historial_window.configure(bg='gray12')

    historial_label = tk.Label(historial_window, text="", justify=tk.LEFT, bg="gray12", font=("Times New Roman", 12), fg="white")
    historial_label.pack(expand=True, fill=tk.BOTH)

    def actualizar_historial_label():
        historial = obtener_historial()

        lineasDeHistorial = []

        for i, (fecha, calculo, resultado) in enumerate(historial):
            linea_form = f"{i+1}. Fecha: {fecha}\nCálculo: {calculo}\nResultado: {resultado}\n"
            lineasDeHistorial.append(linea_form)
        
        historial_text = "\n".join(lineasDeHistorial)
        
        historial_label.config(text=historial_text)

    def borrar_historial_y_actualizar():
        borrar_historial()
        actualizar_historial_label()

    def confirmar_borrado():
        if confirmar_borrar_historial(historial_window):
            borrar_historial_y_actualizar()

    actualizar_historial_label()

    btn_borrar_historial = tk.Button(historial_window, text="Borrar Historial", command=confirmar_borrado, bg="violet red", fg="gray1", bd=0, font=("Times New Roman", 16))
    btn_borrar_historial.pack(pady=10)

    return historial_window
