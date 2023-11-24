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
            print(f"Bem-vindo, {user[1]}! Você entrou na sua conta.\n.\n.\n.\n")
        else:
            print("Falha ao entrar na conta. Verifique suas credenciais e tente novamente.")

    finally:
        # Fechar cursor e conexão
        cursor.close()
        conexao.close()

    return user

def cadastrar_medico(nome, especialidade, n_crm, telefone, email, senha, unidade):
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

def cadastrar_unidade(nome, telefone, email, senha, cep, logradouro, estado, cidade, num_cnes, tipo):
    # Conectar ao banco de dados
    conexao = oracledb.connect(user="rm99627", password="051298",
                               dsn="oracle.fiap.com.br:1521/orcl")
    cursor = conexao.cursor()

    # Usando parâmetros vinculados
    cursor.execute("INSERT INTO T_VGS_UNIDADE (nom_unidade, des_telefone_unidade, des_email_unidade, des_senha, des_cep_unidade, des_endereco_unidade, des_estado, des_cidade, num_cnes, id_tipo) VALUES (:nome, :telefone, :email, :senha, :cep, :logradouro, :estado, :cidade, :num_cnes, :tipo)",
                nome=nome, telefone=telefone, email=email, senha=senha, cep=cep, logradouro=logradouro, estado=estado, cidade=cidade, num_cnes=num_cnes, tipo=tipo)

    conexao.commit()  # Commit para efetivar a inserção

    # Fechar cursor e conexão
    cursor.close()
    conexao.close()

def cadastrar_caso(dat_nasc, des_genero, dat_diagnostico, estado_diagnostico, doenca):
    # Conectar ao banco de dados
    conexao = oracledb.connect(user="rm99627", password="051298",
                               dsn="oracle.fiap.com.br:1521/orcl")
    cursor = conexao.cursor()

    # Usando parâmetros vinculados
    cursor.execute("INSERT INTO T_VGS_CASOS (dat_nasc_paciente, des_genero_paciente, dat_diagnostico, des_estado_diagnostico, id_doenca) VALUES (:dat_nasc, :des_genero, :dat_diagnostico, :estado_diagnostico, :doenca)",
                dat_nasc=dat_nasc, des_genero=des_genero, dat_diagnostico=dat_diagnostico, estado_diagnostico=estado_diagnostico, doenca=doenca)

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
    cursor.execute(consulta, id=user[0])
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

# Função para obter os tipos de unidades logadas na sessão
def obter_tipo_unidades():
    # Conectar ao banco de dados
    conexao = oracledb.connect(user="rm99627", password="051298",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cursor = conexao.cursor()

    cursor.execute("SELECT id_tipo, des_tipo_unidade FROM T_VGS_TIPO_UNIDADE")
    tipo_unidades = cursor.fetchall()

    # Fechar cursor e conexão
    cursor.close()
    conexao.close()

    return tipo_unidades

# Função para obter as doencas logadas na sessão
def obter_doencas():
    # Conectar ao banco de dados
    conexao = oracledb.connect(user="rm99627", password="051298",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cursor = conexao.cursor()

    cursor.execute("SELECT id_doenca, nom_doenca FROM T_VGS_DOENCA")
    doencas = cursor.fetchall()

    # Fechar cursor e conexão
    cursor.close()
    conexao.close()

    return doencas

def alerta_pandemia(cod_cid_doenca, des_estado_diagnostico):
    # Conectar ao banco de dados
    conexao = oracledb.connect(user="rm99627", password="051298",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cursor = conexao.cursor()
    
    # Consultar a quantidade de casos associado ao cid e ao estado da tabela 'T_VGS_CASOS'
    consulta = '''
        SELECT COUNT(*) FROM T_VGS_CASOS
        WHERE id_doenca IN (SELECT id_doenca FROM T_VGS_DOENCA WHERE cod_cid_doenca = :cod)
        AND des_estado_diagnostico = :estado
    '''
    cursor.execute(consulta, cod=cod_cid_doenca, estado=des_estado_diagnostico)
    contador_casos = cursor.fetchone()[0]

    # Fechar cursor e conexão
    cursor.close()
    conexao.close()

    # Simples lógica de alerta, por exemplo, alertar se houver mais de 5 casos em um estado
    if contador_casos > 5:
        return True
    return False

def obter_cid_nome(id):
    # Conectar ao banco de dados
    conexao = oracledb.connect(user="rm99627", password="051298",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cursor = conexao.cursor()

    # Consultar o código cid pelo id doença da tabela 'T_VGS_DOENCA'
    cursor.execute("SELECT nom_doenca, cod_cid_doenca FROM T_VGS_DOENCA WHERE id_doenca = :id", id=id)
    cid_nome = cursor.fetchall()

    # Fechar cursor e conexão
    cursor.close()
    conexao.close()

    return cid_nome

def obter_ultimo_caso():
    # Conectar ao banco de dados
    conexao = oracledb.connect(user="rm99627", password="051298",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cursor = conexao.cursor()

    # Consultar o último caso cadastrado pelo id na tabela 'T_VGS_CASOS'
    cursor.execute("SELECT des_estado_diagnostico, id_doenca FROM T_VGS_CASOS ORDER BY id_caso DESC FETCH FIRST 1 ROW ONLY")
    ultimo_caso = cursor.fetchall()

    # Fechar cursor e conexão
    cursor.close()
    conexao.close()

    return ultimo_caso

def casos_estados(estado):        
    # Conectar ao banco de dados
    conexao = oracledb.connect(user="rm99627", password="051298",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cursor = conexao.cursor()

    # Consultar o código cid pelo id doença da tabela 'T_VGS_DOENCA'
    consulta = '''SELECT T_VGS_DOENCA.NOM_DOENCA, COUNT(*) AS NUM_CASOS
        FROM RM99627.T_VGS_CASOS
        JOIN RM99627.T_VGS_DOENCA ON T_VGS_CASOS.ID_DOENCA = T_VGS_DOENCA.ID_DOENCA
        WHERE T_VGS_CASOS.DES_ESTADO_DIAGNOSTICO = :estado
        GROUP BY T_VGS_DOENCA.NOM_DOENCA
        ORDER BY NUM_CASOS DESC
    '''
    cursor.execute(consulta, estado=estado)
    casos_estado = cursor.fetchall()

    # Fechar cursor e conexão
    cursor.close()
    conexao.close()

    return casos_estado
