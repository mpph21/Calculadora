"""
Archivo principal para iniciar la interfaz de usuario de la calculadora.
"""

from view.ventana_principal import create_calculator_ui

if __name__ == "__main__":
    try:
        create_calculator_ui()
    except Exception as e:
        print(f"Error al iniciar la calculadora: {e}")
