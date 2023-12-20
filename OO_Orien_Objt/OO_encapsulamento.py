# public, protected, private

class BaseDeDados:
    def __init__(self):#metodos
        self.dados = {}

    def inserir_cliente(self, id, nome):#metodos/atributos
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})
    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)
    def apagar_clientes(self, id):
        del self.dados['clientes'][id]
bd = BaseDeDados()
bd.inserir_cliente(1, 'weslley')
bd.inserir_cliente(2, 'joão')
bd.inserir_cliente(3, 'manel')
bd.apagar_clientes(2)
bd.lista_clientes()
