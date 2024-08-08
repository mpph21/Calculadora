import tkinter as tk
from view.botones import crear_botones
from view.historial_calculos import ver_historial_calculos
from view.funciones_avanzadas import agregar_funciones_avanzadas
from modelview.calculadora_modelview import CalculadoraModelView

def create_calculator_ui():
    ventana = tk.Tk()
    ventana.configure(bg='black')
    ventana.title("Kalkulator")

    try:
        logo = tk.PhotoImage(file="kalkulatorRosa.png")  # Asegúrate de proporcionar la ruta correcta
        ventana.iconphoto(True, logo)
    except tk.TclError:
        print("No se pudo cargar el logo. Asegúrate de que la ruta del archivo es correcta y que el archivo está en un formato compatible.")


    # Configurar la expansión de las filas y columnas
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)
    for i in range(5):
        ventana.grid_columnconfigure(i, weight=1)
    
    # Ajustar el tamaño mínimo de las filas y columnas
    ventana.grid_rowconfigure(0, minsize=80)  # Fila de la pantalla
    ventana.grid_rowconfigure(1, minsize=60)
    ventana.grid_rowconfigure(2, minsize=60)
    ventana.grid_rowconfigure(3, minsize=60) #configura el tamaño minimo que peden tener los botones
    ventana.grid_rowconfigure(4, minsize=60)
    ventana.grid_rowconfigure(5, minsize=60)  # Fila para el botón de borrar
    ventana.grid_rowconfigure(6, minsize=60)

    ventana.grid_columnconfigure(0, minsize=60)  # Columna para el primer botón
    ventana.grid_columnconfigure(1, minsize=60)  # Columna para el segundo botón
    ventana.grid_columnconfigure(2, minsize=60)  # Columna para el tercer botón
    ventana.grid_columnconfigure(3, minsize=60)  # Columna para el cuarto botón

    
    pantalla = tk.Entry(ventana, bg="white",justify="right", font = ('Arial', 16), highlightbackground="violet red", highlightcolor="violet red", highlightthickness=8)
    pantalla.grid(row=0, column=0, columnspan=5, sticky="nsew")
    pantalla.insert(tk.END, '0') #inicia la pantalla con un cero

    calculadora = CalculadoraModelView()

    def mostrar_en_pantalla(valor):
        textoActual = pantalla.get() #obtiene el texto actual en la pantalla
        if textoActual == '0': #si es 0 lo borra y añade el valor
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
            ver_historial_calculos(ventana)
        elif key == 'BackSpace':
            current_text = pantalla.get()
            pantalla.delete(len(current_text)-1, tk.END)
        elif key == 'Delete':
            pantalla.delete(0, tk.END)

    ventana.bind('<Key>', tecla_presionada)

    # Crear botones numéricos y de operaciones
    crear_botones(ventana, pantalla, calculadora)
    
    # Crear botones avanzados
    agregar_funciones_avanzadas(ventana, pantalla, calculadora)

    ventana.mainloop()

