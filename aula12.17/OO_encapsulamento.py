# public, protected, private

class BaseDeDados:
    def __init__(self):#metodos
        self.dados = {}

    def inserir_cliente(self, id, nome):#metodos/atributos
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})
bd = BaseDeDados()
bd.inserir_cliente(1, 'weslley')
bd.inserir_cliente(2, 'joão')
bd.inserir_cliente(3, 'manel')
print(bd.dados)


# metodos são verbos 
# se tem atributos nome, curso, idade etc tem que criar gets e sets 

#estancie =>

#abstração => 
