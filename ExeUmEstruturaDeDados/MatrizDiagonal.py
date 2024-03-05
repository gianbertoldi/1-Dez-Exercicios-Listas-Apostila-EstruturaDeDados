import random
def gerarMatrizAleatoria(numLinhas, numColunas):
    matriz = []
    for _ in range(numLinhas):
        linha = [random.randint(0, 9) for _ in range(numColunas)]
        matriz.append(linha)
    return matriz
def verificarMatrizDiagonal(matriz):
    numLinhas = len(matriz)
    numColunas = len(matriz[0])
    if numLinhas != numColunas:
        return False
    for i in range(numLinhas):
        for j in range(numColunas):
            if i != j and matriz[i][j] != 0:
                return False
    return True
def main():
    numLinhas = int(input("Digite o número de linhas da matriz: "))
    numColunas = int(input("Digite o número de colunas da matriz: "))

    matriz = gerarMatrizAleatoria(numLinhas, numColunas)

    if verificarMatrizDiagonal(matriz):
        print("A matriz é uma matriz diagonal.")
    else:
        print("A matriz não é uma matriz diagonal.")


if __name__ == "__main__":
    main()