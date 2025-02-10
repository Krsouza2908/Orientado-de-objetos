#O que é classe, método, atributo e instância?

#Definição de classe
class Pessoa:# Nome da classe sempre maiúsculo
    #O método __init__ é o CONSTRUTOR da classe.
    #Ele inicializa os atributos do objetivo.
    def __init__(self, nome, idade):
        self.nome = nome #Atributo: Armazena o nome
        self.idade = idade#Atributo: Armazena a idade.
    #Método: Uma ação que o objeto pode executar
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")

#Criandop uma instância (objeto) da classe pessoa
pessoa1 = Pessoa("Kainan", 17)
pessoa2 = Pessoa("marcos", 17)

#Chamando o método apresentar() para cada instância
pessoa1.apresentar()
pessoa2.apresentar()
