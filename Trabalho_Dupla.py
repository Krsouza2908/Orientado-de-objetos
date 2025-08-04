class Pessoa:
    def __init__(self, nome, idade, cpf, rg, telefone, endereco):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.endereco = endereco
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
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
    def __init__(self, nome, idade, cpf, nf, disciplina):
        super().__init__(nome, idade, cpf,)
        self.nf = nf
        self.disciplina = disciplina

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Número Funcional: {self.nf}")
        print(f"Disciplina: {self.disciplina}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, setor, funcao):
        super().__init__(nome, idade, cpf,)
        self.setor = setor
        self.funcao = funcao

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Setor: {self.setor}")
        print(f"Função: {self.funcao}")       

nomeA = input("Diite seu nome: ")
idadeA = int(input("Diite sua Idade: "))
cpfA = input("Diite o seu CPF: ")
rgA = int(input("Diite seu RG: "))
telefoneA = input("Diite seu telefone: ")
enderecoA = input("Diite seu endereço: ")

pessoa1 = Pessoa(nomeA, idadeA, cpfA, telefoneA, enderecoA )

print("\nDados Cadastrados")
pessoa1.mostrar_dados()
