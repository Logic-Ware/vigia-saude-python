from datetime import datetime

def forcar_opcao(msg, lista_opcoes):
    resposta = input(msg)
    while not resposta in lista_opcoes:
        resposta = input("Digite um valor válido por favor! ")
    return resposta

def estados(msg):
    resposta = input(msg)
    estados_brasileiros = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", 
    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", 
    "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    while not resposta in estados_brasileiros:
        resposta = input("Digite uma sigla de um estado válido por favor!")
    return resposta

# Convertendo a string da data para o formato de data
def data_valida(msg):
    while True:
        data_str = input(msg)
        try:
            data = datetime.strptime(data_str, "%Y-%m-%d").date()
            return data
        except ValueError:
            print("Formato de data inválido. Certifique-se de seguir o formato YYYY-MM-DD.")

    