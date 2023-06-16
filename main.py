#JOGO DA FORCA UTILIZANDO 100 PALAVRAS DIFERENTES PARA JOGAR
# CRIADO POR MATHEUS JOSÉ DE LIMA COSTA
#GITHUB: https://github.com/MatheusCosta616

import random
from palavras import palavras

def jogar():
    print("O JOGO COMEÇOU")

    nome = str(input("Digite seu nome: \n"))
    print(f"Seja bem vindo {nome}")

    palavra_chave = random.choice(palavras)

    letras_acertadas = ["_" for i in palavra_chave]

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = input("Qual letra? \n").lower()
        chute = chute.strip()

        if chute in palavra_chave:
            index = 0
            for i in palavra_chave:
                if chute.lower() == i.lower():
                    letras_acertadas[index] = i
                index += 1
            acertou = "_" not in letras_acertadas
        else:
            erros += 1
            enforcou = erros == 6

        print(letras_acertadas)

    if enforcou:
        print("Você foi enforcado! Fim de jogo.")
    elif acertou:
        print("Parabéns! Você acertou a palavra. Fim de jogo.")

jogar()