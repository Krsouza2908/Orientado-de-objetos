class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome#Aributo: Armazena o nome
        self.sobrenome = sobrenome#Aributo: Armazena o sobrenome
        
p1 = Pessoa("guilherme", "Pesente")
p2 = Pessoa("tayor", "laignier")

print(f"O nome é {p1.nome} e o sobrenome é {p1.sobrenome}")