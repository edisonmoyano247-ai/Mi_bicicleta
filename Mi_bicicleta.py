class bicicleta:
    def __init__(self, marca, modelo, numero_marchas, color):
        self.marca = marca
        self.modelo = modelo
        self.numero_marchas = numero_marchas
        self.marcha_actual = 0
      
        self.color = color
        
    def cambiar_marcha(self, incremento: int):
        nueva_marcha = self.marcha_actual + incremento

        if 0 < nueva_marcha <= self.numero_marchas:
            self.marcha_actual = nueva_marcha
            print("Marcha cambiada con exito")

        else:
            print("La marcha no fue cambiada")


mi_bicicleta = bicicleta("Cannondale", "Mountain", 20, "Rojo")

mi_bicicleta.cambiar_marcha(1)
    
        

