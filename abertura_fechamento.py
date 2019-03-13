import numpy as np
import cv2
import matplotlib.pyplot as plt

# abre imgem e mostra
imagem1 = cv2.imread('imagens/img2.png', 0)
plt.imshow(imagem1, cmap='gray')
plt.show()
imagem2 = cv2.imread('imagens/img3.png', 0)
plt.imshow(imagem2, cmap='gray')
plt.show()

# cria elemento estruturante
elem_e = np.ones((3, 3), np.uint8)

# aplica a operacao e mostra resultado
abertura = cv2.morphologyEx(imagem1, cv2.MORPH_OPEN, elem_e)
plt.imshow(abertura, cmap='gray')
plt.show()
fechamento = cv2.morphologyEx(imagem2, cv2.MORPH_CLOSE, elem_e)
plt.imshow(fechamento, cmap='gray')
plt.show()
