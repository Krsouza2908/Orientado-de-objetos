#Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando = False): #Filmando está "desligado"
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self): #Ação do atributo filmando
        if self.filmando: #parte 2 codigo
            print(f"{self.nome} já está filmando")#parte 2 código
            return#parte 2 código
        
        print(f"{self.nome} está filmando")
        self.filmando = True

    def parar_filmar(self): #Ação do atributo filmando  
        if not self.filmando: #parte 3 código
            print(f"{self.nome} não está filmando") #parte 3 código
            return #parte 3 código
        
        print(f"{self.nome} está parando de filmar")
        self.filmando = False

    def fotografar(self):
        if self.filmando:#parte 3 código
            print(f"{self.nome} não pode fotografar filmando")#parte 3 código
            return#parte 3 código
        
        print(f"{self.nome} está fotografando")

c1 = Camera("Canon")
c2 = Camera("Sony")

c1.filmar()
c1.filmar()#parte 2 código
c1.fotografar()#parte 3 código
c1.parar_filmar()#parte 3 código
c1.fotografar()#parte 3 código

print()
c2.filmar()
c2.filmar()#parte 2 código
c2.fotografar()#parte 3 código
c2.parar_filmar()#parte 3 código
c2.fotografar()#parte 3 código

print(c1.filmando)
print(c2.filmando)
