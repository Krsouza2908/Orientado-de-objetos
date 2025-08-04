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
    def __init__(self, nome, idade, cpf, rg, telefone, endereco, nf, disciplina):
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
nomeA = input("Digite seu nome: ")
idadeA = int(input("Digite sua idade: "))
cpfA = input("Digite o seu CPF: ")
rgA = input("Digite seu RG: ")
telefoneA = input("Digite seu telefone: ")
enderecoA = input("Digite seu endereço: ")
raA = input("Digite seu RA: ")
cursoA = input("Digite seu curso: ")
pessoa1 = Aluno(nomeA, idadeA, cpfA, rgA, telefoneA, enderecoA, raA, cursoA)


print("\n------------Cadastro de Professor------------")
nomeP = input("Digite seu nome: ")
idadeP = int(input("Digite sua idade: "))
cpfP = input("Digite o seu CPF: ")
rgP = input("Digite seu RG: ")
telefoneP = input("Digite seu telefone: ")
enderecoP = input("Digite seu endereço: ")
nfP = int(input("Digite seu número funcional: "))
disciplinaP = input("Digite sua disciplina: ")
pessoa2 = Professor(nomeP, idadeP, cpfP, rgP, telefoneP, enderecoP, nfP, disciplinaP)


print("\n------------Cadastro de Funcionário------------")
nomeF = input("Digite seu nome: ")
idadeF = int(input("Digite sua idade: "))
cpfF = input("Digite o seu CPF: ")
rgF = input("Digite seu RG: ")
telefoneF = input("Digite seu telefone: ")
enderecoF = input("Digite seu endereço: ")
setorF = input("Digite seu setor: ")
funcaoF = input("Digite sua função: ")
pessoa3 = Funcionario(nomeF, idadeF, cpfF, rgF, telefoneF, enderecoF, setorF, funcaoF)


print("\n------------Dados Cadastrados------------")

print("\n===== DADOS DO ALUNO =====")
pessoa1.mostrar_dados()

print("\n===== DADOS DO PROFESSOR =====")
pessoa2.mostrar_dados()

print("\n===== DADOS DO FUNCIONÁRIO =====")
pessoa3.mostrar_dados()
