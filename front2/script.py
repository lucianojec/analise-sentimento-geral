import psycopg2
import json

def get_data():
    conn = psycopg2.connect(
        dbname="datafeelings",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Query para obter os dados dos clientes
    cursor.execute("SELECT id, nome FROM clientes")
    clientes = cursor.fetchall()

    # Query para obter as análises, incluindo a data de inserção
    cursor.execute("SELECT cliente_id, classe, sentimento, data_insercao FROM analisys")
    analisys = cursor.fetchall()

    # Fechar a conexão
    cursor.close()
    conn.close()

    # Estrutura de dados a ser retornada
    data = {
        "clientes": [{"id": c[0], "nome": c[1]} for c in clientes],
        "analisys": [
            {
                "cliente_id": a[0],
                "classe": a[1],
                "sentimento": a[2],  # Já é um dicionário Python, não precisa de json.loads
                "data_insercao": a[3].isoformat()  # Converter datetime para string no formato ISO 8601
            } for a in analisys
        ]
    }
    return data

# Salvar os dados em um arquivo JSON
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(get_data(), f, ensure_ascii=False, indent=4)
