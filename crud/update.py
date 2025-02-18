import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Gandalf@1234r',
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