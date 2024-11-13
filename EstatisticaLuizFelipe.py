import numpy as np
import matplotlib.pyplot as plt


intervalos = [(300, 400), (400, 500), (500, 600), (600, 700), (700, 800), (800, 900), (900, 1000), (1000, 1100), (1100, 1200)]
freqs = [14, 46, 58, 76, 68, 62, 48, 22, 6]


def pontos_medios(intervalos):
    return [(a + b) / 2 for a, b in intervalos]


def media(pontos, freqs):
    total = sum(freqs)
    return sum(p * f for p, f in zip(pontos, freqs)) / total

def mediana(intervalos, freqs, total):
    freq_acum = np.cumsum(freqs)
    idx = np.where(freq_acum >= total / 2)[0][0]
    li = intervalos[idx][0]
    fa = freqs[idx]
    f_acum_ant = freq_acum[idx - 1] if idx > 0 else 0
    amplitude = intervalos[idx][1] - intervalos[idx][0]
    return li + ((total / 2 - f_acum_ant) / fa) * amplitude

def moda(intervalos, freqs):
    idx = np.argmax(freqs)
    li = intervalos[idx][0]
    fa = freqs[idx]
    f_ant = freqs[idx - 1] if idx > 0 else 0
    f_post = freqs[idx + 1] if idx < len(freqs) - 1 else 0
    amplitude = intervalos[idx][1] - intervalos[idx][0]
    return li + ((fa - f_ant) / ((fa - f_ant) + (fa - f_post))) * amplitude

def desvio_padrao(pontos, freqs, media, total):
    variancia = sum(f * ((p - media) ** 2) for p, f in zip(pontos, freqs)) / total
    return np.sqrt(variancia)

def percentil(p, intervalos, freqs, total):
    freq_acum = np.cumsum(freqs)
    pos = p * total / 100
    idx = np.where(freq_acum >= pos)[0][0]
    li = intervalos[idx][0]
    fa = freqs[idx]
    f_acum_ant = freq_acum[idx - 1] if idx > 0 else 0
    amplitude = intervalos[idx][1] - intervalos[idx][0]
    return li + ((pos - f_acum_ant) / fa) * amplitude

def plotar_grafico(intervalos, freqs):
    intervalos_str = [f"{a}-{b}" for a, b in intervalos]
    plt.figure(figsize=(10, 6))
    plt.bar(intervalos_str, freqs, color='skyblue', edgecolor='black')
    plt.xlabel('Áreas (m³)')
    plt.ylabel('Número de Lotes')
    plt.title('Distribuição de Frequência das Áreas dos Lotes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    total = sum(freqs)
    pontos = pontos_medios(intervalos)
    m = media(pontos, freqs)
    med = mediana(intervalos, freqs, total)
    mod = moda(intervalos, freqs)
    dp = desvio_padrao(pontos, freqs, m, total)

    q1 = percentil(25, intervalos, freqs, total)
    d3 = percentil(30, intervalos, freqs, total)
    d7 = percentil(70, intervalos, freqs, total)
    p15 = percentil(15, intervalos, freqs, total)
    p90 = percentil(90, intervalos, freqs, total)

    print(f"Média: {m:.2f}")
    print(f"Mediana: {med:.2f}")
    print(f"Moda: {mod:.2f}")
    print(f"Desvio Padrão: {dp:.2f}")
    print(f"Q1 (1º quartil): {q1:.2f}")
    print(f"D3 (3º decis): {d3:.2f}")
    print(f"D7 (7º decis): {d7:.2f}")
    print(f"P15 (15º percentil): {p15:.2f}")
    print(f"P90 (90º percentil): {p90:.2f}")

    
    plotar_grafico(intervalos, freqs)

main()
