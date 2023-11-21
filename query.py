import cx_Oracle

def verificar_credenciais(email, senha):
    con = cx_Oracle.connect(user="rm99627", password="051298",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cur = con.cursor()

    user = None
    try:
        # Consulta SQL para verificar se há um usuário com o email e senha fornecidos
        cur.execute(
            "SELECT * FROM T_VGS_MEDICO WHERE des_email = :email AND des_senha = :senha", email=email, senha=senha)
        user = cur.fetchone()

        if user:
            print(f"Olá {user[1]}, você entrou na sua conta.\n")
        else:
            print(
                "\nFalha ao entrar na conta. Verifique suas credenciais e tente novamente.")

    finally:
        cur.close()
        con.close()
        return user