from query import verificar_credenciais, obter_usuario, cadastrar_usuario, obter_unidades

def entrar_na_conta():
    usuario_logado = None
    while usuario_logado is None:
        email = input("Digite o seu e-mail: ")
        senha = input("Digite a sua senha: ")
        usuario_logado = verificar_credenciais(email, senha)

        if usuario_logado:
            return usuario_logado
        else:
            usuario_logado = None

def fazer_cadastro():
    print("Para fazer o cadastro digite:")
    nome = input("Nome: ")
    especialidade = input("Especialidade: ")
    n_crm = input("Nº CRM: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    print("\nUnidades cadastradas em nosso sistema:\n")
    lista_unidades = obter_unidades()
    for unidade in lista_unidades:
        print(f"{unidade[0]} - {unidade[1]}")
    
    unidade = int(input("\nSelecione a unidade em que está afiliado(a): "))

    lista_id = [unidade[0] for unidade in lista_unidades]
    while not unidade in lista_id:
        unidade = int(input("Digite um valor válido por favor! "))

    cadastrar_usuario(nome, especialidade, n_crm, telefone, email, senha, unidade)

    print(f"{nome}, seu cadastro foi concluído com sucesso!\nVocê será redirecionado para a página inicial.\n.\n.\n.\n")


def exibir_informacoes_usuario(user):
    usuario = obter_usuario(user)
    if usuario is not None:
        # Dados do usuário
        print(f"\n{usuario[1]}")
        print(f"Especialidade: {usuario[2]}")
        print(f"Nº CRM: {usuario[3]}")
        print(f"Telefone: {usuario[4]}")
        print(f"Email: {usuario[5]}\n")
