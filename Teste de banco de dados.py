import pyodbc

# Estabelece a conexão com o banco de dados
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=KONSSUP20\SQLEXPRESS;'
                      'Database=Teste;'
                      'Trusted_Connection=yes;')

# Cria um cursor para executar as consultas
cursor = conn.cursor()

# Executa uma consulta
cursor.execute('SELECT * FROM Tarefa')

# Lê o resultado da consulta
for row in cursor:
    print(row)

# Fecha a conexão
conn.close()
