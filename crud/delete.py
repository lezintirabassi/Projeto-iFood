import mysql.connector

conexao = mysql.connector.connect(
    host='crud-instance.c1uka62e40t7.sa-east-1.rds.amazonaws.com',
    user='admin',
    password='Impacta-2025',
    database='crud',
)

cursor = conexao.cursor()

cursor = conexao.cursor()

comando = """
DELETE FROM cliente WHERE nome = 'Evandro Corado'
"""
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
