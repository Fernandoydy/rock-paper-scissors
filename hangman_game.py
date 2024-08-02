import random

words = ["norte", "zinco", "vaso", "confessar", "desamparado", "neve", "tremulando", "enclausurado", "descobrir", "útil", "macabro", "bota", "impossível", "duradouro", "depender", "habilidoso", "rápido", "melhor", "dente", "matar", "roxo", "esquecido", "maneiro", "corpulento", "zumbido", "zebra", "dinâmico", "transbordar", "apressar", "racial", "bombeiro", "lâmpada", "declaração", "esquerda", "ajuste", "materialista", "raiz", "calças", "palavra", "alto", "levantar", "excursão", "coisas", "flores", "cobrir", "trilho", "sentido", "cauteloso", "simples", "machão", "público", "gritar", "brilhante", "sinônimo", "controle", "véu", "olhar", "eufórico", "desgrenhado", "rosa", "adequado", "fumaça", "lindo", "selvagem", "redemoinho", "morto", "igreja", "sussurrante", "reivindicar", "caule", "cama", "caprichoso", "sol", "lado", "criatura", "desastroso", "montanha", "volátil", "pitoresco", "magro", "sufocar", "grato", "nervoso", "merecer", "rolar", "bicicletas", "próximo", "pensamento", "fechar", "ideia", "cutucar", "aspirante", "pinho", "inquisitivo", "carente", "balançar", "aventureiro", "divergente", "experiente"]
correctWord = ""
tries = 6
playerTry = ""
wordSize = 0
draw = ""
correctTries = [] #lista p guardar chars acertados
drawPositions = [] #lista p guardar posiçoes dos acertos

def drawer():
    global draw, wordSize, drawPositions, playerTry, correctTries
    wordSize = len(correctWord)
    correctTries.append(playerTry)
    drawPositions = "_" * wordSize
    '''while correctTries in correctWord:
        print(correctTries)
'''
    print(correctTries)
    #print(drawPositions)
    if playerTry in correctWord:
        pass
    #print(draw)
def Start():
    global words, correctWord, playerTry, tries, correctTries
    correctWord = random.choice(words)
    print(correctWord)
    playerTry = input(f"Choose a letter, you have {tries} tries!\n")
    while tries >= 1:
        if playerTry in correctWord:
            drawer()
            playerTry = input(f"Correct! Pick another letter, you still have {tries}.\n")
        elif playerTry != correctWord:
            tries -= 1
            drawer()
            if tries == 0:
                print(f"GAME OVER!\n😂 L 😂 O 😂 S 😂 E 😂 R 😂")
                break
            playerTry = input(f"Wrong! Try again. You have {tries} more tries!\n")
            continue

Start()
#print(correctTries)
