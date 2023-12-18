class FoneDeOuvido:
    def get_volume(self): 
        print('Entrei no GET')
        return self.__volume
    
    def set_volume(self, novo_volume):
        print('Entrei no SET  com volume de 200')
        self.__volume = novo_volume
    
    volume = property(get_volume, set_volume)

# sempre que usar o property o atributo tem que estar privado "__" por que ele nao aceita publico

#INSTANCIAS
fone = FoneDeOuvido()

fone.volume = 200 # SET

print(fone.volume) # GET