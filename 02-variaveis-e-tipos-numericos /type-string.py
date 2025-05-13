import tkinter as tk

# Função que será chamada quando o botão for clicado
def somar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado.set(f"Resultado: {n1 + n2}")
    except ValueError:
        resultado.set("Erro: digite números válidos")

# Janela principal
janela = tk.Tk()
janela.title("Somador Simples")

# Variável para mostrar o resultado
resultado = tk.StringVar()

# Widgets
tk.Label(janela, text="Número 1:").pack()
entrada1 = tk.Entry(janela)
entrada1.pack()

tk.Label(janela, text="Número 2:").pack()
entrada2 = tk.Entry(janela)
entrada2.pack()

tk.Button(janela, text="Somar", command=somar).pack(pady=5)
tk.Label(janela, textvariable=resultado).pack()

# Loop principal da interface
janela.mainloop()
