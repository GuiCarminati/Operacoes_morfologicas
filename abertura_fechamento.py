import numpy as np
import cv2
import matplotlib.pyplot as plt

# abre imgem e mostra
imagem1 = cv2.imread('imagens/img2.png', 0)
plt.figure('Original 1')
plt.imshow(imagem1, cmap='gray')

imagem2 = cv2.imread('imagens/img3.png', 0)
plt.figure('Original 2')
plt.imshow(imagem2, cmap='gray')

# cria elemento estruturante
elem_e = np.ones((3, 3), np.uint8)

# aplica a operacao e mostra resultado
abertura = cv2.morphologyEx(imagem1, cv2.MORPH_OPEN, elem_e)
plt.figure('Abertura')
plt.imshow(abertura, cmap='gray')

fechamento = cv2.morphologyEx(imagem2, cv2.MORPH_CLOSE, elem_e)
plt.figure('Fechamento')
plt.imshow(fechamento, cmap='gray')

plt.show()
