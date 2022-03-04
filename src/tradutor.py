#pip install requests
import requests
from time import sleep

class Tradutor:
    def __init__(self, palavra, source='en', target='pt'):
        self.palavra_sem_traducao = palavra
        self.lingua_source = source
        self.lingua_target = target
        print('Traduzindo palavra...')
        sleep(0.8)
        self._palavra_traduzida = 'não está traduzido ainda, rode o método traduzir'


    def traduzir(self, palavra_para_traducao):
        # testando API para tradução 
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

        key_da_api = self.pega_chave_api()

        payload = f"q={palavra_para_traducao}&target={self.lingua_target}&source={self.lingua_source}"
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'accept-encoding': "application/gzip",
            'x-rapidapi-host': "google-translate1.p.rapidapi.com",
            'x-rapidapi-key': f"{key_da_api}" # Pegar a sua própia key na documentação da API
            }

        return self.resposta(url, payload, headers)

    def resposta(self, url, payload, headers):
        # fazendo busca com request e pegando os dados em json
        response = requests.request("POST", url, data=payload, headers=headers)
        response_json = response.json()

        nome_traduzido = response_json['data']['translations'][0]['translatedText']

        return  nome_traduzido
    
    def pega_chave_api(self):
        with open('key_tradutor_API.txt', mode = 'r') as arquivo_chave:
            key_api = arquivo_chave.readline()
        
        return key_api

if __name__ == "__main__":
    texto = 'I love you'
    traduzir = Tradutor(texto)
    
    print(traduzir.traduzir(texto))

    