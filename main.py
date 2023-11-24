from user import entrar_na_conta, exibir_informacoes_usuario, cadastro_medico, cadastro_unidade, cadastro_caso
from funcoes import forcar_opcao

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
            escolhaCadastro = int(
                forcar_opcao(
                    "\nCadastrar como médico ou como unidade:"
                    "\n1 - Médico"
                    "\n2 - Unidade",
                    ["1","2"]
                )
            )

            print("Para fazer o cadastro digite:")
            if escolhaCadastro == 1:
                user = cadastro_medico()
            else:
                user = cadastro_unidade()
        else:
            print("Obrigado. Volte logo.")
            return

    # Exibição do menu de funcionalidades
    while True:
        escolhaMenu = int(
            forcar_opcao(
                "Este é nosso menu de funcionalidades:"
                "\n1 - Registrar Novo Caso"
                "\n2 - Visualizar Dados de Usuário"
                "\n3 - Sair"
                "\nQual delas deseja utilizar? ",
                ["1", "2", "3"]
            )
        )

        if escolhaMenu == 1:
            cadastro_caso(user)
        elif escolhaMenu == 2:
            exibir_informacoes_usuario(user)
        else:
            print("Sessão encerrada!")
            return

main()