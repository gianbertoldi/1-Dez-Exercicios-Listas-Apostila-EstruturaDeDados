def mediaGeometrica(lista):
    menor = min(lista)
    maior = max(lista)
    media = (menor * maior) ** 0.5
    return media

def main():
    lista = []
    tamanho = int(input("Digite o tamanho da lista: "))
    print("Coloque os valores para preencher a lista:")
    for i in range(tamanho):
        elemento = float(input(f"Digite o {i+1}º elemento: "))
        lista.append(elemento)
    resultado = mediaGeometrica(lista)

    print(f"A média geometrica entre o menor e o maior elemento da lista é: {resultado}")

if __name__ == "__main__":
    main()