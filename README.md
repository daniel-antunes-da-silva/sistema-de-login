# sistema-de-login
Sistema de cadastro e login com interface gráfica usando tkinter
É possível cadastrar novos usuários em um simulador de banco de dados (com arquivo .txt), 
e fazer login verificando se o usuário e senha realmente existem. O usuário e senha são 
separados por vírgula.

Ao fazer cadastro de um novo usuário, aparece uma tela de sucesso, e a janela é fechada para abrir a de login.
Ao fazer o login com usuário e senha que existam, aparece uma mensagem de que foi efetuado com sucesso.
Caso o usuário ou senha não existam, é exibida uma mensagem de erro, informando que os dados não estão
no banco de dados.

# Demonstração na prática:

Tela de escolha (cadastro ou login):

![Tela de escolha](https://github.com/daniel-antunes-da-silva/sistema-de-login-tkinter/assets/132831685/d274cd23-7055-46ef-8b9f-232a33ec6fde)


Tela de cadastro:

![Tela de cadastro](https://github.com/daniel-antunes-da-silva/sistema-de-login-tkinter/assets/132831685/a239ab1b-3d45-4cea-aa5d-be5f2c565fc3)

Os usuários cadastrados ficam em um arquivo de texto para posterior autenticação:

![usuarios cadastrados](https://github.com/daniel-antunes-da-silva/sistema-de-login-tkinter/assets/132831685/0f606265-b4b0-47e6-9141-97a74f2e5f0a)


Tela de login:

![Tela Login](https://github.com/daniel-antunes-da-silva/sistema-de-login-tkinter/assets/132831685/0f601a5e-7f1b-49e9-b7fa-97a652d0a909)

Caso o usuário e senha inseridos estejam corretos, é exibido uma mensagem de sucesso. Caso contrário, é exibido mensagem de que usuário e/ou senha estão incorretos.

![Sucesso](https://github.com/daniel-antunes-da-silva/sistema-de-login-tkinter/assets/132831685/aeda069e-5442-4574-97c4-7cd048d010c3)           ![falha_login](https://github.com/daniel-antunes-da-silva/sistema-de-login-tkinter/assets/132831685/8d31af16-ca81-4120-b74e-09da2f3cf33a)

Para utilizar o programa, clonar o repositório e rodar o arquivo "sistema.py".
