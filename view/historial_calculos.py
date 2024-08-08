import tkinter as tk
from model.historial import obtener_historial, borrar_historial
from model.client_experience import confirmar_borrar_historial

def ver_historial_calculos(ventana): #parametro ventana principal desde la cual se abrirá la nueva
    historial_window = tk.Toplevel(ventana) #crea una ventana secundaria superior
    historial_window.title("Historial de Cálculos")
    historial_window.geometry("300x200")
    historial_window.configure(bg='gray12')

    historial_label = tk.Label(historial_window, text="", justify=tk.LEFT, bg="gray12", font=("Times New Roman", 12), fg="white")
    historial_label.pack(expand=True, fill=tk.BOTH) #La etiqueta se expande para llenar el espacio disponible en la ventana y se ajusta

    def actualizar_historial_label():
        # Obtiene el historial de cálculos
        historial = obtener_historial()
        
        # Lista para almacenar cada línea del historial formateado
        lineasDeHistorial = []

        # Itera sobre el historial con sus índices
        for i, resultado in enumerate(historial):
            # Formatea la cadena para cada resultado
            linea_form = f"{i+1}. {resultado}"
            # Añade la cadena formateada a la lista
            lineasDeHistorial.append(linea_form)
        
        # Une todas las líneas con saltos de línea
        historial_text = "\n".join(lineasDeHistorial)
        
        # Actualiza la etiqueta con el texto del historial
        historial_label.config(text=historial_text)

    def borrar_historial_y_actualizar():
        borrar_historial()
        actualizar_historial_label()

    def confirmar_borrado():
        if confirmar_borrar_historial(historial_window):
            borrar_historial_y_actualizar()

    # Actualiza el historial al abrir la ventana
    actualizar_historial_label()

    btn_borrar_historial = tk.Button(historial_window, text="Borrar Historial", command=confirmar_borrado, bg="violet red", fg="gray1", bd=0, font=("Times New Roman", 16))
    btn_borrar_historial.pack()

    return historial_window
