import numpy as np
import cv2
import matplotlib.pyplot as plt

# abre imgem e mostra
imagem = cv2.imread('imagens/img1.png', 0)
plt.figure('Original')
plt.imshow(imagem, cmap='gray')

# inverte imagem
imagem = cv2.bitwise_not(imagem)

# cria elemento estruturante
elem_e = np.ones((3, 3), np.uint8)

# aplica a operacao e mostra resultado
erosao = cv2.erode(imagem, elem_e, iterations=1)
erosao = cv2.bitwise_not(erosao)
plt.figure('Erosao com o complemento')
plt.imshow(erosao, cmap='gray')

dilatacao = cv2.dilate(imagem, elem_e, iterations=1)
dilatacao = cv2.bitwise_not(dilatacao)
plt.figure('Dilatacao com o complemento')
plt.imshow(dilatacao, cmap='gray')

plt.show()
