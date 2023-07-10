from tkinter import *
import tkinter.messagebox
from time import sleep

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
        with open('dados.txt', 'r') as dados:
            linhas = dados.readlines()
            print(linhas)
            login_efetuado = False
            for linha in linhas:
                usuario_cadastrado = linha[0:linha.find(',')]
                senha_cadastrada = linha[linha.find(',')+1:len(linha)-1]
                usuario_digitado = input_usuario.get()
                senha_digitada = input_senha.get()
                print(usuario_digitado, senha_digitada)
                if usuario_digitado == usuario_cadastrado and senha_digitada == senha_cadastrada:
                    login_efetuado = True
                    print('Login efetuado com sucesso.')
            if login_efetuado:
                tkinter.messagebox.showinfo(title='Sucesso', message='Login efetuado com sucesso.')
            else:
                tkinter.messagebox.showerror(title='Ops', message='Usuário ou senha não estão cadastrados.')

# Destroi a janela de login e volta para a tela de escolha.
    def voltar_tela():
        janela_login.destroy()
        tela_escolha()
    # janela
    janela_login = Tk()
    janela_login.geometry("700x400+370+220")
    # mensagem escrita na tela
    texto = Label(janela_login, text='Sistema de Login')
    texto.pack(padx=10, pady=10)

    # Armazena o texto inserido pelo usuário
    input_usuario = StringVar()
    # entrada para escrever o usuário
    usuario = Entry(janela_login, textvariable=input_usuario)
    usuario.pack(padx=10, pady=10)

    # Armazena o texto inserido pelo usuário
    input_senha = StringVar()
    senha = Entry(janela_login, textvariable=input_senha, show='*')
    senha.pack(padx=10, pady=10)

    checkbox = Checkbutton(janela_login, text='Lembrar login?')
    checkbox.pack(padx=10, pady=10)
    # cria um botão na tela.
    botao = Button(janela_login, text='Fazer login', command=login)
    botao.pack(padx=10, pady=10)

    voltar_tela_escolha = Button(janela_login, text='Voltar', command=voltar_tela)
    voltar_tela_escolha.pack(padx=10, pady=10)
    # deixa a janela rodando
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
    definir_senha = Entry(janela_cadastro, textvariable=input_senha, show='*')
    definir_senha.pack(padx=10, pady=10)

    def voltar_tela():
        janela_cadastro.destroy()
        tela_escolha()

    def cadastrar():
        user = input_usuario.get()
        password = input_senha.get()
        usuario_e_senha = [user + ',' + password, '\n']
        with open('dados.txt', 'a') as arquivo_cadastro:
            arquivo_cadastro.writelines(usuario_e_senha)
        tkinter.messagebox.showinfo(title='Sucesso', message='Usuário e senha cadastrados com sucesso.')
        sleep(0.5)
        janela_cadastro.destroy()
        tela_de_login()

    confirmar_cadastro = Button(janela_cadastro, text='Cadastrar', command=cadastrar)
    confirmar_cadastro.pack(padx=10, pady=10)

    voltar_tela_principal = Button(janela_cadastro, text='Voltar', command=voltar_tela)
    voltar_tela_principal.pack(padx=10, pady=10)

    janela_cadastro.mainloop()
