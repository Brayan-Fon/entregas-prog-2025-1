""" 
Título de práctica: saludo en GUI

Descripción:
Aplicación gráfica desarrollada con Tkinter que permite ingresar un nombre y recibir un saludo personalizado. La interfaz cuenta con campos de entrada, 
botones interactivos y uso de ventanas emergentes (messagebox). Se aplicaron principios de diseño amigable y pruebas unitarias para validar la funcionalidad.

Autor: Brayan Steven Fontecha Lozano <brayanstevenfontechalozano@gmail.com>
Fecha: 2025/05/26
 """

import tkinter as tk
from tkinter import messagebox

class VentanaSaludo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Aplicación de Saludo")
        self.ventana.geometry("300x200")
        self.ventana.configure(bg="#5A827E")

        self.etiqueta_nombre = tk.Label(ventana, text="Ingrese su nombre:", bg="#5A827E", font=("Arial", 12))
        self.etiqueta_nombre.pack(pady=10)

        self.campo_nombre = tk.Entry(ventana, width=30)
        self.campo_nombre.pack(pady=5)

        self.btn_saludo = tk.Button(ventana, text="Saludar", command=self.mostrar_saludo, bg="#84AE92", fg="white", font=("Arial", 10, "bold"))
        self.btn_saludo.pack(pady=10)

        self.btn_salir = tk.Button(ventana, text="Salir", command=self.ventana.quit, bg="black", fg="white", font=("Arial", 10, "bold"))
        self.btn_salir.pack(pady=5)

    def mostrar_saludo(self):
        nombre_usuario = self.campo_nombre.get().strip()
        if nombre_usuario:
            mensaje = f"Hola {nombre_usuario}"
            messagebox.showinfo("Saludo", mensaje)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un nombre.")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = VentanaSaludo(ventana)
    ventana.mainloop()
