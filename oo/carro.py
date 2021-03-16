class Carro:
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0


CIMA = 'CIMA'
DIREITA = 'DIREITA'
BAIXO = 'BAIXO'
ESQUERDA = 'ESQUERDA'


class Direcao:
    rotacao_direita_dicionario = {CIMA: DIREITA, DIREITA: BAIXO, BAIXO: ESQUERDA, ESQUERDA: CIMA}
    rotacao_esquerda_dicionario = {CIMA: ESQUERDA, DIREITA: CIMA, BAIXO: DIREITA, ESQUERDA: BAIXO}

    def __init__(self):
        self.valor = CIMA

    def girar_a_direita(self):
        self.valor = self.rotacao_direita_dicionario[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_esquerda_dicionario[self.valor]


if __name__ == '__main__':
    motor = Motor()
    motor.acelerar()
    motor.acelerar()
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    motor.frear()
    motor.frear()
    print(motor.velocidade)

    print('')

    direcao = Direcao()

    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)

    direcao.girar_a_esquerda()
    print(direcao.valor)

    print('')

    carro = Carro(motor, direcao)
    carro.acelerar()
    print(carro.calcular_velocidade())
    print(carro.calcular_direcao())
    carro.girar_a_esquerda()
    print(carro.calcular_direcao())