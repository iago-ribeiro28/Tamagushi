def alimentar(player):
    opcao = input('Deseja alimentar? [S/N]').strip().upper()

    if opcao[0] == 'S':
        player.red_fome(30)

        print("{} foi alimentado!".format(player.nome))

    else:
        print("{} Não foi alimentado.".format(player.nome))


def medicar(player):
    opcao = input('Deseja medicar? [S/N]').strip().upper()

    if opcao[0] == 'S':
        player.medicar(30)
        print(f'{player.nome} foi medicado.')

    else:
        print(f'{player.nome} não foi medicado.')


def brincar(player):
    opcao = input('Deseja brincar? [S/N]').strip().upper()

    if opcao[0] == 'S':
        player.brincar(30)
        print(f'Você brincou com o(a) {player.nome} .')

    else:
        print(f'Você não brincou com o(a) {player.nome}.')


def eventos(player, segundos):
    sair = False

    player.envelhecer(segundos)

    player.aum_fome(int(segundos // 2))

    player.reduz_saude(int(segundos // 1))

    player.aum_tedio(int(segundos // 1))

    if player.idade >= 100:
        print(f'O(a) {player.nome} morreu de fome.')
        sair = True

    if player.saude <= 0:
        print("\nSaúde 0")
        print(f'O(a) {player.nome} morreu!')
        sair = True

    if player.tedio >= 100:
        print("\ntedio 100%")
        print(f'O(a) {player.nome} ficou muito entediado e foi embora.')
        sair = True

    return player, sair


def jogada(player):
    sair = False
    print('------------------')
    print('(1) Alimentar')
    print('(2) Dar remédio')
    print('(3) Brincar')
    print('(4) Sair')
    print("(Enter) Atualizar Status")
    selec = input("=== ")

    if selec == '1':
        alimentar(player)
    elif selec == '2':
        medicar(player)
    elif selec == '3':
        brincar(player)
    elif selec == "4":
        print("Saindo...")

        sair = True

    return player, sair
