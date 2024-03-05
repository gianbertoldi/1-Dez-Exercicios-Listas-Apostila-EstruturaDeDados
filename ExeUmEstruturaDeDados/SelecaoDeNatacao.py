def addTempos():
    tempos = {}
    for i in range(7):
        nome = input("Digite o nome do nadador: ")
        tempo = float(input(f"Digite o tempo do nadador {nome} (em segundos): "))
        print(f"----------------------------------------")
        tempos[nome] = tempo
    return tempos

def relatorio(tempos):
    melhorTempo = min(tempos, key=tempos.get)
    piorTempo = max(tempos, key=tempos.get)
    tempoMedio = sum(tempos.values()) / len(tempos)

    print(f"----------------------------------------")
    print(f"Relatorio da seletiva de natação:")
    print(f"a. Aluno com o melhor tempo: {melhorTempo} - {tempos[melhorTempo]} segundos")
    print(f"b. Aluno com o pior desempenho: {piorTempo} - {tempos[piorTempo]} segundos")
    print(f"c. Tempo médio dos alunos: {tempoMedio} segundos")

def main():
    tempos = addTempos()
    relatorio(tempos)


if __name__ == "__main__":
    main()
