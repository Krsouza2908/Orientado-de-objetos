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
            print(f"Depósito de R$ {valorDeposito:.2f} realizado! /n")
        else:
            print("Valores negativos não são permitidos!")

    def sacar(self, valorSacado):
            ...

    def mostrar_saldo(self):
        ...

#Criar intância para akimentar a classe
conta = ContaBancaria()

valor_depositado = float(input("Informe o valor do éposito R$ "))
conta.depositar(valor_depositado)

conta.mostrar_saldo()
sacar = float(input("Informe o valor do saque R$ "))
conta.sacar(sacar)