from user import entrar_na_conta, fazer_cadastro, exibir_informacoes_usuario

def forcar_opcao(msg, lista_opcoes):
    resposta = input(msg)
    while not resposta in lista_opcoes:
        resposta = input("Digite um valor válido por favor!")
    return resposta

def main():
    user = None

    # Exibição do menu inicial
    while user is None:
        escolhaLogin = int(
            forcar_opcao(
                "*** Bem-vindo(a) à Vigia Saúde! ***\n"
                "\nO que deseja fazer?"
                "\n1- Entrar"
                "\n2- Cadastrar-se"
                "\n3- Sair \n",
                ["1", "2", "3"],
            )
        )
        if escolhaLogin == 1:
            user = entrar_na_conta()
        elif escolhaLogin == 2:
            user = fazer_cadastro()
        else:
            print("Obrigado. Volte logo.")
            return

    # Exibição do menu de funcionalidades
    while True:
        escolhaMenu = int(
            forcar_opcao(
                "Este é nosso menu de funcionalidades:"
                "\n1 - Visualizar Dados de Usuário"
                "\n2 - Sair"
                "\nQual delas deseja utilizar? ",
                ["1", "2"],
            )
        )

        if escolhaMenu == 1:
            exibir_informacoes_usuario(user)
        else:
            print("Sessão encerrada!")
            return

main()