class BichinhoEletronico:

    def __init__(self, nome: str, fome: int, saude: int, idade: int, tedio: int):
        self._nome = nome
        self._fome = fome
        self._saude = saude
        self._idade = idade
        self._tedio = tedio

    @property
    def nome(self):
        return self._nome

    @property
    def fome(self):
        return self._fome

    @property
    def saude(self):
        return self._saude

    @property
    def idade(self):
        return self._idade

    @property
    def tedio(self):
        return self._tedio

    # Método nome
    def mudar_nome(self):
        novo_nome = input('Coloque o nome desejado: ')
        self._nome = novo_nome

    # Métodos fome
    def alimentar(self):
        if 30 + self._fome <= 0:
            self._fome = 0
        else:
            self._fome -= 30

    def aum_fome(self, tempo):
        self._fome += tempo

    def red_fome(self, valor):
        if self._fome - valor >= 0:
            self._fome -= valor

        elif self._fome - valor < 0:
            self._fome = 0

    # Métodos saúde
    def medicar(self, valor):
        if self._saude + valor <= 100:
            self._saude += valor
        elif self._saude + valor > 100:
            self._saude = 100

    def reduz_saude(self, tempo):
        self._saude -= tempo

    # Método idade
    def envelhecer(self, tempo):
        if tempo // 2 + self._idade >= 100:
            self._idade = 100
            return f'Lamento o(a) {self._nome} morreu de velhice'
        else:
            self._idade += tempo // 2

    # Método humor
    def humor(self):
        humor = (self._fome + self._saude)/2
        return humor

    # Métodos tédio
    def brincar(self, valor):
        if self._tedio - valor >= 0:
            self._tedio -= valor

        elif self._tedio - valor < 0:
            self._tedio = 0

    def aum_tedio(self, tempo):
        self._tedio += tempo

    def __str__(self):
        return f'nome: {self._nome}\n' \
               f'idade: {self._idade}\n' \
               f'fome: {self._fome}\n' \
               f'saúde: {self._saude}\n' \
               f'tédio: {self._tedio}'

