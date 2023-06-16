# JOGO DA FORCA UTILIZANDO 100 PALAVRAS DIFERENTES PARA JOGAR
# CRIADO POR MATHEUS JOSÉ DE LIMA COSTA
# GITHUB: https://github.com/MatheusCosta616

import random
from palavras import palavras


def jogar():
    print("""
        ************************************************
        ****************JOGO DA FORCA*******************
                            _______ 
                                  |
                                 (_)  
                                 \|/
                                  |  
                                 / /
        ************************************************
                       O JOGO COMEÇOU

    """)

    nome = str(input("Digite seu nome: \n"))
    print(f"Seja bem vindo {nome}")

    palavra_chave = random.choice(palavras)

    letras_acertadas = ["_" for i in palavra_chave]

    enforcou = False
    acertou = False
    erros = 0

    def imprime_mensagem_perdedor(palavra_secreta):
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

    def imprime_mensagem_vencedor():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    def desenha_forca(erros):
        print("  _______     ")
        print(" |/      |    ")

        if erros == 1:
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if erros == 2:
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if erros == 3:
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if erros == 4:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if erros == 5:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if erros == 6:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if erros == 7:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

    while not enforcou and not acertou:
        chute = input("Qual letra? \n").lower().strip()

        if len(chute) != 1:
            print("Apenas 1 caractere")
            continue

        if chute in palavra_chave:
            index = 0
            for i in palavra_chave:
                if chute.lower() == i.lower():
                    letras_acertadas[index] = i
                index += 1
            acertou = "_" not in letras_acertadas
        else:
            erros += 1
            enforcou = erros == 7
            desenha_forca(erros)

        print(letras_acertadas)

    if enforcou:
        print("Você foi enforcado! Fim de jogo.")
        imprime_mensagem_perdedor(palavra_chave)
    elif acertou:
        print("Parabéns! Você acertou a palavra. Fim de jogo.")
        imprime_mensagem_vencedor()


jogar()