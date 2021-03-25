import time
from random import randint
from Tamagushi import BichinhoEletronico
import jogadas


def main():

    fome = randint(50, 100)
    saude = randint(50, 100)
    tedio = randint(20, 100)
    tamagushi = BichinhoEletronico('tamagushi', fome, saude, 0, tedio)
    tamagushi.mudar_nome()

    sair = False

    while not sair:
        tempo_inicio = time.time()

        print(tamagushi)

        tamagushi, sair = jogadas.jogada(tamagushi)

        if sair:
            break

        tempo_fim = time.time()
        tamagushi, sair = jogadas.eventos(tamagushi, (tempo_fim - tempo_inicio))


main()
