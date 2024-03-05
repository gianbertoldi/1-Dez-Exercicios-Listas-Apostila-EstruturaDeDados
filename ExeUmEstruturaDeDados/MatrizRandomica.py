import random
def gerarMatriz(numeroLinhas, numeroColunas):
    matriz = []
    for _ in range(numeroLinhas):
        linha = [random.random() for _ in range(numeroColunas)]
        matriz.append(linha)
    return matriz
def verificarMatrizNula(matriz):
    for linha in matriz:
        for valor in linha:
            if valor != 0:
                return False
    return True

# Função principal
def main():
    numLinhas = int(input("Digite o tamanho de linhas da matriz: "))
    numColunas = int(input("Digite o tamanho de colunas da matriz: "))
    matriz = gerarMatriz(numLinhas, numColunas)
    if verificarMatrizNula(matriz):
        print("É uma matriz nula.")
    else:
        print("Não é uma matriz nula.")

if __name__ == "__main__":
    main()