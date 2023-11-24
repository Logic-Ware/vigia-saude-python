from query import obter_usuario, cadastrar_caso, obter_doencas, alerta_pandemia, obter_ultimo_caso, obter_cid_nome, casos_estados
from funcoes import forcar_opcao, estados, data_valida

def cadastro_caso(user):
    dat_nasc = data_valida("Data de nascimento do paciente (YYYY-MM-DD): ")
    des_genero = int(forcar_opcao("Gênero do paciente:"
            "\n1 - Feminino"
            "\n2 - Masculino\n", ["1", "2"]))

    if des_genero == 1:
        des_genero = "Feminino"
    else:
        des_genero = "Masculino"

    dat_diagnostico = data_valida("Data do diagnóstico (YYYY-MM-DD): ")
    estado_diagnostico = estados("Estado de origem do diagnóstico: ")

    # Retornando listas das doenças pelo banco, para o usuário escolher
    print("\nQual foi a doença diagnosticada? ")
    lista_doencas = obter_doencas()
    for doenca in lista_doencas:
        print(f"{doenca[0]} - {doenca[1]}")
    lista_id = [doenca[0] for doenca in lista_doencas]
    
    doenca = int(forcar_opcao("Selecione a doença: ", list(map(str, lista_id))))

    cadastrar_caso(dat_nasc, des_genero, dat_diagnostico, estado_diagnostico, doenca)
    
    nome_usuario = obter_usuario(user)
    print(f"{nome_usuario[1]}, o caso foi cadastrado em nosso sistema com sucesso!\nVocê será redirecionado para a página inicial.\n.\n.\n.\n")

def notificar_pandemia():
    ultimo_caso = obter_ultimo_caso()
    estado_diagnosticado = ultimo_caso[0][0]
    id_doenca = ultimo_caso[0][1]

    dados_doenca = obter_cid_nome(id_doenca)
    cod_cid = dados_doenca[0][1]
    nom_doenca = dados_doenca[0][0]

    if alerta_pandemia(cod_cid, estado_diagnosticado):
        print(f"ALERTA: Possível surto de {nom_doenca} em {estado_diagnosticado}! Notifique as autoridades de saúde.")

def casos_crescentes():
    estado = estados("Digite o seu estado, para calcularmos os casos registrados: ")
    casos_por_estado = casos_estados(estado)

    print(f"\n{'Doença':<20}{'Casos em ' + estado:>10}")
    for caso in casos_por_estado:
        print(f"{caso[0]:<20}{caso[1]:<10}")

    # Foi utilizado paramêtros pequenos para testar
    if caso[1] > 5:
        print(f"ALERTA: Possível surto de {caso[0]} em {estado}! Notifique as autoridades de saúde.") 
    elif caso[1] > 2 and caso[1] < 5: 
        print(f"CUIDADO: A doença {caso[0]} está se espalhando em: {estado}! Fique de olho nos casos.") 
    else:
        print(f"Nenhuma possível pandemia em seu estado!")

    print("\n.\n.\n.\n")