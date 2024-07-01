import psycopg2
import json
from datetime import datetime, timedelta
import random

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname="datafeelings",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Lista de clientes
clientes = [
    (1, 'bmg'),
    (2, 'bradesco'),
    (3, 'itau'),
    (4, 'simpress'),
    (5, 'sem parar'),
    (6, 'banco toyota'),
    (7, 'banco master'),
    (8, 'endered'),
    (9, 'santander'),
    (10, 'b3'),
    (11, 'dasa'),
    (12, 'crefisa')
]

# Inserir clientes na tabela clientes
cursor.executemany(
    "INSERT INTO clientes (id, nome) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING", clientes
)

# Função para gerar uma data aleatória entre duas datas
def random_date(start, end):
    return start + timedelta(days=random.randint(0, int((end - start).days)))

# Datas de início e fim
start_date = datetime(2023, 1, 1)
end_date = datetime.now()

# Sentimentos e classes para dados fictícios
sentimentos_positivos = [
    {"alegria": 50, "orgulho": 60, "satisfação": 70},
    {"gratidão": 80, "entusiasmo": 65, "reconhecimento": 75}
]

sentimentos_negativos = [
    {"decepção": 60, "frustração": 75, "preocupação": 50},
    {"insatisfação": 40, "irritação": 55, "tristeza": 65}
]

contribuicoes = {
    "positivos": ["Entrega antecipada", "Atendimento excelente", "Qualidade do produto"],
    "negativos": ["Atraso na entrega", "Falta de comunicação", "Produto com defeito"]
}

razoes_possiveis = {
    "positivos": ["Equipe dedicada", "Bom planejamento", "Uso de tecnologias avançadas"],
    "negativos": ["Problemas logísticos", "Falta de recursos", "Erro humano"]
}

explicacao_modelo = "O sentimento foi identificado com base na análise das palavras-chave e seu contexto no texto."

# Gerar e inserir dados fictícios nas tabelas analisys e sentimentos
for cliente in clientes:
    for _ in range(10):  # Inserir 10 registros por cliente
        if cliente[1] in ['simpress', 'b3']:
            sentimento = {"amigavel": random.randint(70, 100)}
            classe = "positiva"
        else:
            sentimento = random.choice(sentimentos_positivos if random.random() > 0.5 else sentimentos_negativos)
            classe = "positiva" if sentimento in sentimentos_positivos else "negativa"
        
        data_insercao = random_date(start_date, end_date)

        # Inserir análise
        cursor.execute(
            """
            INSERT INTO analisys (cliente_id, classe, contribuicoes, razoes_possiveis, explicacao_modelo, data_insercao)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
            """,
            (
                cliente[0],
                classe,
                json.dumps(random.choice(contribuicoes["positivos" if classe == "positiva" else "negativos"])),
                json.dumps(random.choice(razoes_possiveis["positivos" if classe == "positiva" else "negativos"])),
                explicacao_modelo,
                data_insercao
            )
        )
        analisys_id = cursor.fetchone()[0]

        # Inserir sentimentos
        for tipo, valor in sentimento.items():
            cursor.execute(
                """
                INSERT INTO sentimentos (analisys_id, tipo, valor)
                VALUES (%s, %s, %s)
                """,
                (analisys_id, tipo, valor)
            )

# Confirmar as transações
conn.commit()

# Fechar a conexão
cursor.close()
conn.close()

print("Dados inseridos com sucesso.")
