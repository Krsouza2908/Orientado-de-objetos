class Pessoa:
    def __init__(self, nome, idade, cpf, rg, telefone, endereco):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.endereco = endereco
    
    def mostrar_dados(self):
        print(f"\nNome cadastrado: {self.nome}")
        print(f"Idade cadastrada: {self.idade}")
        print(f"CPF cadastrado: {self.cpf}")
        print(f"RG cadastrado: {self.rg}")
        print(f"Telefone cadastrado: {self.telefone}")
        print(f"Endereço cadastrado: {self.endereco}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, rg, telefone, endereco, curso, ra):
        super().__init__(nome, idade, cpf, rg, telefone, endereco)
        self.ra = ra
        self.curso = curso

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Curso cadastrado: {self.curso}")
        print(f"RA cadastrado: {self.ra}")

class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, rg, telefone, endereco, disciplina, numero_funcional):
        super().__init__(nome, idade, cpf, rg, telefone, endereco)
        self.numero_funcional = numero_funcional
        self.disciplina = disciplina

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Disciplina cadastrada: {self.disciplina}")
        print(f"Número funcional cadastrado: {self.numero_funcional}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, rg, telefone, endereco, funcao, setor):
        super().__init__(nome, idade, cpf, rg, telefone, endereco)
        self.setor = setor
        self.funcao = funcao

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Função cadastrada: {self.funcao}")
        print(f"Setor cadastrado: {self.setor}")

# Cadastro do aluno
print("------------ Cadastro do Aluno ------------")
nomeA = input("Informe seu nome: ")
idadeA = int(input("Informe sua idade: "))
cpfA = input("Informe seu CPF: ")
rgA = input("Informe seu RG: ")
telefoneA = input("Informe seu telefone: ")
enderecoA = input("Informe seu endereço: ")
cursoA = input("Informe seu curso: ")
raA = input("Informe seu RA: ")

aluno = Aluno(nomeA, idadeA, cpfA, rgA, telefoneA, enderecoA, cursoA, raA)

# Cadastro do professor
print("\n------------ Cadastro do Professor ------------")
nomeP = input("Informe seu nome: ")
idadeP = int(input("Informe sua idade: "))
cpfP = input("Informe seu CPF: ")
rgP = input("Informe seu RG: ")
telefoneP = input("Informe seu telefone: ")
enderecoP = input("Informe seu endereço: ")
disciplinaP = input("Informe sua disciplina: ")
numeroFuncionalP = input("Informe seu número funcional: ")

professor = Professor(nomeP, idadeP, cpfP, rgP, telefoneP, enderecoP, disciplinaP, numeroFuncionalP)

# Cadastro do funcionário
print("\n------------ Cadastro do Funcionário ------------")
nomeF = input("Informe seu nome: ")
idadeF = int(input("Informe sua idade: "))
cpfF = input("Informe seu CPF: ")
rgF = input("Informe seu RG: ")
telefoneF = input("Informe seu telefone: ")
enderecoF = input("Informe seu endereço: ")
funcaoF = input("Informe sua função: ")
setorF = input("Informe seu setor: ")

funcionario = Funcionario(nomeF, idadeF, cpfF, rgF, telefoneF, enderecoF, funcaoF, setorF)


print("\n------------ DADOS CADASTRADOS ------------")

print("\n--- Dados do Aluno ---")
aluno.mostrar_dados()

print("\n--- Dados do Professor ---")
professor.mostrar_dados()

print("\n--- Dados do Funcionário ---")
funcionario.mostrar_dados()
