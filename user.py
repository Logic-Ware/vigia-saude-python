from query import verificar_credenciais

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

'''def fazer_cadastro():
    print("Para fazer o cadastro digite:")
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    telefone = input("Telefone para contato: ")
    cpf = input("CPF: ")
    cep = input("Cep: ")

    cadastrar_usuario_no_bd(nome, email, senha, telefone, cpf, cep)
    usuario_cadastrado = obter_ultimo_usuario()

    print(
        f"{usuario_cadastrado[1]}, seu cadastro foi concluído com sucesso!\nVocê será redirecionado para a página inicial.\n.\n.\n.")

def exibir_informacoes_usuario(user):
    usuario = obter_usuario_no_bd(user)
    if usuario is not None:
        # Dados do usuário
        print(f"\n{usuario[1]}")
        print(f"Email: {usuario[2]}")
        print(f"Telefone: {usuario[4]}")
        print(f"CPF: {usuario[5]}")
        print(f"CEP: {usuario[6]}\n")'''
