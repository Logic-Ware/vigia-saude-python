import json
from query_user import verificar_credenciais, obter_usuario, cadastrar_medico, cadastrar_unidade, obter_unidades, obter_tipo_unidades, obter_unidade_usuario, obter_tipo_usuario
from funcoes import forcar_opcao

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

def cadastro_medico():
    nome = input("Nome: ")
    especialidade = input("Especialidade: ")
    n_crm = input("Nº CRM: ")
    telefone = input("Telefone: ")

    # Retornando listas das unidades pelo banco, para o usuário escolher
    print("\nUnidades cadastradas em nosso sistema:")
    lista_unidades = obter_unidades()
    for unidade in lista_unidades:
        print(f"{unidade[0]} - {unidade[1]}")
    lista_id = [unidade[0] for unidade in lista_unidades]
    
    unidade = int(forcar_opcao("\nSelecione a unidade em que está afiliado(a): ", list(map(str, lista_id))))

    email = input("E-mail: ")
    senha = input("Senha: ")

    cadastrar_medico(nome, especialidade, n_crm, telefone, email, senha, unidade)

    print(f"{nome}, seu cadastro foi concluído com sucesso!\nVocê será redirecionado para a página inicial.\n.\n.\n.\n")

def cadastro_unidade():
    nome = input("Nome da unidade: ")
    telefone = input("Telefone: ")
    cep = input("CEP: ")
    logradouro = input("Logradouro: ")
    estado = input("Estado: ")
    cidade = input("Cidade: ")
    num_cnes = input("Nº CNES: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    
    # Retornando listas dos tipos das unidades pelo banco, para o usuário escolher
    print("\nTipos de unidades cadastradas em nosso sistema:")
    lista_tipo_unidades = obter_tipo_unidades()
    for tipo in lista_tipo_unidades:
        print(f"{tipo[0]} - {tipo[1]}")
    lista_id = [tipo[0] for tipo in lista_tipo_unidades]    

    tipo = int(forcar_opcao("Selecione o tipo da sua unidade: ", list(map(str, lista_id))))

    cadastrar_unidade(nome, telefone, email, senha, cep, logradouro, estado, cidade, num_cnes, tipo)

    print(f"{nome}, seu cadastro foi concluído com sucesso!\nVocê será redirecionado para a página inicial.\n.\n.\n.\n")

def exibir_informacoes_usuario(user):
    usuario = obter_usuario(user)
    unidade = obter_unidade_usuario(user)
    if usuario is not None:
        # Dados do usuário
        print(f"\nOlá, {usuario[1]}, seus dados abaixo: ")
        print(f"Especialidade: {usuario[2]}")
        print(f"Nº CRM: {usuario[3]}")
        print(f"Telefone: {usuario[4]}")
        print(f"Email: {usuario[5]}")
        print(f"Unidade Afiliada: {unidade[1]}")
    
    exportar_json = forcar_opcao("\nDeseja exportar os dados para um arquivo JSON? (S/N)", ["S","N"])

    if exportar_json == 'S':
        # Criar um dicionário com os dados
        dados_para_exportar = {'Nome': usuario[1], 
            'Especialidade': usuario[2], 
            'Nº CRM:': usuario[3], 
            'Telefone' : usuario[4], 
            'Email': usuario[5], 
            'Unidade Afiliada': unidade[1]
        }
        
        # Nome do arquivo
        nome_arquivo = 'usuario.json'
        with open(nome_arquivo, 'w') as arquivo_json:
            json.dump(dados_para_exportar, arquivo_json)

        print(f"\nOs dados foram exportados para '{nome_arquivo}'.")
    else:
        print("Consulta não exportada.")
    
    print(".\n.\n.\n")

def exibir_informacoes_unidade(user):
    usuario = obter_usuario(user)
    unidade = obter_unidade_usuario(user)
    tipo_unidade = obter_tipo_usuario(unidade)
    print(tipo_unidade)
    if usuario is not None:
        # Dados do usuário
        print(f"\nOlá, {usuario[1]}, os dados da sua unidade abaixo: ")
        print(f"Nome Unidade: {unidade[1]}")
        print(f"Telefone: {unidade[2]}")
        print(f"Email: {unidade[3]}")
        print(f"Cep: {unidade[5]}")
        print(f"Logradouro: {unidade[6]}")
        print(f"Estado: {unidade[7]}")
        print(f"Cidade: {unidade[8]}")    
        print(f"Nº CNES: {unidade[9]}")
        print(f"Tipo de Unidade: {tipo_unidade[1]}")
    
    exportar_json = forcar_opcao("\nDeseja exportar os dados para um arquivo JSON? (S/N)", ["S","N"])

    if exportar_json == 'S':
        # Criar um dicionário com os dados
        dados_para_exportar = {'Medico': usuario[1], 
            'Nome Unidade': unidade[1], 
            'Telefone' : unidade[2],
            'Email': unidade[3], 
            'CEP': unidade[5],
            'Logradouro': unidade[6],
            'Estado': unidade[7], 
            'Cidade': unidade[8], 
            'Nº CNES:': unidade[9], 
            'Tipo de Unidade': tipo_unidade[1]
        }
        
        # Nome do arquivo
        nome_arquivo = 'unidade_medico.json'
        with open(nome_arquivo, 'w') as arquivo_json:
            json.dump(dados_para_exportar, arquivo_json)

        print(f"\nOs dados foram exportados para '{nome_arquivo}'.")
    else:
        print("Consulta não exportada.")

    print(".\n.\n.\n")