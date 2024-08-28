# historial_graficas.py

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Lista para almacenar el historial localmente
historial_graficas = []

def inicializar_firebase():
    try:
        firebase_admin.get_app()
    except ValueError:
        try:
            cred = credentials.Certificate("C:\\Users\\tatia\\OneDrive\\Escritorio\\Calculadora\\model\\bd.json")
            firebase_admin.initialize_app(cred)
        except FileNotFoundError:
            print("Error: El archivo 'bd.json' no se encuentra")
            raise

def agregar_a_historial_graficas(calculo, resultado):
    inicializar_firebase()
    db = firestore.client()
    doc_ref = db.collection('historalgraficas').document()  # Nombre de la colección
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    doc_ref.set({
        'fecha': fecha,
        'calculo': calculo,
        'resultado': resultado
    })
    historial_graficas.append((fecha, calculo, resultado))  # Guarda localmente


def obtener_historial_graficas():
    inicializar_firebase()
    db = firestore.client()
    historial_ref = db.collection('historalgraficas')  # Nombre de la colección
    docs = historial_ref.stream()
    
    global historial_graficas
    historial_graficas = []
    for doc in docs:
        data = doc.to_dict()
        fecha = data.get('fecha', 'Fecha no disponible')
        calculo = data.get('calculo', 'Cálculo no disponible')
        resultado = data.get('resultado', 'Resultado no disponible')
        historial_graficas.append((fecha, calculo, resultado))
    
    return historial_graficas

def borrar_historial_graficas(historial_texto=None, confirmar=True):
    if confirmar:
        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas borrar todo el historial?")
        if not respuesta:
            return

    inicializar_firebase()
    db = firestore.client()
    historial_ref = db.collection('historalgraficas')  # Nombre de la colección
    docs = historial_ref.stream()
    for doc in docs:
        doc.reference.delete()
    if historial_texto:
        historial_texto.delete(1.0, tk.END)  # Borra el historial en la interfaz si es proporcionado
    historial_graficas.clear()

def cargar_historial(historial_texto):
    historial = obtener_historial_graficas()
    historial_texto.delete(1.0, tk.END)  # Limpiar el widget de texto
    for fecha, calculo, resultado in historial:
        line = f"Fecha: {fecha}\nCálculo: {calculo}\nResultado: Gráfica de {resultado}\n\n"
        historial_texto.insert(tk.END, line)
