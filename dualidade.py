import numpy as np
import cv2
import matplotlib.pyplot as plt

# abre imgem e mostra
imagem = cv2.imread('imagens/img1.png', 0)
plt.imshow(imagem, cmap='gray')
plt.show()

# inverte imagem
imagem = cv2.bitwise_not(imagem)

# cria elemento estruturante
elem_e = np.ones((3, 3), np.uint8)

# aplica a operacao e mostra resultado
erosao = cv2.erode(imagem, elem_e, iterations=1)
erosao = cv2.bitwise_not(erosao)
plt.imshow(erosao, cmap='gray')
plt.show()
dilatacao = cv2.dilate(imagem, elem_e, iterations=1)
dilatacao = cv2.bitwise_not(dilatacao)
plt.imshow(dilatacao, cmap='gray')
plt.show()
