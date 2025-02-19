#Métodos m instâncias de classe em Python
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f"{self.nome} está acelerando.")
            
    def parar(self):
        print(f"{self.nome} está parando.")   

fusca = Carro("Fusca")
print(fusca.nome)
fusca.acelerar()
fusca.parar()         