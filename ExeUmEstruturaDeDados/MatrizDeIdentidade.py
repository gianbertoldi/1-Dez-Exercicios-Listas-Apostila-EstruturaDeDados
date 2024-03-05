def criarMatrizZeros(numLinhas, numColunas):
    return [[0] * numColunas for _ in range(numLinhas)]
def matrizIdentidade(matriz):
    numeroLinhas = len(matriz)
    numeroColunas = len(matriz[0])
    if numeroLinhas != numeroColunas:
        return False
    for i in range(numeroLinhas):
        for j in range(numeroColunas):
            if i == j and matriz[i][j] != 1:
                return False
            elif i != j and matriz[i][j] != 0:
                return False
    return True
def main():
    numLinhas = int(input("Quantidade de linhas da matriz: "))
    numColunas = int(input("Quantidade de colunas da matriz: "))
    matriz = criarMatrizZeros(numLinhas, numColunas)
    print("Digite os valores da matriz:")
    for i in range(numLinhas):
        for j in range(numColunas):
            matriz[i][j] = float(input(f"Digite o valores da posição ({i + 1}, {j + 1}): "))
    if matrizIdentidade(matriz):
        print("A matriz é uma matriz identidade.")
    else:
        print("A matriz não é uma matriz identidade.")
if __name__ == "__main__":
    main()