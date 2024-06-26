import google.generativeai as genai
import json
import os

genai.configure(api_key="AIzaSyAmgGTQxa1HMLBpOK7OiNuFo4_8x9_gZ9A")

model = genai.GenerativeModel('gemini-pro')

with open('texto4.txt', 'r', encoding='utf-8') as file:
    texto = file.read()

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
    "\"explicacao_modelo\": \"string\""
    "} "
    "O texto a ser analisado é esse: "
    f"\"{texto}\""
)

response = model.generate_content(comando)

# Exibir a resposta no console
# print(response.text)

# Verificar se a resposta não está vazia e converter aspas simples para aspas duplas
if response.text:
    try:
        # Remove a formatação indesejada na string
        response_corrected = response.text.replace("```json\n", "").replace("\n```", "")
        response_json = json.loads(response_corrected)

        # Definir o caminho para salvar o arquivo JSON na pasta public do frontend
        frontend_public_path = os.path.join(
            'C:\\git\\analise-sentimento-geral\\frontend-analise-sentimento\\my-app\\public', 'resultado.json'
        )

        # Salvar a resposta em um arquivo JSON na pasta public do frontend
        with open('resultado.json', 'w', encoding='utf-8') as json_file:
            json.dump(response_json, json_file, ensure_ascii=False, indent=4)
            
    except json.JSONDecodeError as e:
        print("Erro ao decodificar o JSON:", e)
else:
    print("Resposta do modelo está vazia.")
