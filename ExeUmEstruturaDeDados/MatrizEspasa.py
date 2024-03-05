import random
def gerarMatrizRandomica(numLinhas, numColunas):
    matriz = []
    for _ in range(numLinhas):
        linha = [random.randint(0, 9) for _ in range(numColunas)]
        matriz.append(linha)
    return matriz
def verificarMatrizEspasa(matriz):
    numLinhas = len(matriz)
    numColunas = len(matriz[0])
    zeros = 0
    diferenteDeZero = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == 0:
                zeros += 1
            else:
                diferenteDeZero += 1

    if zeros > diferenteDeZero:
        return True
    else:
        return False
def main():
    numLinhas = int(input("Digite o número de linhas da matriz: "))
    numColunas = int(input("Digite o número de colunas da matriz: "))
    matriz = gerarMatrizRandomica(numLinhas, numColunas)
    if verificarMatrizEspasa(matriz):
        print("A matriz é uma matriz esparsa.")
    else:
        print("A matriz não é uma matriz esparsa.")
if __name__ == "__main__":
    main()