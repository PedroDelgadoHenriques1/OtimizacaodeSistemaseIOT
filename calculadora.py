import random


# Definindo as matrizes com os novos nomes
deslocamento = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

velocidade = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Criando uma matriz tempo como uma matriz 3x3
tempo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Realizando a divisão dos elementos e armazenando na matriz tempo
for i in range(3):
    for j in range(3):
        tempo[i][j] = deslocamento[i][j] / velocidade[i][j]

# Exibindo a matriz tempo como uma matriz 3x3
for linha in tempo:
    print(linha)


# Função para calcular os custos mínimo e máximo do caminho através da matriz dada uma sequência de colunas
def calcular_custos(tempo, sequencia):
    custos_minimos = []
    custos_maximos = []
# Cálculo da matriz transposta
    matriz_transposta = [[linha[coluna] for linha in tempo] for coluna in sequencia]
    
    for coluna in matriz_transposta:
        menor_valor = min(coluna)
        maior_valor = max(coluna)
        custos_minimos.append(menor_valor)
        custos_maximos.append(maior_valor)
        
        print(f"O menor valor encontrado na coluna foi: {menor_valor}")
        print(f"O maior valor encontrado na coluna foi: {maior_valor}")
    
    custo_total_minimo = sum(custos_minimos)
    custo_total_maximo = sum(custos_maximos)
    return custos_minimos, custos_maximos, custo_total_minimo, custo_total_maximo

# Sequência de colunas (começando na segunda coluna, indo até a última e retornando para a primeira)
sequencia = list(range(1, 3)) + [0]
print("Sequencia criada:")
print(sequencia)

# Cálculo dos custos mínimo e máximo
custos_minimos, custos_maximos, custo_total_minimo, custo_total_maximo = calcular_custos(tempo, sequencia)
print(f"Menores custos do caminho: {custos_minimos}")
print(f"Custo total mínimo do melhor caminho: {custo_total_minimo}")
print(f"Maiores custos do caminho: {custos_maximos}")
print(f"Custo total máximo do melhor caminho: {custo_total_maximo}")