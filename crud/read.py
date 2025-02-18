import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Gandalf@1234r',
    database='crud',
)

cursor = conexao.cursor()

#COMANDO READ
comando = """
SELECT * from cliente
"""
cursor.execute(comando)
resultado = cursor.fetchall() #ler o bd
print(resultado)

cursor.close()
conexao.close()