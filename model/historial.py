import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

historial = [] # Inicializa una lista vacía para almacenar el historial de cálculos localmente

def inicializar_firebase(): #funcion para iniciaizar Firebase
    try:
        firebase_admin.get_app() #verifica si está iniciada
    except ValueError: #si no, busca en el archivo local e intenta iniciarla conlas credenciales
        try:
            cred = credentials.Certificate("C:\\Users\\tatia\\OneDrive\\Escritorio\\Calculadora\\model\\bd.json")
            firebase_admin.initialize_app(cred)
        except FileNotFoundError: #si no puede lanza un error
            print("Error: El archivo 'bd.json' no se encuentra")
            raise #devuelve la excepcion luego del comentario de error

def agregar_al_historial(resultado): #funcion para agregar un resultado al historial
    inicializar_firebase() #llama a la funcion de inicio de la firebase
    db = firestore.client() #obtiene el cliente
    doc_ref = db.collection('historial').document() #en la coleccion de historial crea un documento
    doc_ref.set({'resultado': resultado})#añade el resultado al documento
    historial.append(resultado) #se guarda localmente el resultado en la lista histotial

def obtener_historial():
    return historial

def borrar_historial():
    inicializar_firebase()
    db = firestore.client()
    historial_ref = db.collection('historial') # variable igual a la coleccion del historial en firebase
    docs = historial_ref.stream() #variable que va a ser igual a la iteracion de cada referencia en el historial 
    for doc in docs:
        doc.reference.delete() # al iterar va borrando cada referencia que encuentre
    historial.clear() #borra localmente los resultados almacenados en la lista creada