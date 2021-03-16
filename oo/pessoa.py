class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.filhos = list(filhos)
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá, " {id(self)} "'


if __name__ == '__main__':
    nicolas = Pessoa(nome='Nicolas')
    elton = Pessoa(nicolas, nome='Elton')
    print(Pessoa.cumprimentar(elton))
    print(id(elton))
    print(elton.cumprimentar())

    print(elton.nome, elton.idade)
    # print(elton.filhos)
    for filho in elton.filhos:
        print(filho.nome)

    elton.sobrenome = 'Castor'
    del elton.filhos

    nicolas.olhos = 1
    del nicolas.olhos
    print(elton.__dict__)
    print(nicolas.__dict__)
    Pessoa.olhos = 3
    print(nicolas.olhos)
