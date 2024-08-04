import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

historial = []

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

def agregar_al_historial(resultado):
    inicializar_firebase()
    db = firestore.client()
    doc_ref = db.collection('historial').document()
    doc_ref.set({'resultado': resultado})
    historial.append(resultado)

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