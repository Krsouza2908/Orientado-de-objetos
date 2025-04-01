'''Exercício 03- Sistema de biblioteca com atributos privadas
(-__livros_disponiveis e __livros_emprestados), e os seguintes métodos:
adicionarLviros, emprestarLivro, devolverLivro e listarLivro().'''

class Biblioteca:
    def __init__(self):
        #Lista privada para armazenar os livros disponíveis
        self.__livros_disponiveis = []
        #Lista para armazenar os livros emprestados e os usários responsáveis
        self.__livros_emprestados = {}

    def adicionarLivro(self):
            #solicita ao usuário o aramazenamento de um livro
            livro = input("Digite o nome do Livro que deseja aicionar: ")
            self.__livros_disponiveis.append(livro)
            print(f'O livro "{livro}" foi cadatrado com sucesso!\n')

    def emprestarLivro(self):
        livro = input("Digite o nome do Livro que deseja emprestar: ")
        if livro in self.__livros_disponiveis:
            usuario = input("Informe o nome de Usuário")
            self.__livros_disponiveis.remove(livro)
            self.__livros_emprestados[livro] = usuario
            print(f'O livro "{livro}" foi emprestado para {usuario}.\n')
        else:
            print(f'O livro "{livro}" não está disponível para empréstimo.\n')


    def devolverLivro(self):
        livro = input("Digite o nome do Livro que deseja devolver: ")
        if livro in self.__livros_emprestados:
            usuario = self.__livros_emprestados.pop(livro)
            self.__livros_disponiveis.append(livro)
            print(f'O livro "{livro}" foi devolvido por {usuario}\n')
        else:
            print(f'O livro "{livro}" não está registrado como emprestado\n')

    def listarLivro(self):
        #Exibir todos os livros disponíveis/cadastrados
        if self.__livros_disponiveis:
            print("Livros diponíveis para empréstimos")
            for livro in self.__livros_disponiveis:
                print(f"-{livro}")
        else:
            print("Nenhum livro disponível no momento.\n")

biblioteca = Biblioteca()

while True:
    print("MENU BIBLIOTECA")
    print("1 - Adicionar Livro")
    print("2 - Emprestar Livro")
    print("3 - Devolver Livro")
    print("4 - Listar Livros Diponíveis")
    print("5 - Sair")

    opc = input("Escolha uma opção: ")

    if opc == "1":
        biblioteca.adicionarLivro()
    elif opc == "2":
        biblioteca.emprestarLivro()
    elif opc == "3":
        biblioteca.devolverLivro()
    elif opc == "4":
        biblioteca.listarLivro()
    elif opc == "5":
        print("aindo do sistema...")
    else:
        print("Opção inválida! Tente novamente.")

