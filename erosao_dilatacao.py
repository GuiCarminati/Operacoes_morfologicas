import numpy as np
import cv2
import matplotlib.pyplot as plt

# abre imgem e mostra
imagem = cv2.imread('imagens/img1.png', 0)
plt.imshow(imagem, cmap='gray')
plt.show()

# cria elemento estruturante
elem_e = np.ones((3, 3), np.uint8)
# ou utilizando funcao do opencv
# elem_e = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# aplica a operacao e mostra resultado
erosao = cv2.erode(imagem, elem_e, iterations=1)
plt.imshow(erosao, cmap='gray')
plt.show()
dilatacao = cv2.dilate(imagem, elem_e, iterations=1)
plt.imshow(dilatacao, cmap='gray')
plt.show()
