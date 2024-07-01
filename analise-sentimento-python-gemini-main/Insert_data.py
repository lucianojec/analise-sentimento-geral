import json
import psycopg2
from datetime import datetime

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
cliente_id = 10

# Ler o JSON do arquivo
with open('resultado.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Obter a data e hora atuais
data_atual = datetime.now()

# Inserir dados na tabela analisys
cursor.execute(
    """
    INSERT INTO analisys (cliente_id, classe, contribuicoes, razoes_possiveis, explicacao_modelo, data_insercao)
    VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
    """,
    (
        cliente_id,
        data['classe'],
        json.dumps(data['contribuicoes']),
        json.dumps(data['razoes_possiveis']),
        data['explicacao_modelo'],
        data_atual
    )
)
analisys_id = cursor.fetchone()[0]

# Inserir dados na tabela sentimentos
sentimentos = data['sentimentos']
for sentimento, intensidade in sentimentos.items():
    cursor.execute(
        """
        INSERT INTO sentimentos (analisys_id, tipo, valor)
        VALUES (%s, %s, %s)
        """,
        (
            analisys_id,
            sentimento,
            intensidade
        )
    )

# Confirmar as transações
conn.commit()

# Fechar a conexão
cursor.close()
conn.close()

print("Dados inseridos com sucesso.")
