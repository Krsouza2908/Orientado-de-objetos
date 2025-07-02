'''
Super() é a super classe
Classe Principal 
 --> super class, base class, parent clas
 Clases filhas
  --> sub clas, child class, derived class
'''

class Programa():
    def __init__(self, titulo, descricao, trailer):
        self.titulo = titulo
        self.descricao = descricao
        self.trailer = trailer

    def exibir_descricao(self):
        print(f"Descrição: {self.descricao}")

    def exibir_diretor(self):
        print("Direor: Nolan")

class Serie(Programa):
    def exibir_descricao(self):
        print("Tem 8 episódios")
        super().exibir_descricao()
        super().exibir_diretor()

class Filme(Programa):
    pass

round6 = Serie("Round6", "Série de jogos entre pessoas reais", "trailer_round6.mp4")
#print("round6.descricao")
round6.exibir_descricao()

