# -*- coding: utf-8 -*-
"""Biomec_Cruzreta
"""

#Camera 1
print("Escreva os dados da Camera 1")
xc1 = float(input("Agora, escreva a coordenada x da camera 1: "))
yc1 = float(input("Agora, escreva a coordenada y da camera 1: "))


#Projeção 1
print("Escreva os dados da projeção da Camera 1")
xp1 = float(input("Agora, escreva a coordenada x da projeção da camera 1: "))
yp1 = float(input("Agora, escreva a coordenada y da projeção da camera 1: "))



#Camera 2
print("Escreva os dados da Camera 2")
xc2 = float(input("Agora, escreva a coordenada x da camera 2: "))
yc2 = float(input("Agora, escreva a coordenada y da camera 2: "))


#Projeção 2
print("Escreva os dados da projeção da Camera 2")
xp2 = float(input("Agora, escreva a coordenada x da projeção da camera 2: "))
yp2 = float(input("Agora, escreva a coordenada y da projeção da camera 2: "))

import matplotlib.pyplot as plt
import numpy as np


mr1 = (yp1 - yc1) / (xp1 - xc1)
mr2 = (yp2 - yc2) / (xp2 - xc2)

br1 = -1 * (mr1 * xc1 - yc1) #Coeficiente linear da r1
br2 = -1 * (mr2 * xc2 - yc2) #Coeficiente linear da r2

 #r1 = mr1*xc1 + br1
 #r2 = mr2*xc1 + br1

#Ponto do cruzamento
xi = (-(mr2*xc2) + yc2 + (mr1*xc1) - yc1) / (mr1 - mr2) #x do cruzamento

yi = (mr1*xi)  - (mr1*xc1) + yc1 #y do cruzamento

#Posição do objeto reconstruído
print("xi =", xi)
print("yi =", yi)


#Gráfico
x1 = np.linspace(0,3,100)
y1 = mr1*x1 +br1

x2 = np.linspace(0,3,100)
y2 = mr2*x2 +br2

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.scatter(xi,yi, color = 'black') #Posição do objeto no plano xy - Ponto preto
plt.scatter(xc1,yc1, color = 'purple') #Posição da câmera 1 no plano xy - Ponto roxo
plt.scatter(xc2,yc2, color = 'blue') #Posição da câmera 2 no plano xy - Ponto azul

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title("Cruzamento de retas")
plt.show()

#r1 = yc1 + mr1(x - xc1)
#r2 = yc2 + mr2(x - xc2)
