'''
    En este archivo se describe cómo crear e instanciar clases.
'''

#Clase de un protocolo.
class Protocol(object):
    def __init__(self, name, number, description):
        self.name = name
        self.number = number
        self.description = description

    def __str__(self):
        return '%s - (%s) - %s' %(self.name, str(self.number), self.description)
    
    def get_protocol_info(self):
        return self.name, self.description

'''CLASES PARA HERENCIA'''
#Clase contacto.
class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

#Clase vendedor.
class Seller(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone
    
    def order(self, order):
        print('Se enviará el pedido {} a {}'.format(order, self.name))


#Se crea una instancia del objeto Protocol.
protocol_http = Protocol('HTTP', 80, 'Hyper Type Text Protocol')

print(protocol_http.name) #Obtenemos el atributo name.
print(protocol_http.number) #Obtenemos el atributo number.
print(protocol_http.description) #Obtenemos el atributo description.
print(protocol_http) #Obtenemos lo que retorna el método __str__.
print(protocol_http.__class__) #Obtenemos el tipo de clase.
print(protocol_http.get_protocol_info) #Obtenemos lo que retorna la función get_protocol_info.

seller = Seller('Oscar', 'reyesglez_oscar@outlook.com', '55-6543-2198')
seller.order('1411')