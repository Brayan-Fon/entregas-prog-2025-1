import unittest
from unittest.mock import patch
import tkinter as tk
from Saludo_GUI import VentanaSaludo  # Asegúrate de que el nombre coincida con el nuevo de la clase

class TestVentanaSaludo(unittest.TestCase):
    def setUp(self):
        self.ventana = tk.Tk()
        self.ventana.withdraw()
        self.app = VentanaSaludo(self.ventana)

    def tearDown(self):
        self.ventana.destroy()

    @patch('tkinter.messagebox.showinfo')
    def test_saludo_con_nombre(self, mock_info):
        self.app.campo_nombre.insert(0, "Carlos")
        self.app.mostrar_saludo()
        mock_info.assert_called_once_with("Saludo", "Hola Carlos")

    @patch('tkinter.messagebox.showwarning')
    def test_saludo_sin_nombre(self, mock_warning):
        self.app.campo_nombre.delete(0, tk.END)
        self.app.mostrar_saludo()
        mock_warning.assert_called_once_with("Advertencia", "Por favor, ingrese un nombre.")

if __name__ == '__main__':
    unittest.main()
