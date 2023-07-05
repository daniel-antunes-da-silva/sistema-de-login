from customtkinter import *


def clique():
    print('Testando')


set_appearance_mode("Dark")
set_default_color_theme("dark-blue")
janela = CTk()
janela.geometry("700x400+370+220")

texto = CTkLabel(janela, text='Sistema de Login')
texto.pack(padx=10, pady=10)

usuario = CTkEntry(janela, placeholder_text='Seu usuário')
usuario.pack(padx=10, pady=10)

senha = CTkEntry(janela, placeholder_text='Sua senha', show='*')
senha.pack(padx=10, pady=10)

checkbox = CTkCheckBox(janela, text='Lembrar login?')
checkbox.pack(padx=10, pady=10)

botao = CTkButton(janela, text='Fazer login', command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()

#
# janela = tkinter.Tk()
# janela.geometry("700x400+370+220")
#
# texto = tkinter.Label(janela, text='Sistema de Login')
# texto.pack(padx=10, pady=10)
#
# botao = tkinter.Button(janela, text='Login', command=clique)
# botao.pack(padx=10, pady=10)
#
# janela.mainloop()
#
# '''from tkinter import *
# class Login:
#     def __init__(self, raiz):
#         self.raiz = raiz
#         self.raiz.title("Sistema de Login")
#         self.largura_tela = winfo_reqwidth()
#         self.raiz.geometry("1200x600+100+50")
#
#
# raiz = Tk()
# objeto = Login(raiz)
# raiz.mainloop()'''

