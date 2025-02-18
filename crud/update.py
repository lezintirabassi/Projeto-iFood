import mysql.connector

conexao = mysql.connector.connect(
    host='crud-instance.c1uka62e40t7.sa-east-1.rds.amazonaws.com',
    user='admin',
    password='Impacta-2025',
    database='crud',
)

cursor = conexao.cursor()

comando = """
UPDATE cliente set nome = 'Vampeta' WHERE telefone = '(11) 94713-8776'
"""
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
