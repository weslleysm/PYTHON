#Disercando uma variavel

a = input('Digite algo:')
print('o tipo primitivo desse valor é', type(a))
print('so tem espaços?', a.isspace())
print('É um numero?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumerica?', a.isalnum())
print('Estar em maiusculo', a.isupper())
print('Estar em minusculo', a.islower())
print('Tem apenas numeros?', a.isdigit())