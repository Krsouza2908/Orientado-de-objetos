class Pessoa:
    def __init__(self, nome, idade, cpf, rg, telefone, endereco):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.endereco = endereco
    
    def mostrar_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
        print(f"RG: {self.rg}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, rg, telefone, endereco, ra, curso):
        super().__init__(nome, idade, cpf, rg, telefone, endereco)
        self.ra = ra
        self.curso = curso

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"RA: {self.ra}")
        print(f"Curso: {self.curso}")

class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, rg, telefone, endereco, numerofuncional, disciplina):
        super().__init__(nome, idade, cpf, rg, telefone, endereco)
        self.nf = nf
        self.disciplina = disciplina

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Número Funcional: {self.nf}")
        print(f"Disciplina: {self.disciplina}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, rg, telefone, endereco, setor, funcao):
        super().__init__(nome, idade, cpf, rg, telefone, endereco)
        self.setor = setor
        self.funcao = funcao

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Setor: {self.setor}")
        print(f"Função: {self.funcao}")


print("------------Cadastro de Aluno------------")
nomeA = input("Informe seu nome: ")
idadeA = int(input("Informe sua idade: "))
cpfA = input("Informe o seu CPF: ")
rgA = input("Informe seu RG: ")
telefoneA = input("Informe seu telefone: ")
enderecoA = input("Digite seu endereço: ")
raA = input("Informe seu RA: ")
cursoA = input("Informe seu curso: ")
pessoa1 = Aluno(nomeA, idadeA, cpfA, rgA, telefoneA, enderecoA, raA, cursoA)


print("\n----------Cadastro de Professor----------")
nomeProfessor = input("Informe seu nome: ")
idadeProfessor = int(input("Informe sua idade: "))
cpfProfessor = input("Informe o seu CPF: ")
rgProfessor = input("Informe seu RG: ")
telefoneProfessor = input("Informe seu telefone: ")
enderecoProfessor = input("Informe seu endereço: ")
numerofuncionalProfessor = int(input("Informe seu número funcional: "))
disciplinaProfessor = input("Informe sua disciplina: ")
    pessoa2 = Professor(nomeProfessor, idadeProfessor, cpfProfessor, numerofuncionalProfessor, telefoneProfessor, enderecoProfessor, numerofuncionalProfessor, disciplinaProfessor)


print("\n------------Cadastro de Funcionário------------")
nomeFuncionario = input("Informe seu nome: ")
idadeFuncionario = int(input("Informe sua idade: "))
cpfFuncionario = input("Informe o seu CPF: ")
rgFuncionario = input("Informe seu RG: ")
telefoneFuncionario = input("Informe seu telefone: ")
enderecoFuncionario = input("Informe seu endereço: ")
setorFuncionario = input("Informe seu setor: ")
funcaoFuncionario = input("Informe sua função: ")
pessoa3 = Funcionario(nomeFuncionario, idadeFuncionario, cpfFuncionario, rgFuncionario, telefoneFuncionario, enderecoFuncionario, setorFuncionario, funcaoFuncionario)


print("\n----------Dados Cadastrados----------")

print("\n------Dados cadastrados do Aluno -----")
pessoa1.mostrar_dados()

print("\n----- Dados cadastrados do Professor -----")
pessoa2.mostrar_dados()

print("\n----- Dados cadastrados do  Funcionário -----")
pessoa3.mostrar_dados()
