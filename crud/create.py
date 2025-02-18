import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Gandalf@1234r',
    database='crud',
)

cursor = conexao.cursor()

# COMANDO CREATE
comando = """
INSERT INTO cliente (nome, email, cpf, senha, telefone, endereco) 
VALUES ("Carlo Tevez","ctevezo@gmail.com","372.081.832-58","Tevez123","(11) 99472-8931","Rua Jaracatiá, 635 - Jardim Umarizal")
"""
cursor.execute(comando)
conexao.commit() #edita o bds
cursor.close()
conexao.close()