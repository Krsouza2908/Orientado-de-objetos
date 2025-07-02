'''
Crie uma classe chamada Pessoa comos atributos nome e idade, além de um método que exibe eses dados.Depois, 
crie uma classe chamada Aluno que herda da classe 
Pessoa. Essa classe Aluno não terá atributos novos, apenas herdará os atributos e métodos da classe
Pessoa.O programa deve permitir que o usuário informe o nome e a idade de um aluno, e depois exibir esses dados. 
'''
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_nome(self):
        print(f"Nome: {self.nome}")

    def exibir_idade(self):
        print(f"Idade: {self.idade}")

class Aluno(Pessoa):
    pass
    
nome_aluno = input("Informe seu nome: ")    
idade_aluno = int(input("Informe sua idade: ")) 

aluno = Aluno(nome_aluno, idade_aluno)

aluno.exibir_nome()
aluno.exibir_idade()
