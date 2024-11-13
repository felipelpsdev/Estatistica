import numpy as np
import matplotlib.pyplot as plt


intervalos = [(300, 400), (400, 500), (500, 600), (600, 700), (700, 800), (800, 900), (900, 1000), (1000, 1100), (1100, 1200)]
frequencia = [14, 46, 58, 76, 68, 62, 48, 22, 6]


def pontos_medios(intervalos):
    return [(a + b) / 2 for a, b in intervalos]


def media(pontos, frequencia):
    total = sum(frequencia)
    return sum(p * f for p, f in zip(pontos, frequencia)) / total

def mediana(intervalos, frequencia, total):
    freq_acum = np.cumsum(frequencia)
    idx = np.where(freq_acum >= total / 2)[0][0]
    li = intervalos[idx][0]
    fa = frequencia[idx]
    f_acum_ant = freq_acum[idx - 1] if idx > 0 else 0
    amplitude = intervalos[idx][1] - intervalos[idx][0]
    return li + ((total / 2 - f_acum_ant) / fa) * amplitude

def moda(intervalos, frequencia):
    idx = np.argmax(frequencia)
    li = intervalos[idx][0]
    fa = frequencia[idx]
    f_ant = frequencia[idx - 1] if idx > 0 else 0
    f_post = frequencia[idx + 1] if idx < len(frequencia) - 1 else 0
    amplitude = intervalos[idx][1] - intervalos[idx][0]
    return li + ((fa - f_ant) / ((fa - f_ant) + (fa - f_post))) * amplitude

def desvio_padrao(pontos, frequencia, media, total):
    variancia = sum(f * ((p - media) ** 2) for p, f in zip(pontos, frequencia)) / total
    return np.sqrt(variancia)

def percentil(p, intervalos, frequencia, total):
    freq_acum = np.cumsum(frequencia)
    pos = p * total / 100
    idx = np.where(freq_acum >= pos)[0][0]
    li = intervalos[idx][0]
    fa = frequencia[idx]
    f_acum_ant = freq_acum[idx - 1] if idx > 0 else 0
    amplitude = intervalos[idx][1] - intervalos[idx][0]
    return li + ((pos - f_acum_ant) / fa) * amplitude

def plotar_grafico(intervalos, frequencia):
    intervalos_str = [f"{a}-{b}" for a, b in intervalos]
    plt.figure(figsize=(10, 6))
    plt.bar(intervalos_str, frequencia, color='green', edgecolor='black')
    plt.xlabel('Áreas (m³)')
    plt.ylabel('Número de Lotes')
    plt.title('Distribuição de Frequência das Áreas dos Lotes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    total = sum(frequencia)
    pontos = pontos_medios(intervalos)
    m = media(pontos, frequencia)
    med = mediana(intervalos, frequencia, total)
    mod = moda(intervalos, frequencia)
    dp = desvio_padrao(pontos, frequencia, m, total)

    q1 = percentil(25, intervalos, frequencia, total)
    d3 = percentil(30, intervalos, frequencia, total)
    d7 = percentil(70, intervalos, frequencia, total)
    p15 = percentil(15, intervalos, frequencia, total)
    p90 = percentil(90, intervalos, frequencia, total)

    print("Média: ", m)
    print("Mediana: ", med)
    print("Moda: ", mod)
    print("Desvio Padrão: ", dp)
    print("Q1 (1º quartil): ", q1)
    print("D3 (3º decis): ", d3)
    print("D7 (7º decis): ", d7)
    print("P15 (15º percentil): ", p15)
    print("P90 (90º percentil):", p90)

    
    plotar_grafico(intervalos, frequencia)

main()
