###############################################
#                                             #
#         Desafio dos Pixels Strider          #
# ___________________________________________ #
#                                             #
# Nome: Luiz Gustavo Braganca dos Santos      #
#                                             #
###############################################

# importando a biblioteca
from PIL import Image, ImageDraw
import numpy as np
import shutil


# Metodo para ler a quantidade de pixels
def le_quantidade(img):    
    quantidade = 0                            # variavel para contar quantidade de vermelhos
    array_pixels = imagem_para_array(img)     # array com a posicao dos pixels

    # # verifica a imagem em busca de pixels vermelhos
    # for pixel in img.getdata():
    #     if pixel == (255, 0, 0):
    #         quantidade += 1

    for pixel in iter(array_pixels):
        if pixel == (255, 0, 0):
            quantidade += 1

    return quantidade, array_pixels
# end le_quantidade()


def imagem_para_array(img):
    array = []

    for pixel in iter(img.getdata()):
        array.append(pixel)

    return array
# end le_imagem


def acha_mensagem(img, array):
    draw = ImageDraw.Draw(img)

    for i, j in iter(array), range(array):
        if i == (255, 0, 0):
            liga_pixels(draw, array[j], array[j+1])
# end acha_mensagem()


def liga_pixels(draw, primeiro, ultimo):
    # desenha uma linha ligando os pixels
    draw.line((primeiro, ultimo), width=1)
# end liga_pixels()


def clona_imagem():
    shutil.copy("challenge_strider.png", "copia.png")
# end clona_imagem()


if __name__ == "__main__":
    # pegando a imagem
    img = Image.open('challenge_strider.png')

    # clona a imagem original
    clona_imagem()

    # pega a quantidade de pixels
    quantidade, array_pixels = le_quantidade(img)

    # liga os pixels
    acha_mensagem(img, array_pixels)
    
    # mostra a quantidade de pixels vermelhos
    print("Quantidade =", quantidade, "pixels vermelhos")
# end main
