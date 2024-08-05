from model.funciones import (suma, resta, multiplicacion, division, potencia, raiz_cuadrada, seno, coseno, tangente)
from model.historial import agregar_al_historial, obtener_historial, borrar_historial

class CalculadoraModelView: #esta clase gestiona la logica de las operaciones y la interaccion con el historial
    def __init__(self): #inicia la instancia de la clase, con dos atributos
        self.valor_a = 0 #almacena el primer valor de la operacion
        self.operacion = "" #almacena el simbolo de la operación

    def operar(self, simbolo, valor_a): #método operar
        self.valor_a = valor_a #atributo de la instancia self
        self.operacion = simbolo #atributo de la instancia self

    def resultado(self, valor_b): #obtiene el simbolo guardado y lo opera según cual sea
        if self.operacion == '+':
            resultado = suma(self.valor_a, valor_b) #llama a las funciones del model
        elif self.operacion == '-':
            resultado = resta(self.valor_a, valor_b)
        elif self.operacion == '*':
            resultado = multiplicacion(self.valor_a, valor_b)
        elif self.operacion == '^':
            resultado = potencia(self.valor_a, valor_b)
        elif self.operacion == '/':
            resultado = division(self.valor_a, valor_b)
        else:
            resultado = "Error"
        agregar_al_historial(resultado) #llama a la funcion para guardar el resultado
        return resultado



class WindowManager:
    def __init__(self):
        self.windows = {}

    def open_window(self, window_name, window_func, *args, **kwargs):
        # Verifica si la ventana ya existe y está abierta
        if window_name in self.windows and self.windows[window_name].winfo_exists():
            self.windows[window_name].lift()  # Trae la ventana al frente
        else:
            # Crea una nueva ventana
            self.windows[window_name] = window_func(*args, **kwargs)

        return self.windows[window_name]
    
# Crear una instancia de WindowManager
window_manager = WindowManager()
