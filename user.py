from query import verificar_credenciais, obter_usuario, cadastrar_medico, cadastrar_unidade, obter_unidades, obter_tipo_unidades, obter_unidade_usuario

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

def fazer_cadastro_medico():
    nome = input("Nome: ")
    especialidade = input("Especialidade: ")
    n_crm = input("Nº CRM: ")
    telefone = input("Telefone: ")

    # Retornando listas das unidades pelo banco, para o usuário escolher
    print("\nUnidades cadastradas em nosso sistema:")
    lista_unidades = obter_unidades()
    for unidade in lista_unidades:
        print(f"{unidade[0]} - {unidade[1]}")
    
    unidade = int(input("\nSelecione a unidade em que está afiliado(a): "))

    lista_id = [unidade[0] for unidade in lista_unidades]
    while not unidade in lista_id:
        unidade = int(input("Digite um valor válido por favor! "))

    email = input("E-mail: ")
    senha = input("Senha: ")

    cadastrar_medico(nome, especialidade, n_crm, telefone, email, senha, unidade)

    print(f"{nome}, seu cadastro foi concluído com sucesso!\nVocê será redirecionado para a página inicial.\n.\n.\n.\n")

def fazer_cadastro_unidade():
    nome = input("Nome da unidade: ")
    telefone = input("Telefone: ")
    cep = input("CEP: ")
    logradouro = input("Logradouro: ")
    estado = input("Estado: ")
    cidade = input("Cidade: ")
    num_cnes = input("Nº CNES: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    print("\nTipos de unidades cadastradas em nosso sistema:")
    lista_tipo_unidades = obter_tipo_unidades()
    for tipo in lista_tipo_unidades:
        print(f"{tipo[0]} - {tipo[1]}")
    
    tipo = int(input("\nSelecione o tipo da sua unidade: "))

    lista_id = [tipo[0] for tipo in lista_tipo_unidades]
    while not tipo in lista_id:
        tipo = int(input("Digite um valor válido por favor! "))

    cadastrar_unidade(nome, telefone, email, senha, cep, logradouro, estado, cidade, num_cnes, tipo)

    print(f"{nome}, seu cadastro foi concluído com sucesso!\nVocê será redirecionado para a página inicial.\n.\n.\n.\n")

def exibir_informacoes_usuario(user):
    usuario = obter_usuario(user)
    unidade = obter_unidade_usuario(user)
    if usuario is not None:
        # Dados do usuário
        print(f"\n{usuario[1]}")
        print(f"Especialidade: {usuario[2]}")
        print(f"Nº CRM: {usuario[3]}")
        print(f"Telefone: {usuario[4]}")
        print(f"Email: {usuario[5]}")
        print(f"Unidade afiliada: {unidade}\n")
