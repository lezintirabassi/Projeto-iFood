import mysql.connector

conexao = mysql.connector.connect(
    host='crud-instance.c1uka62e40t7.sa-east-1.rds.amazonaws.com',
    user='admin',
    password='Impacta-2025',
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
