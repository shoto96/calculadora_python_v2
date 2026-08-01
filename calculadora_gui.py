import tkinter as tk
import math

class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Python")
        self.root.geometry("380x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#202020")

        self.expressao = ""

        self.visor = tk.Entry(
            root, 
            font=("Arial", 24, "bold"), 
            bg="#171717", 
            fg="#FFFFFF", 
            bd=0, 
            justify="right"
        )
        self.visor.pack(fill="both", ipadx=8, ipady=18, padx=10, pady=15)

        botoes = [
            ("C", 1, 0, "#D9534F"), ("√", 1, 1, "#333333"), ("^", 1, 2, "#333333"), ("/", 1, 3, "#FF9500"),
            ("sin", 2, 0, "#333333"), ("cos", 2, 1, "#333333"), ("tan", 2, 2, "#333333"), ("*", 2, 3, "#FF9500"),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("-", 3, 3, "#FF9500"),
            ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("+", 4, 3, "#FF9500"),
            ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("=", 5, 3, "#28A745"),
            ("%", 6, 0, "#333333"), ("0", 6, 1), (".", 6, 2)
        ]

        frame_botoes = tk.Frame(root, bg="#202020")
        frame_botoes.pack(fill="both", expand=True, padx=10, pady=(0, 15))

        for i in range(4):
            frame_botoes.grid_columnconfigure(i, weight=1)

        for item in botoes:
            texto = item[0]
            linha = item[1]
            coluna = item[2]
            cor_bg = item[3] if len(item) > 3 else "#3B3B3B"
            rowspan = 2 if texto == "=" else 1

            btn = tk.Button(
                frame_botoes,
                text=texto,
                font=("Arial", 14, "bold"),
                bg=cor_bg,
                fg="#FFFFFF",
                activebackground="#555555",
                activeforeground="#FFFFFF",
                bd=0,
                relief="flat",
                command=lambda t=texto: self.ao_clicar_botao(t)
            )
            btn.grid(row=linha, column=coluna, rowspan=rowspan, sticky="nsew", padx=3, pady=3)

    def ao_clicar_botao(self, caractere):
        if caractere == "C":
            self.expressao = ""
            self.atualizar_visor("")
        elif caractere == "=":
            self.calcular_resultado()
        elif caractere == "√":
            self.aplicar_funcao_unaria(lambda x: math.sqrt(x))
        elif caractere == "sin":
            self.aplicar_funcao_unaria(lambda x: math.sin(math.radians(x)))
        elif caractere == "cos":
            self.aplicar_funcao_unaria(lambda x: math.cos(math.radians(x)))
        elif caractere == "tan":
            self.aplicar_funcao_unaria(lambda x: math.tan(math.radians(x)))
        elif caractere == "%":
            self.aplicar_funcao_unaria(lambda x: x / 100)
        else:
            if caractere == "^":
                self.expressao += "**"
            else:
                self.expressao += str(caractere)
            self.atualizar_visor(self.expressao)

    def atualizar_visor(self, texto):
        self.visor.delete(0, tk.END)
        self.visor.insert(0, texto)

    def aplicar_funcao_unaria(self, funcao):
        try:
            val = float(self.visor.get())
            resultado = funcao(val)
            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)
            else:
                resultado = round(resultado, 6)
            self.expressao = str(resultado)
            self.atualizar_visor(self.expressao)
        except Exception:
            self.atualizar_visor("Erro")
            self.expressao = ""

    def calcular_resultado(self):
        try:
            if not self.expressao:
                return
            resultado = eval(self.expressao, {"__builtins__": None}, {"math": math})
            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)
            else:
                resultado = round(resultado, 4)
            self.expressao = str(resultado)
            self.atualizar_visor(self.expressao)
        except ZeroDivisionError:
            self.atualizar_visor("Erro: Div/0")
            self.expressao = ""
        except Exception:
            self.atualizar_visor("Erro")
            self.expressao = ""

if __name__ == "__main__":
    janela = tk.Tk()
    app = CalculadoraGUI(janela)
    janela.mainloop()
