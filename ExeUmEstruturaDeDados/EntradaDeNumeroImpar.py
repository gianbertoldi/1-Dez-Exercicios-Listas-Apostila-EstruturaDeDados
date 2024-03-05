def CalculoDoFatorial(n):
    if n == 0:
        return 1
    else:
        return n * CalculoDoFatorial(n - 1)

def main():
    while True:
        n = int(input("Digite um numero impar maior que 1: "))
        if n > 1 and n % 2 == 1:
            break
        else:
            print("O numero deve ser ímpar e maior que 1, digite de acordo.")
    lista = []
    for i in range(n):
        while True:
            numero = int(input(f"Digite o {i + 1}º nmero inteiro positivo: "))
            if numero > 0:
                lista.append(numero)
                break
            else:
                print("O numero deve ser positivo, digite novamente.")
    CentroDaLista = lista[n // 2]
    fatorialDoCentroDaLista = CalculoDoFatorial(CentroDaLista)
    print(f"O fatorial do elemento central ({CentroDaLista}) é: {fatorialDoCentroDaLista}")

if __name__ == "__main__":
    main()