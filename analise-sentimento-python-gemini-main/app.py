import google.generativeai as genai

genai.configure(api_key="AIzaSyAmgGTQxa1HMLBpOK7OiNuFo4_8x9_gZ9A")

# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)
        
model = genai.GenerativeModel('gemini-pro')

# with open('texto1.txt', 'r', encoding='utf-8') as file:
#     texto = file.read()
    
# with open('texto2.txt', 'r', encoding='utf-8') as file:
#     texto = file.read()
    
# with open('texto3.txt', 'r', encoding='utf-8') as file:
#     texto = file.read()
    
# with open('texto4.txt', 'r', encoding='utf-8') as file:
#     texto = file.read()
    
with open('texto5.txt', 'r', encoding='utf-8') as file:
    texto = file.read()

comando = ( 
            "Por favor, realize uma análise simples e objetiva "\
             "do sentimento expresso na frase abaixo, "\
             "classificando-a como positiva, negativa ou neutra. "\
             "Identifique e liste os sentimentos específicos presentes, "\
             "em sua forma mais simples e direta (palavra primitiva)" \
             "tanto explícitos quanto implícitos, e avalie a intensidade de cada sentimento de 0 (zero) a 100. "\
             "Indique quais palavras-chave na sentença contribuíram " \
             "para os sentimentos identificados. "\
             "Em seguida, sugira possíveis razões para esses sentimentos "\
             "com base no contexto da frase. Por fim, explique como você chegou " \
             "a essas conclusões. Retorne todas essas informações " \
             "no seguinte formato de um objeto JSON valido e identado: " \
             "{" \
                "'classe': 'positivo, negativo ou neutro'," \
                "'sentimentos': {'sentimento': 'intensidade'}," \
                "'contribuicoes': {'palavra/frase': 'sentimento associado'}," \
                "'razoes_possiveis': ['string']," \
                "'explicacao_modelo': 'string'" \
            "}" \
            "O texto a ser analisado é esse:" \
            f"'{texto}'"
        )

response = model.generate_content(comando)

print(response.text)