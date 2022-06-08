# importar o draw module como um objeto
import draw
# Importar alguma função / atributo específico
from draw import draw_game
# Importar todos os objetos de um módulo
from draw import *

def playGame():
    print("Jogandoo")
    return True

def main():
    result = playGame()
    draw_game(result)

# Isso significa que se o script for executado, então
# a função main() será executada
if __name__ == '__main__':
    main()

# Ou da pra fazer desse jeito, não? ("Talvez tenha algum motivo pra ser da forma acima")
main()

# Condicional Import
if True:
    import print as printModule
else:
    import draw as drawModule

print =  printModule.Print()
print.action()