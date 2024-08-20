import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime

historial = []  # Inicializa una lista vacía para almacenar el historial de cálculos localmente

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

def agregar_al_historial(calculo, resultado):
    inicializar_firebase()
    db = firestore.client()
    doc_ref = db.collection('historial').document()
    
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    doc_ref.set({
        'fecha': fecha,
        'calculo': calculo,
        'resultado': resultado
    })
    
    historial.append((fecha, calculo, resultado))  # Guarda localmente el historial con fecha, cálculo y resultado

def obtener_historial():
    return historial

def borrar_historial():
    inicializar_firebase()
    db = firestore.client()
    historial_ref = db.collection('historial')
    docs = historial_ref.stream()
    for doc in docs:
        doc.reference.delete()
    historial.clear()
