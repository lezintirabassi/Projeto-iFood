import mysql.connector

conexao = mysql.connector.connect(
    host='crud-instance.c1uka62e40t7.sa-east-1.rds.amazonaws.com',
    user='admin',
    password='Impacta-2025',
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
