# módulo a ser importado em Python

print("__name__ no arquivo dois está definido como: {}" .format(__name__))

def function_three():
   print("Função três é executada")

def function_four():
   print("Função quatro é executada")

if __name__ == "__main__":
   print("Arquivo dois executado quando rodou diretamente")
else:
   print("Arquivo dois executado ao ser importado")