#Herança simples
class Jogador(): #Super classe/Classe mãe
    def __init__(self, altura, velocidade, passe, dible, precicao):
        self.altura = altura
        self.velocidade = velocidade
        self.passe = passe
        self.dible = dible
        self.precicao = precicao

    def passar(self):
        print("Mirar")
        print("Encostar na bola com a força de passe do jogador. ")

    def chutar(self):
        print("Mirar")
        print("Encostar na bola com 2x a força de passe do jogador. ")

class Jogador_Goleiro(Jogador):
    def agarrar(self):
        print("Pular")
        print("Se esticar para pegar a bola")
           
class Jogador_Linha(Jogador_Goleiro):
    pass

jogador1 = Jogador_Goleiro(180, 60, 80, 20, 60)
jogador2 = Jogador_Linha(174, 90, 80, 85, 80)

jogador1.passar()
jogador2.passar()
jogador1.agarrar()
jogador2.agarrar()

print(Jogador_Linha.mro())
