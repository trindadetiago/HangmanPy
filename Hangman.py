from random import randint

words = open("words.txt", "r")
def draw(OneToSix):

    if OneToSix == 0:
        print("_______")
        print("|     |")
        print("|      ")
        print("|        ")
        print("|        ")
    if OneToSix == 1:
        print("_______")
        print("|     |")
        print("|     O")
        print("|        ")
        print("|        ")
    if OneToSix == 2:
        print("_______")
        print("|     |")
        print("|     O")
        print("|     | ")
        print("|        ")
    if OneToSix == 3:
        print("_______")
        print("|     |")
        print("|     O")
        print("|    /|  ")
        print("|        ")
    if OneToSix == 4:
        print("_______")
        print("|     |")
        print("|     O")
        print("|    /|\\")
        print("|        ")
    if OneToSix == 5:
        print("_______")
        print("|     |")
        print("|     O")
        print("|    /|\\")
        print("|    /'  ")
    if OneToSix == 6:
        print("_______")
        print("|     |")
        print("|     O")
        print("|    /|\\")
        print("|    /'\\")

def selectword():
    x = randint(1, 1000)
    list = words.readlines()
    return list[x]

word = selectword().rstrip()
words.close()

letras_usadas = []
letters = {}
def upd():
    letters.clear()
    for l in word:
        if not l in letras_usadas:
            letters[l] = "_"
        else:
            letters[l] = str(l)

def check():
    upd()
    if "_" in letters.values():
        return False
    else:
        return True

def guess(chances):
    if check():
        draw(chances)
        print("\nVOCÊ VENCEU!\nA palavra é "+ word)

    else:
        if(chances) > 5:
            draw(chances)
            print("\nVOCÊ PERDEU!\nA palavra era: " + word.upper())
            return
        else:
            upd()
            draw(chances)
            for i in word:
                if i in letters:
                    print(letters[i], end= "")
            for l in letras_usadas:
                print("\t"+ l.upper(), end= "")
            myguess = str(input("\nDigite sua letra:"))
            if (myguess.isalpha()) and len(myguess) == 1:
                if myguess in letras_usadas:
                    print("\nLetra já usada")
                    guess(chances)
                else:
                    letras_usadas.append(myguess)
                    if not myguess in word:
                        chances += 1
                        guess(chances)
                    else:
                        guess(chances)
            else:
                print("Tente novamente")
                guess(chances)


print("HANGMAN")
guess(0)
