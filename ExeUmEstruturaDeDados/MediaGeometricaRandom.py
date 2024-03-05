import random
def mediaGeometrica(lista):
    produto = 1
    for elemento in lista:
        produto *= elemento
    media = produto ** (1/len(lista))
    return media
def main():
    while True:
        n = int(input("Digite um valor N maior que 1: "))
        if n > 1:
            break
        else:
            print("Por favor, digite um valor N maior que 1.")
    lista = [random.randint(1, 100) for _ in range(n)]
    resultado = mediaGeometrica(lista)
    print(f"A média geométrica dos {n} elementos da lista é: {resultado}")

if __name__ == "__main__":
    main()