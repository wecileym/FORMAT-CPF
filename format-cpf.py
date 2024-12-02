
from tkinter import messagebox
import re
import tkinter as tk
import customtkinter as ctk

class Logon(ctk.CTk): 

    def __init__(self):
        super().__init__()
        
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        self.geometry("800x600")
        self.minsize(800, 600)
        self.title('Login')
        
        self.cpf = ctk.CTkEntry(self, width=480, height=50, font=('Century Gothic', 20,'bold'))
        self.cpf.pack(pady=5, padx=10)
        self.cpf.bind("<FocusOut>", lambda event: self.format_cpf(event, self.cpf))

        self.anything = ctk.CTkEntry(self, width=480, height=50, font=('Century Gothic', 20,'bold'))
        self.anything.pack(pady=5, padx=10)

    def format_cpf(self, event, entry):
        
        text = entry.get().replace('.', '').replace('-', '')  # Remover pontos e hífen para simplificar a verificação

        if not text.isdigit():
            messagebox.showerror("Erro de entrada", "Por favor, insira apenas números.")
            entry.delete(0, tk.END)
            return

        if len(text) > 11:  # Limitar a entrada a 11 caracteres para o CPF
            text = text[:11]

        # Formatando o CPF no formato XXX.XXX.XXX-XX
        formatted_text = ""
        if len(text) >= 1:
            formatted_text = text[:3]
        if len(text) >= 4:
            formatted_text += '.' + text[3:6]
        if len(text) >= 7:
            formatted_text += '.' + text[6:9]
        if len(text) >= 10:
            formatted_text += '-' + text[9:11]

        entry.delete(0, tk.END)
        entry.insert(0, formatted_text)

if __name__ == "__main__":
    logon = Logon()
    logon.mainloop()
    
   
