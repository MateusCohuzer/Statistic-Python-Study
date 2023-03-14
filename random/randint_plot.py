from random import randint

import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


def get_spreadSheet(lista):
    frequencia = {valor: lista.count(valor) for valor in set(lista)}
    df = pd.DataFrame.from_dict({'Valor': list(frequencia.keys()), 'Frequência': list(frequencia.values())})
    return df


numbers = []
for i in range(0, 1000):
    numbers.append(randint(0, 10)-randint(0, 10))

df = get_spreadSheet(numbers)

x = df['Valor']
y = df['Frequência']

plt.bar(x, y)
plt.title('Distribuição populacional da função Randint')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.show()
