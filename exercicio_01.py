'''
Exercicios 01 - Crie uma classe chamada ContaBancaria com os seguintes atribos e métodos: Aributo privado "saldo" iniciado em zero.
Métodos depositar, sacar e mostrar_saldo.
Você deve pedir para o usuario efetuar o depósito, saque e mostrar o saldo posteriormente. 
'''
class ContaBancaria:
    def __init__(self):
        self.__saldo = 0

    def depositar(self, valorDeposito):
        if valorDeposito > 0:
            self.__saldo = self.__saldo + valorDeposito
            #self.__saldo += valorDeposito #forma abreviada   
            print(f"Depósito de R$ {valorDeposito:.2f} realizado! \n")
        else:
            print("Valores negativos não são permitidos!")

    def sacar(self, valorSacado):
            if valorSacado > 0:
                if valorSacado <= self.__saldo:
                    self.__saldo = self.__saldo - valorSacado
                    #self.__saldo -= __saldo
                    print(f"Saque de R$ {valorSacado: .2f} realizado com suceso!")
                else:
                    print("Saldo insuficiente para saque")
            else:
                print("O valor do saque deve ser positivo")    

    def mostrar_saldo(self):
        print(f"saldo atual R$ {self.__saldo: .2f}")

#Criar intância para alimentar a classe
conta = ContaBancaria()

valor_depositado = float(input("Informe o valor do deposito R$ "))
conta.depositar(valor_depositado)

sacar = float(input("Informe o valor do saque R$ "))
conta.sacar(sacar)

conta.mostrar_saldo()

