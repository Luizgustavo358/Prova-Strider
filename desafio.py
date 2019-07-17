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


# Metodo para ler a quantidade de pixels
def le_quantidade():
    # pegando a imagem
    img = Image.open('challenge_strider.png')
    quantidade = 0

    # verifica a imagem em busca de pixels vermelhos
    for pixel in img.getdata():
        if pixel == (255, 0, 0):
            quantidade += 1

    return quantidade
# end le_quantidade()


if __name__ == "__main__":
    # pega a quantidade de pixels
    quantidade = le_quantidade()

    # mostra a quantidade de pixels vermelhos
    print("Quantidade =", quantidade, "pixels vermelhos")
# end main
