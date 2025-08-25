class Pessoa():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome(self):
        print(self.nome, self.sobrenome, self.__class__.__name__) 

class Cliente(Pessoa):
    pass

class Aluno(Pessoa):
    pass

c1 = Cliente("Kauã", "Rosa")
c1.falar_nome()  

a1 = Aluno("Vitor", "Alochio")
a1.falar_nome()  
