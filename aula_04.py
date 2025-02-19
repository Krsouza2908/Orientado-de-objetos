class Pessoa: #classe criada
    #tudo o que vai dentro da classe são aributos
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
nome1 = input("Informe eu nome: ")
sobrenome1 = input("Informe seu sobrenome: ")

nome2 = input("Informe eu nome: ")
sobrenome2 = input("Informe seu sobreome: ")

p1 = Pessoa(nome1, sobrenome1)
p2 = Pessoa(nome2, sobrenome2)

print("Dados cadastraos")
print(f"Pessoa 1: {p1.nome} {p1.sobrenome}")
print(f"Pessoa 1: {p2.nome} {p2.sobrenome}")
