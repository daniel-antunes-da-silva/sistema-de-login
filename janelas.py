from tkinter import *


def tela_escolha():
    janela_escolha = Tk()
    janela_escolha.geometry("500x250")

    def abrir_tela_login():
        janela_escolha.destroy()
        tela_de_login()

    def abrir_tela_cadastro():
        janela_escolha.destroy()
        tela_de_cadastro()

    escolha_login = Button(janela_escolha, text='Fazer login', command=abrir_tela_login)
    escolha_login.pack(padx=10, pady=10)

    escolha_cadastro = Button(janela_escolha, text='Fazer cadastro', command=abrir_tela_cadastro)
    escolha_cadastro.pack(padx=10, pady=10)

    janela_escolha.mainloop()


def tela_de_login():
    def login():
        user = input_usuario.get()
        password = input_senha.get()
        print(user, password)

    def voltar_tela():
        janela_login.destroy()
        tela_escolha()

    janela_login = Tk()
    janela_login.geometry("700x400+370+220")

    texto = Label(janela_login, text='Sistema de Login')
    texto.pack(padx=10, pady=10)

    input_usuario = StringVar()
    usuario = Entry(janela_login, textvariable=input_usuario)
    usuario.pack(padx=10, pady=10)

    input_senha = StringVar()
    senha = Entry(janela_login, textvariable=input_senha, show='*')
    senha.pack(padx=10, pady=10)

    checkbox = Checkbutton(janela_login, text='Lembrar login?')
    checkbox.pack(padx=10, pady=10)

    botao = Button(janela_login, text='Fazer login', command=login)
    botao.pack(padx=10, pady=10)

    voltar_tela_escolha = Button(janela_login, text='Voltar', command=voltar_tela)
    voltar_tela_escolha.pack(padx=10, pady=10)

    janela_login.mainloop()


def tela_de_cadastro():
    janela_cadastro = Tk()
    janela_cadastro.geometry("500x250")

    mensagem_cadastro = Label(text='Cadastro de usuário')
    mensagem_cadastro.pack(padx=10, pady=10)

    input_usuario = StringVar()
    definir_usuario = Entry(janela_cadastro, textvariable=input_usuario)
    definir_usuario.pack(padx=10, pady=10)

    input_senha = StringVar()
    definir_senha = Entry(janela_cadastro, textvariable=input_senha)
    definir_senha.pack(padx=10, pady=10)

    def voltar_tela():
        janela_cadastro.destroy()
        tela_escolha()

    voltar_tela_principal = Button(janela_cadastro, text='Voltar', command=voltar_tela)
    voltar_tela_principal.pack(padx=10, pady=10)

    janela_cadastro.mainloop()
