class Carro:
    def __init__(self, marca, cilindrada, kilometraje):
        self.marca = marca
        self.cilindrada = cilindrada
        self.kilometraje = kilometraje
        
    def encender(self):
        print('brum brum')
    
    def _iniciar_motor(self):
        print('Iniciano el motor.....')

ty = Carro("Subaru", 1500, 20000)
ty.encender()

ty2 = Carro('Toyota', 2000, 40000)
ty2.encender()

print(f"Marca carro1: {ty.marca}")
print(f"Marca carro2: {ty2.marca}")