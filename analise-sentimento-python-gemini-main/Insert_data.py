import json
import psycopg2

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname="datafeelings",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Defina o ID do cliente para o qual a análise será associada
cliente_id = 2

# Ler o JSON do arquivo
with open('resultado.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Inserir dados na tabela analisys
cursor.execute(
    """
    INSERT INTO analisys (cliente_id, classe, sentimento, contribuicoes, razoes_possiveis, explicacao_modelo)
    VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
    """,
    (
        cliente_id,
        data['classe'],
        json.dumps(data['sentimentos']),
        json.dumps(data['contribuicoes']),
        json.dumps(data['razoes_possiveis']),
        data['explicacao_modelo']
    )
)

# Confirmar as transações
conn.commit()

# Fechar a conexão
cursor.close()
conn.close()
