class Biblioteca:
    def __init__(self):
        self.__livros_disponiveis = {}
        self.__livros_emprestados = {}
        self.__proximo_id = 1
       
    def adicionar_livro(self):
        livro = input("Digite o nome do livro que deseja adicionar: ")
        livro_id = self.__proximo_id
        self.__livros_disponiveis[livro_id] = livro
        self.__proximo_id += 1
        print(f'O livro "{livro}" foi adicionado com o ID {livro_id}.\n')
       
    def listar_livros_cadastrados(self):
        print("\nLivros Cadastrados:")
        if self.__livros_disponiveis:
            for livro_id, livro in self.__livros_disponiveis.items():
                print(f"ID: {livro_id} | Livro: {livro}")
        else:
            print("Nenhum livro cadastrado.")
           
    def excluir_livro(self):
        self.listar_livros_cadastrados()
        try:
            livro_id = int(input("Informe o ID do livro a ser excluído: "))
        except ValueError:
            print("ID inválido.")
            return
        
        if livro_id in self.__livros_disponiveis:
            livro_removido = self.__livros_disponiveis.pop(livro_id)
            print(f'O livro "{livro_removido}" foi removido da biblioteca.')
        else:
            print("ID não encontrado. Tente novamente.")
           
    def emprestar_livro(self):
        if not self.__livros_disponiveis:
            print("Nenhum livro disponível.")
            return
        
        usuario = input("Informe seu nome: ")
        self.listar_livros_cadastrados()
        
        try:
            livro_id = int(input("\nDigite o ID do livro que deseja emprestar: "))
        except ValueError:
            print("ID inválido.")
            return
        
        if livro_id in self.__livros_disponiveis:
            livro = self.__livros_disponiveis.pop(livro_id)
            self.__livros_emprestados[livro] = usuario
            print(f'O livro "{livro}" foi emprestado para {usuario}.')
        else:
            print("ID não encontrado.")
    
    def devolver_livro(self):
        if not self.__livros_emprestados:
            print("Nenhum livro emprestado.")
            return
        
        usuario = input("Informe seu nome: ")
        livros_usuario = [livro for livro, u in self.__livros_emprestados.items() if u == usuario]

        if not livros_usuario:
            print("Você não tem livros emprestados.")
            return

        print("\nSeus livros emprestados:")
        for livro in livros_usuario:
            print(f"- {livro}")

        livro = input("\nDigite o nome do livro que deseja devolver: ")

        if livro in livros_usuario:
            self.__livros_disponiveis[self.__proximo_id] = livro
            self.__proximo_id += 1
            del self.__livros_emprestados[livro]
            print(f'O livro "{livro}" foi devolvido com sucesso.')
        else:
            print("Esse livro não está registrado como emprestado por você.")

    def listar_livros(self):
        print("\nLivros disponíveis para empréstimos:")
        if self.__livros_disponiveis:
            for livro_id, livro in self.__livros_disponiveis.items():
                print(f"ID: {livro_id} | Livro: {livro}")
        else:
            print("Nenhum livro disponível para empréstimo.")

biblioteca = Biblioteca()

while True:
    print("\n========== MENU BIBLIOTECA ==========")
    print("1 - Adicionar Livros")
    print("2 - Listar Livros Cadastrados")
    print("3 - Excluir Livro pelo ID")
    print("4 - Devolver Livros")
    print("5 - Emprestar Livro")
    print("6 - Listar Livros Disponíveis")
    print("0 - SAIR")
   
    try:
        opc = int(input("Digite a opção que deseja acessar: "))
    except ValueError:
        print("Opção inválida. Digite um número.")
        continue
   
    if opc == 1:
        biblioteca.adicionar_livro()
    elif opc == 2:
        biblioteca.listar_livros_cadastrados()
    elif opc == 3:
        biblioteca.excluir_livro()
    elif opc == 4:
        biblioteca.devolver_livro()
    elif opc == 5:
        biblioteca.emprestar_livro()
    elif opc == 6:
        biblioteca.listar_livros()
    elif opc == 0:
        print("Sistema encerrando...")
        break
    else:
        print("Número inválido.")