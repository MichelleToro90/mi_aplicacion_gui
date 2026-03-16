import tkinter as tk
from gui.aplicacion_gui import AplicacionGUI

if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionGUI(ventana)
    ventana.mainloop()