#pip install requests
import requests
from time import sleep

class Tradutor:
    def __init__(self, source='en', target='pt'):
        self.lingua_source = source
        self.lingua_target = target
        
    def traduzir(self, texto_para_traducao):
        print('Traduzindo palavra...')
        sleep(0.8)

        # testando API para tradução 
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

        key_da_api = self._pega_chave_api()

        payload = f"q={texto_para_traducao}&target={self.lingua_target}&source={self.lingua_source}"
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
    
    def _pega_chave_api(self):
        with open('key_tradutor_API.txt', mode = 'r') as arquivo_chave:
            key_api = arquivo_chave.readline()
        
        
        return key_api
            
    def linguagens_disponiveis(self):

        url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

        key_da_api = self._pega_chave_api()

        headers = {
            'accept-encoding': "application/gzip",
            'x-rapidapi-host': "google-translate1.p.rapidapi.com",
            'x-rapidapi-key': f"{key_da_api}"
            }

        response = requests.request("GET", url, headers=headers)
        resposta = response.json()

        linguas = resposta['data']['languages']

        print('Linguagens disponíveis: ')
        for posicao, lingua in enumerate(linguas):
            print(lingua['language'], end =' - ')

            if posicao == len(linguas)-1:
                print(lingua['language'])
