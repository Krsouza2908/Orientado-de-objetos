'''
Herança simples - Você deve desenvolver um sistema que envie notificações de forma genérica, mas que possa ser adaptado a diferentes caanais de envio, como: Email ou Sms.  
'''
class Mensagem:
    def __init__(self, conteudo):
        self.conteudo = conteudo

    def enviar(self):
        print("Mensagem genérica enviada:", self.conteudo)

class Email(Mensagem):
    def enviar(self):
        print("Email enviado:", self.conteudo)

class SMS(Mensagem):
    def enviar(self):
        print("SMS enviado:", self.conteudo)


conteudo = input("Digite a mensagem: ")

while True:
    print("\nQual tipo de mensagem quer enviar?")
    print("1 - Genérico")
    print("2 - SMS")
    print("3 - Email")
    print("4 - Sair")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        mensagem = Mensagem(conteudo)
    elif escolha == 2:
        mensagem = SMS(conteudo)
    elif escolha == 3:
        mensagem = Email(conteudo)
    elif escolha == 4:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")
        continue

    mensagem.enviar()