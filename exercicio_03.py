'''
Você está desenvolvendo um sistema para um departamento de recursos humanos.
Nesse sistema, há dois tipos de pessoas que devem ser cadastradas: Funcionários e Gerentes. Todo
gerente é um funcionário, mas com uma informação a mais: o setor que gerencia.

--> Crie duas classes:
        --> Funcionário: que possui nome e salario
        --> Gerente: que herda de Funcionário e adiciona o atributo setor. 

--> O programa deverá:
        --> Solicitar os dados do funcionário e do gerente via input.
        --> Exibir os dados do gerente utilizando o método da classe Gerente.
        --> Use o super() para reutilizar o método da classe base.
'''

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: {self.salario}")


class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Setor: {self.setor}")


nome = input("Diite o nome: ")
salario = input("Diite o salario: ")
setor = input("Diite o setor: ")

gerente1 = Gerente(nome, salario, setor)

print("\nDados Cadastrados")
gerente1.mostrar_dados()

