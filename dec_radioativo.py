
import matplotlib.pyplot as plt
import numpy as np

# Equação diferencial
def f(t, y, Q):
    return Q * y

# Parâmetros da equação
t_inicial = 0
y_inicial = 50
t_final = 10

# Criação de listas para armazenar os valores
t_list = [t_inicial]
y_list = [y_inicial]

# Método de Euler para o cálculo dos valores
Q = -0.0525
h = 0.0001
t = t_inicial
y = y_inicial
while t < t_final:
    y = y + h * f(t, y, Q)
    t = t + h
    t_list.append(t)
    y_list.append(y)

# Plotagem dos resultados
plt.plot(t_list, y_list, 'b-', label='Decaimento Radiativo')
plt.xlabel('Tempo (anos)')
plt.ylabel('Quantidade (mg)')
plt.legend(loc='best')
plt.show()

print('Final: ', y_list[-1])