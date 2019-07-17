###############################################
#                                             #
#         Desafio dos Pixels Strider          #
# ___________________________________________ #
#                                             #
# Nome: Luiz Gustavo Braganca dos Santos      #
#                                             #
###############################################

# importando a biblioteca
from PIL import Image
import numpy as np


# Metodo para ler a quantidade de pixels
def le_quantidade(img):    
    quantidade = 0                         # variavel para contar quantidade de vermelhos
    array_pixels = imagem_para_array(img)  # array com a posicao dos pixels

    # verifica a imagem em busca de pixels vermelhos
    for pixel in iter(array_pixels):
        if pixel == (255, 0, 0):
            quantidade += 1
        # end if
    # end for

    return quantidade
# end le_quantidade()


def imagem_para_array(img):
    # cria um array auxiliar
    array = []

    # transforma a imagem em um array
    for pixel in iter(img.getdata()):
        array.append(pixel)
    # end for

    return array
# end le_imagem


if __name__ == "__main__":
    # pegando a imagem
    img = Image.open('challenge_strider.png')

    # pega a quantidade de pixels
    quantidade = le_quantidade(img)
    
    # mostra a quantidade de pixels vermelhos
    print("Quantidade =", quantidade, "pixels vermelhos")
# end main
