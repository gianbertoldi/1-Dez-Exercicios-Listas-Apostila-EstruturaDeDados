def gerarPA(primeiroTermo, quantidadeTermos, razao):
    pa = [primeiroTermo + i * razao for i in range(quantidadeTermos)]
    soma_pa = sum(pa)
    return pa, soma_pa

def main():
    primeiroTermo = int(input("Digite o primeiro termo da PA: "))
    quantidadeTermos = int(input("Digite a quantidade de termos da PA: "))
    razao = int(input("Digite a razão da PA: "))

    pa, soma_pa = gerarPA(primeiroTermo, quantidadeTermos, razao)

    print("Valores do PA:", pa)
    print("Soma dos valores do PA:", soma_pa)

if __name__ == "__main__":
    main()