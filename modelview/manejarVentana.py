from model.client_experience import confirmar_cierre_ventana
import tkinter as tk

class WindowManager:
    def __init__(self):
        self.windows = {}

    def open_window(self, window_name, window_func, *args, **kwargs):
        if window_name in self.windows and self.windows[window_name].winfo_exists():
            self.windows[window_name].lift()
        else:
            self.windows[window_name] = window_func(*args, **kwargs)
            # Vincular el evento de cierre con la confirmación
            self.windows[window_name].protocol("WM_DELETE_WINDOW", lambda: self.close_window(window_name))

        return self.windows[window_name]

    def close_window(self, window_name):
        if window_name in self.windows and self.windows[window_name].winfo_exists():
            if confirmar_cierre_ventana(self.windows[window_name]):
                self.windows[window_name].destroy()
                del self.windows[window_name]

# Crear una instancia de WindowManager
window_manager = WindowManager()
