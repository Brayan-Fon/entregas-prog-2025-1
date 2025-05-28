
import tkinter as tk
from tkinter import messagebox

class AppSaludoPersonalizado:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Bienvenido")
        self.ventana_principal.geometry("400x250")
        self.ventana_principal.configure(bg="#EFEFEF")

        # Frame superior para la entrada
        self.marco_entrada = tk.Frame(self.ventana_principal, bg="#EFEFEF")
        self.marco_entrada.pack(pady=20)

        self.lbl_nombre = tk.Label(self.marco_entrada, text="Nombre:", bg="#EFEFEF", font=("Verdana", 10))
        self.lbl_nombre.grid(row=0, column=0, padx=5, pady=5)

        self.entrada_nombre = tk.Entry(self.marco_entrada, width=30, font=("Verdana", 10))
        self.entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

        # Frame inferior para botones
        self.marco_botones = tk.Frame(self.ventana_principal, bg="#EFEFEF")
        self.marco_botones.pack(pady=10)

        self.boton_enviar = tk.Button(self.marco_botones, text="Enviar Saludo", command=self.enviar_saludo,
                                      bg="#4CAF50", fg="white", font=("Verdana", 9, "bold"), width=15)
        self.boton_enviar.grid(row=0, column=0, padx=10)

        self.boton_cerrar = tk.Button(self.marco_botones, text="Cerrar Ventana", command=self.ventana_principal.destroy,
                                      bg="#f44336", fg="white", font=("Verdana", 9, "bold"), width=15)
        self.boton_cerrar.grid(row=0, column=1, padx=10)

    def enviar_saludo(self):
        nombre_usuario = self.entrada_nombre.get().strip()
        if nombre_usuario:
            mensaje = f"¡Hola, {nombre_usuario}! Bienvenido/a."
            messagebox.showinfo("Saludo", mensaje)
        else:
            messagebox.showwarning("Campo vacío", "Por favor, introduce tu nombre.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppSaludoPersonalizado(root)
    root.mainloop()
