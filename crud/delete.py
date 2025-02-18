import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Gandalf@1234r',
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