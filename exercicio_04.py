'''
Você foi contratado para e senvolver um sistem simples de cadastro de veículos para uma empresa. Essa empresa possui veículos comuns e caminhões. Todos os veículos possuem : Marca e Modelo. Os Caminhões, além disso, possuem: Capaciade de carga(em toneladas). Você deverá criar:

--> Uma superclasse Veículo com os atributos comuns.

--> Uma subclasse Caminhao que herda de Veiculo, adicionando o atributo capacidae_carga. 

--> Um método exibir_dados() em cada classe, sendo que a subclasse deve usar super() para reaproveitar o método da superclase.
'''
class Veiculos:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")


class Caminhao(Veiculos):
    def __init__(self, marca, modelo, capacidade_carga):
        super().__init__(marca, modelo)
        self.capacidade_carga = capacidade_carga

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Capacidade de carga: {self.capacidade_carga}")

marca = input("Diite a Marca: ")
modelo = input("Diite o Modelo: ")
capacidade_carga = float(input("Diite a Capacidade de carga(em toneladas): "))

caminhao1 = Caminhao(marca, modelo, capacidade_carga)

print("\nDados Cadastrados")
caminhao1.mostrar_dados()
