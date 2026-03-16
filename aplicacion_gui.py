import tkinter as tk
from tkinter import messagebox
from utils.gestor_datos import GestorDatos

class AplicacionGUI:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registro de Personas")
        self.ventana.geometry("400x350")

        self.gestor = GestorDatos()

        # Label y campo Nombre
        self.label_nombre = tk.Label(ventana, text="Nombre:")
        self.label_nombre.pack()

        self.entrada_nombre = tk.Entry(ventana, width=30)
        self.entrada_nombre.pack(pady=5)

        # Label y campo Cédula
        self.label_cedula = tk.Label(ventana, text="Cédula:")
        self.label_cedula.pack()

        self.entrada_cedula = tk.Entry(ventana, width=30)
        self.entrada_cedula.pack(pady=5)

        # Botón Agregar
        self.boton_agregar = tk.Button(
            ventana,
            text="Agregar",
            command=self.agregar_dato
        )
        self.boton_agregar.pack(pady=10)

        # Lista para mostrar datos
        self.lista = tk.Listbox(ventana, width=45, height=10)
        self.lista.pack()

        # Botón Limpiar
        self.boton_limpiar = tk.Button(
            ventana,
            text="Limpiar",
            command=self.limpiar_datos
        )
        self.boton_limpiar.pack(pady=10)

    def agregar_dato(self):
        nombre = self.entrada_nombre.get()
        cedula = self.entrada_cedula.get()

        if nombre and cedula:
            self.gestor.agregar(nombre, cedula)

            texto = f"Nombre: {nombre} | Cédula: {cedula}"
            self.lista.insert(tk.END, texto)

            self.entrada_nombre.delete(0, tk.END)
            self.entrada_cedula.delete(0, tk.END)

        else:
            messagebox.showwarning("Advertencia", "Ingrese nombre y cédula")

    def limpiar_datos(self):
        self.lista.delete(0, tk.END)
        self.gestor.limpiar()