import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

classes = [(300, 400), (400, 500), (500, 600), (600, 700), (700, 800), (800, 900), (900, 1000), (1000, 1100), (1100, 1200)]
frequencias = [14, 46, 58, 76, 68, 62, 48, 22, 6]


pontos_medios = [(classe[0] + classe[1]) / 2 for classe in classes]


total_lotes = sum(frequencias)
media = sum(ponto_medio * freq for ponto_medio, freq in zip(pontos_medios, frequencias)) / total_lotes

frequencias_acumuladas = np.cumsum(frequencias)
classe_mediana_index = np.where(frequencias_acumuladas >= total_lotes / 2)[0][0]
limite_inferior = classes[classe_mediana_index][0]
frequencia_classe_mediana = frequencias[classe_mediana_index]
frequencia_acumulada_anterior = frequencias_acumuladas[classe_mediana_index - 1] if classe_mediana_index > 0 else 0
amplitude_classe = classes[classe_mediana_index][1] - classes[classe_mediana_index][0]

mediana = limite_inferior + ((total_lotes / 2 - frequencia_acumulada_anterior) / frequencia_classe_mediana) * amplitude_classe

classe_modal_index = np.argmax(frequencias)
limite_inferior_modal = classes[classe_modal_index][0]
frequencia_modal = frequencias[classe_modal_index]
frequencia_anterior = frequencias[classe_modal_index - 1] if classe_modal_index > 0 else 0
frequencia_posterior = frequencias[classe_modal_index + 1] if classe_modal_index < len(frequencias) - 1 else 0

moda = limite_inferior_modal + ((frequencia_modal - frequencia_anterior) / ((frequencia_modal - frequencia_anterior) + (frequencia_modal - frequencia_posterior))) * amplitude_classe

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda:.2f}")

variancia = sum(freq * ((ponto_medio - media) ** 2) for ponto_medio, freq in zip(pontos_medios, frequencias)) / total_lotes
desvio_padrao = np.sqrt(variancia)
print(f"Desvio Padrão: {desvio_padrao:.2f}")

def calcular_percentil(p):
    posicao = p * total_lotes / 100
    classe_index = np.where(frequencias_acumuladas >= posicao)[0][0]
    limite_inferior = classes[classe_index][0]
    frequencia_classe = frequencias[classe_index]
    frequencia_acumulada_anterior = frequencias_acumuladas[classe_index - 1] if classe_index > 0 else 0
    return limite_inferior + ((posicao - frequencia_acumulada_anterior) / frequencia_classe) * amplitude_classe

Q1 = calcular_percentil(25)
D3 = calcular_percentil(30)
D7 = calcular_percentil(70)
P15 = calcular_percentil(15)
P90 = calcular_percentil(90)

print(f"Q1: {Q1:.2f}")
print(f"D3: {D3:.2f}")
print(f"D7: {D7:.2f}")
print(f"P15: {P15:.2f}")
print(f"P90: {P90:.2f}")

