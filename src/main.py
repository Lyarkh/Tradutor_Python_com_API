from tradutor import Tradutor

class Principal:
    def main(self):
        tradutor = Tradutor()
        texto = 'let it go'

        traducao = tradutor.traduzir(texto)
        
        print(traducao)
    
if __name__ == "__main__":
    Principal().main()