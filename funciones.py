import tkinter as tk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

def RealtimeSet(resultado):

    cred = credentials.Certificate("bd.json")
    firebase_admin.initialize_app(cred)
    
    # Get a reference to the Firestore database
    db = firestore.client()

    # Example: Write data to the Firestore database
    doc_ref = db.collection('historial').document()
    doc_ref.set({
        'resultado': resultado
    })
    # # Initialize Firebase Admin SDK with service account credentials
    # cred = credentials.Certificate("bd.json")
    # firebase_admin.initialize_app(cred, {
    #     'databaseURL': 'https://calkulator-612c1-default-rtdb.firebaseio.com/'
    # })
    
    # # Get a reference to the Firebase Realtime Database
    # ref = db.reference('/')

    # # Example: Write data to the Realtime Database
    # ref.set({{
    #     'historial': "resultado"
    #     }
    # })
    

def create_calculator_ui():
    ventana = tk.Tk()
    ventana.configure(bg='white')  # Color de fondo blanco
    pantalla = tk.Entry(ventana, width=24, bd=7, justify="right")
    pantalla.grid(row=0, column=0, columnspan=4)
    pantalla.insert(tk.END, 0)
    
    # Variables
    valor_a = 0
    valor_b = 0
    operacion = ""
    resultado = 0

    # Funciones de operación
    def operar(simbolo):
        nonlocal valor_a, operacion
        valor_a = float(pantalla.get())
        pantalla.delete(0, tk.END)
        operacion = simbolo  # Almacenar el operador seleccionado

    def result():
        nonlocal resultado, valor_b
        valor_b = float(pantalla.get())
        pantalla.delete(0, tk.END)
        try:
            if operacion == '+':
                resultado = valor_a + valor_b
            elif operacion == '-':
                resultado = valor_a - valor_b
            elif operacion == '*':
                resultado = valor_a * valor_b
            elif operacion == '/':
                if valor_b != 0:
                    resultado = valor_a / valor_b
                else:
                    resultado = "Error: División por cero"
            pantalla.insert(tk.END, resultado)
            RealtimeSet(resultado)
        except Exception as e:
            pantalla.insert(tk.END, "Error")

    def mostrar_en_pantalla(valor):
        pantalla.insert(tk.END, valor)

    # Interfaz gráfica

    # Botones
    boton_config = {
        "bg": "#E0E0E0",  # Color de fondo gris claro
        "activebackground": "#BDBDBD",  # Color de fondo gris más oscuro al hacer clic
        "width": 4,
        "bd": 0,  # Grosor del borde
        "font": ('Arial', 12)  # Fuente y tamaño del texto
    }

    botones = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        (".", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ]

    for (text, row, column) in botones:
        if text == "=":
            btn = tk.Button(ventana, text=text, command=result, **boton_config)
        elif text in {"+", "-", "*", "/"}:
            btn = tk.Button(ventana, text=text, command=lambda t=text: operar(t), **boton_config)
        else:
            btn = tk.Button(ventana, text=text, command=lambda t=text: mostrar_en_pantalla(t), **boton_config)
        btn.grid(row=row, column=column)

    borrar = tk.Button(ventana, text="Borrar", width=26, command=lambda: pantalla.delete(0, tk.END), bg="#FF5733", fg="#FFFFFF", bd=0)
    borrar.grid(row=5, column=0, columnspan=4)

    ventana.mainloop()

create_calculator_ui()
