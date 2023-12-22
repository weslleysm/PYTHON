"""
Questão 03

• Faça a abstração de superclasse Fabrica de Rações. 

Obs: você deve ter um str mostrando cada status da fabrica

-------------------------
|    FabricaDeRacoes    |
-------------------------

"""
class FabricaDeRacoes:
    def __init__(self,funcionario):
        self.funcionario = funcionario
        self.producao = False
        self.empacotamento = False

    def inicio_producao(self,):
        if self.empacotamento:
            print(f'nao pode empacotar')
            return
        if self.producao:
            print(f'já estou na produção')
            return
        print(f'{self.funcionario} está na produção de raçoes')
        self.producao = True
    
    def fim_producao(self):
        if not self.producao:
            print(f'ja saiu da produção')
            return
        print(f'{self.funcionario} saiu da produção')
        self.producao = False

    def inicio_empacotamento(self):
        if self.empacotamento:
            print(f'ja estar no empacotamento')
            return
        if self.producao:
            print(f'não posso ir para o empacotamento, pois estou na produção')
            return
        print(f'{self.funcionario} ja está no empacotamento da ração')
        self.empacotamento = True
    
    def fim_empacotamento(self):
        if not self.producao:
            print(f'estar na produção')
            return
        print(f'{self.funcionario} entrou na produção')
        self.producao = False
        self.empacotamento = False

    
p1 = FabricaDeRacoes('weslley')

p1.inicio_producao() #mandei iniciar a produção da ração
p1.inicio_producao()# mandei novamente e ele vai me dizer que ja estar produzindo
p1.fim_producao() # mandei finalizar a produção
p1.fim_producao()#mandei novamente ele finalizar, e ele vai dizer que ja saiu da prodição

p1.inicio_producao() #mandei iniciar a produção da ração
p1.inicio_empacotamento()# mandei ele ir para a 

