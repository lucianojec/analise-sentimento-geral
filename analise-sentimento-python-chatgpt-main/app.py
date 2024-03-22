from avaliacoes_clientes import avaliacoes_clientes
from analise_sentimento import analise_sentimento
import json

# Nome do arquivo de saída
nome_arquivo = "saida_avaliacoes.json"

# Abrir o arquivo em modo de gravação ('w' para escrever) com a codificação 'utf-8'
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    # Iterar sobre as avaliações dos clientes
    for texto in avaliacoes_clientes:
        # Realizar a análise de sentimento
        sentimento = analise_sentimento(texto)

        # Converter o dicionário para uma string JSON com recuo
        resultado_json = json.dumps(sentimento, ensure_ascii=False, indent=2)
        
        # Remover caracteres de quebra de linha e escrever a string no arquivo
        arquivo.write(resultado_json)

# Mensagem indicando que a operação foi concluída
print(f"A saída foi impressa no arquivo {nome_arquivo}.")
