import oracledb

def verificar_credenciais(email, senha):
    # Conectar ao banco de dados
    conexao = oracledb.connect(user="rm99627", password="051298",
                               dsn="oracle.fiap.com.br:1521/orcl")
    cursor = conexao.cursor()

    user = None

    try:
        # Consultar se há um usuário com o email e senha fornecidos
        consulta = """
            SELECT * FROM T_VGS_MEDICO
            WHERE des_email = :email AND des_senha = :senha
        """
        cursor.execute(consulta, email=email, senha=senha)
        user = cursor.fetchone()

        if user:
            print(f"Bem-vindo, {user[1]}! Você entrou na sua conta.\n")
        else:
            print("Falha ao entrar na conta. Verifique suas credenciais e tente novamente.")

    finally:
        # Fechar cursor e conexão
        cursor.close()
        conexao.close()

    return user

def cadastrar_usuario(nome, especialidade, n_crm, telefone, email, senha, unidade):
    # Conectar ao banco de dados
    conexao = oracledb.connect(user="rm99627", password="051298",
                               dsn="oracle.fiap.com.br:1521/orcl")
    cursor = conexao.cursor()

    # Usando parâmetros vinculados
    cursor.execute("INSERT INTO T_VGS_MEDICO (nom_medico, des_especialidade, num_crm, des_telefone, des_email, des_senha, id_unidade) VALUES (:nome, :especialidade, :n_crm, :telefone, :email, :senha, :id_unidade)",
                nome=nome, especialidade=especialidade, n_crm=n_crm, telefone=telefone, email=email, senha=senha, id_unidade=unidade)

    conexao.commit()  # Commit para efetivar a inserção

    # Fechar cursor e conexão
    cursor.close()
    conexao.close()

# Função para obter informações do usuário logado na sessão
def obter_usuario(user):
    # Conectar ao banco de dados
    conexao = oracledb.connect(user="rm99627", password="051298",
                               dsn="oracle.fiap.com.br:1521/orcl")
    cursor = conexao.cursor()

    try:
        # Consultar informações do usuário pelo ID
        consulta = "SELECT * FROM T_VGS_MEDICO WHERE id_medico = :id"
        cursor.execute(consulta, id=user[0])
        usuario = cursor.fetchone()

    finally:
        # Fechar cursor e conexão
        cursor.close()
        conexao.close()

    return usuario

def obter_unidade_usuario(user):
    # Conectar ao banco de dados
    conexao = oracledb.connect(user="rm99627", password="051298",
                               dsn="oracle.fiap.com.br:1521/orcl")
    cursor = conexao.cursor()

    # Consultar o nome da unidade da tabela 'T_VGS_UNIDADE' associado ao ID do médico fornecido.
    consulta = """
        SELECT T_VGS_UNIDADE.nom_unidade
        FROM T_VGS_MEDICO
        JOIN T_VGS_UNIDADE ON T_VGS_MEDICO.id_unidade = T_VGS_UNIDADE.id_unidade
        WHERE T_VGS_MEDICO.id_medico = :id
    """
    cursor.execute(consulta, id=user[7])
    unidade = cursor.fetchone()

    # Fechar cursor e conexão
    cursor.close()
    conexao.close()

    return unidade[0]


# Função para obter as unidades logadas na sessão
def obter_unidades():
    # Conectar ao banco de dados
    conexao = oracledb.connect(user="rm99627", password="051298",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cursor = conexao.cursor()

    cursor.execute("SELECT id_unidade, nom_unidade FROM T_VGS_UNIDADE")
    unidades = cursor.fetchall()

    # Fechar cursor e conexão
    cursor.close()
    conexao.close()

    return unidades
