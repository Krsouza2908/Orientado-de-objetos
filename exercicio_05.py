'''
Você está criando um sistema simples de cadastro de pessoas em uma escola. 
Existem dois tipos principais:
Pessoa: contém informações basicas de qualquer individuo: Nome, Idade.  
Professor: Herda de Pessoa, mas também possui: Disciplina lecionada.   
'''

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")


class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, disciplina_lecionada):
        super().__init__(nome, idade, cpf,)
        self.disciplina_lecionada = disciplina_lecionada

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Disciplina lecionada: {self.disciplina_lecionada}")


nome = input("Diite o nome: ")
idade = input("Diite sua Idade: ")
cpf = input("Diite o seu CPF: ")
disciplina_lecionada = input("Diite a Disciplina lecionada: ")

professor1 = Professor(nome, idade, cpf, disciplina_lecionada)

print("\nDados Cadastrados")
professor1.mostrar_dados()
