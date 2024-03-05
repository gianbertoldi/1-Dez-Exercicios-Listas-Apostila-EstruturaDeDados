import random

def cadastrarRifas():
    numRifas = int(input("foi vendidas quantas rifas? "))
    rifas = []
    for i in range(numRifas):
        nome = input(f"Digite o nome de quem comprou a rifa {i+1}: ")
        rifas.append(nome)
    return rifas

def ganhadorDaRifa(rifas):
    ganhador = random.choice(rifas)
    return ganhador
def main():
    print("===========================")
    print("Rifas:")
    rifas = cadastrarRifas()
    print("------------------------")
    print("\nSorteando o ganhador...")
    ganhador = ganhadorDaRifa(rifas)
    print("------------------------")
    print(f"O ganhador da rifa é: {ganhador}")
    print("===========================")


if __name__ == "__main__":
    main()