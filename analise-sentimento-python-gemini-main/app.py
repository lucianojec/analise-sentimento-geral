from flask import Flask, request, jsonify
import google.generativeai as genai
import json
from datetime import datetime
from psycopg2 import connect, sql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Configura CORS para permitir todas as origens

genai.configure(api_key='AIzaSyAmgGTQxa1HMLBpOK7OiNuFo4_8x9_gZ9A')

model = genai.GenerativeModel('gemini-pro')

conn = connect(
    dbname="datafeelings",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.json
    texto = data.get('texto')
    cliente = data.get('cliente')
    email = data.get('email')

    if not texto or not cliente or not email:
        return jsonify({"error": "Texto, cliente e email são obrigatórios"}), 400

    comando = (
        "Por favor, realize uma análise simples e objetiva "
        "do sentimento expresso na frase abaixo, "
        "classificando-a como positiva, negativa ou neutra. "
        "Identifique e liste os sentimentos específicos presentes, "
        "em sua forma mais simples e direta (palavra primitiva) "
        "tanto explícitos quanto implícitos, e avalie a intensidade de cada sentimento de 0 (zero) a 100. "
        "Indique quais palavras-chave na sentença contribuíram "
        "para os sentimentos identificados. "
        "Em seguida, sugira possíveis razões para esses sentimentos "
        "com base no contexto da frase. Por fim, explique como você chegou "
        "a essas conclusões. Retorne todas essas informações "
        "no seguinte formato de um objeto JSON valido e identado: "
        "{"
        "\"classe\": \"positivo, negativo ou neutro\","
        "\"sentimentos\": {\"sentimento\": \"intensidade\"},"
        "\"contribuicoes\": {\"palavra/frase\": \"sentimento associado\"},"
        "\"razoes_possiveis\": [\"string\"],"
        "\"explicacao_modelo\": \"string\","
        "\"cliente\": \"" + cliente + "\","
        "\"email\": \"" + email + "\""
        "} "
        "O texto a ser analisado é esse: "
        f"\"{texto}\""
    )

    response = model.generate_content(comando)

    if response.text:
        try:
            response_corrected = response.text.replace("```json\n", "").replace("\n```", "")
            response_json = json.loads(response_corrected)
            response_json['cliente'] = cliente
            response_json['email'] = email
            return jsonify(response_json)
        except json.JSONDecodeError as e:
            return jsonify({"error": "Erro ao decodificar o JSON", "message": str(e)}), 500
    else:
        return jsonify({"error": "Resposta do modelo está vazia"}), 500

@app.route('/api/save', methods=['POST'])
def save_to_db():
    data = request.json
    cliente = data.get('cliente')
    email = data.get('email')
    classe = data.get('classe')
    contribuicoes = json.dumps(data.get('contribuicoes'))
    razoes_possiveis = json.dumps(data.get('razoes_possiveis'))
    explicacao_modelo = data.get('explicacao_modelo')
    data_insercao = datetime.now()

    if not cliente or not email or not classe or not contribuicoes or not razoes_possiveis or not explicacao_modelo:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    print(f"Saving to DB: cliente={cliente}, email={email}, classe={classe}, contribuicoes={contribuicoes}, razoes_possiveis={razoes_possiveis}, explicacao_modelo={explicacao_modelo}")

    try:
        query = sql.SQL("""
            INSERT INTO analisys (cliente_id, classe, contribuicoes, razoes_possiveis, explicacao_modelo, data_insercao, email)
            VALUES (
                (SELECT id FROM clientes WHERE nome = %s),
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            ) RETURNING id;
        """)
        values = (cliente, classe, contribuicoes, razoes_possiveis, explicacao_modelo, data_insercao, email)
        cur.execute(query, values)
        inserted_id = cur.fetchone()[0]

        # Inserindo sentimentos na tabela sentimentos
        for tipo, valor in data.get('sentimentos', {}).items():
            query_sentimento = sql.SQL("""
                INSERT INTO sentimentos (analisys_id, tipo, valor)
                VALUES (%s, %s, %s)
            """)
            cur.execute(query_sentimento, (inserted_id, tipo, valor))

        conn.commit()
        return jsonify({"success": True, "message": "Dados salvos com sucesso"})
    except Exception as e:
        conn.rollback()
        print(f"Error saving to DB: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
