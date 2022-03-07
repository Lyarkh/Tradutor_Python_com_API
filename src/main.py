from tradutor import Tradutor

class Principal:
    def main(self):
        tradutor = Tradutor()
        texto = 'let it go'

        traducao = tradutor.traduzir(texto)
        
        print(traducao)
    
    def verificando_linguagens(self):
        tradutor = Tradutor()
        tradutor.linguagens_disponiveis()
    
if __name__ == "__main__":
    Principal().verificando_linguagens()