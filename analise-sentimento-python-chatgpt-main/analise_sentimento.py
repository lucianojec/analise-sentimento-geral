import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def analise_sentimento(texto: str) -> str:
    try:
        chave_api = getenv("CHAVE_API", None)
        # chave_api = "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"
        # modelo_engine = "text-davinci-005"
        modelo_engine = "gpt-3.5-turbo-instruct"
        # modelo_engine = "gpt-3.5-turbo"
        comando = ( 
            "Por favor, realize uma análise profunda e detalhada "\
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
             "no seguinte formato de um objeto JSON: " \
             "{" \
                "'classe': 'classe'," \
                "'sentimentos': {'sentimento': 'intensidade'}," \
                "'contribuicoes': {'palavra/frase': 'sentimento associado'}," \
                "'razoes_possiveis': ['string']," \
                "'explicacao_modelo': 'string'" \
            "}" \
            "O texto a ser analisado é esse:" \
            f"'{texto}'"
        )

        cabecalho = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {chave_api}",
        }

        dados = {
            "prompt": comando,
            "temperature": 0.7,
            "max_tokens": 1035,
            "n": 1,
            "stop": None,
        }

        reposta = requests.post(
            f"https://api.openai.com/v1/engines/{modelo_engine}/completions",
            # f"https://api.openai.com/v1/chat/completions",
            headers=cabecalho,
            json=dados,
        )

        reposta.raise_for_status()  # Isso lança uma exceção se o código de status não for 2xx

        return reposta.json()["choices"][0]["text"].strip().lower()
    
    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação: {e}")
        return f"Código de status: {reposta.status_code}"
    except Exception as e:
        print(f"Erro desconhecido: {e}")
        return f"Código de status: {reposta.status_code}"

if __name__ == "__main__":
    texto = "Fiquei extremamente feliz pela minha promoção, mas chateado porque meu amigo foi demitido."
    resultado = analise_sentimento(texto)
    print(resultado)
