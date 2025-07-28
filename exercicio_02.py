class Veiculo:
    def __init__(self, marca):
        self.marca = marca

    def ligar(self):
        print(f"A moto da marca {self.marca} está ligada")

    def desligar(self):    
        print(f"A moto da marca {self.marca} está desligada")

class Moto(Veiculo):
    def empinar(self):
        print(f"A moto da marca {self.marca} está empinando")


marca = input("Informe a marca da moto: ")

moto1 = Moto(marca)


while True:
    print("\nO que você deseja fazeer? ")
    print("1 - Ligar a moto")
    print("2 - Empinar a moto")
    print("3 - Desligar a moto")
    print("4 - Sair")
    opc = int(input("Escolha uma opção: "))

    if opc == 1:
        moto1.ligar()
    elif opc == 2:
        moto1.empinar()
    elif opc == 3:
        moto1.desligar()
    elif opc == 4:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")

        