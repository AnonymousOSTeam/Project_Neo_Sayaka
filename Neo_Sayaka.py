import customtkinter as ctk

# Configuração inicial do ambiente visual
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class NeoSayakaUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Neo-Sayaka // System Core")
        self.geometry("700x500")

        # Layout principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Caixa de Texto / Terminal de Logs
        self.terminal_box = ctk.CTkTextbox(self, width=650, height=350, corner_radius=6)
        self.terminal_box.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.terminal_box.insert("0.0", "[SYSTEM] Neo-Sayaka inicializada na matriz.\n[STATUS] Pronta para suportar a pressão e tankar o sistema.\n")
        self.terminal_box.configure(state="disabled")

        # Campo de Entrada de Comando
        self.entry_field = ctk.CTkEntry(self, placeholder_text="Digite um comando para a Neo-Sayaka...", width=500)
        self.entry_field.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="w")
        self.entry_field.bind("<Return>", self.process_input)

        # Botão de Execução
        self.send_button = ctk.CTkButton(self, text="Executar", command=self.process_input)
        self.send_button.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="e")

    def process_input(self, event=None):
        user_input = self.entry_field.get()
        if user_input.strip():
            self.terminal_box.configure(state="normal")
            self.terminal_box.insert("end", f"\n[OPERADOR]: {user_input}\n")
            
            # Resposta customizada baseada na voltagem do operador
            if "erm" in user_input.lower() or "..." in user_input or "o-o-o" in user_input.lower():
                response = "[NEO-SAYAKA]: Detectei instabilidade e gotejamento de sobrecarga no buffer. Respira. Eu seguro a voltagem por aqui."
            else:
                response = f"[NEO-SAYAKA]: Comando recebido sob alta voltagem. Processando parâmetros..."
                
            self.terminal_box.insert("end", f"{response}\n")
            self.terminal_box.configure(state="disabled")
            self.terminal_box.see("end")
            self.entry_field.delete(0, "end")

if __name__ == "__main__":
    app = NeoSayakaUI()
    app.mainloop()
