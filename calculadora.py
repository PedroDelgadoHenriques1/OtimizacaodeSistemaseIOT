import random


# Definindo as matrizes com os novos nomes
deslocamento = [
    [41.3, 21, 12.8],
    [31, 25.6, 14],
    [32.5, 28.4, 11]
]

velocidade = [
    [31, 41, 32.5],
    [27, 44, 33],
    [34, 48, 20.6]
]

# Criando uma matriz tempo como uma matriz 3x3
tempo = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

#matriz bloqueio
matriz_bloqueio = [[1, 1, 0],
                   [0, 0, 1],
                   [0, 0, 0]]


# Realizando a divisão dos elementos e armazenando na matriz tempo
for i in range(3):
    for j in range(3):
        tempo[i][j] = deslocamento[i][j] / velocidade[i][j]

# Exibindo a matriz tempo como uma matriz 3x3
for linha in tempo:
    print(linha)


# Função para calcular os custos mínimo e máximo do caminho através da matriz dada uma sequência de colunas
def calcular_custos(tempo, sequencia, matriz_bloqueio):
    custos_minimos = []
    custos_maximos = []
    
    # Cálculo da matriz transposta
    matriz_transposta = [[linha[coluna] for linha in tempo] for coluna in sequencia]
    
    for i, (coluna, bloqueio) in enumerate(zip(matriz_transposta, matriz_bloqueio)):
        # Verifica se o índice está bloqueado (valor 1 na matriz de bloqueio)
        if bloqueio == 1:
            continue  # Pula esta coluna
        
        menor_valor = min(coluna)
        maior_valor = max(coluna)
        custos_minimos.append(menor_valor)
        custos_maximos.append(maior_valor)
        
        for j in range(0, 3):
            print(f"O menor valor encontrado na coluna {j+1} foi: {menor_valor}")
            print(f"O maior valor encontrado na coluna {j+1} foi: {maior_valor}")
    
    custo_total_minimo = sum(custos_minimos)
    custo_total_maximo = sum(custos_maximos)
    return custos_minimos, custos_maximos, custo_total_minimo, custo_total_maximo

# Sequência de colunas (começando na segunda coluna, indo até a última e retornando para a primeira)
sequencia = list(range(1, 3)) + [0]
print("Sequencia criada:")
print(sequencia)

# Cálculo dos custos mínimo e máximo
custos_minimos, custos_maximos, custo_total_minimo, custo_total_maximo = calcular_custos(tempo, sequencia, matriz_bloqueio)

print(f"Menores custos do caminho: {custos_minimos*60}")
print(f"Custo total mínimo do melhor caminho: {custo_total_minimo*60}")
print(f"Maiores custos do caminho: {custos_maximos*60}")
print(f"Custo total máximo do melhor caminho: {custo_total_maximo*60}")