class Empleado():
    def __init__(self,Nombre, SueldoBase):
         self.Nombre = Nombre 
         self.SueldoBase = SueldoBase
    def calcular_sueldo(self):
            print(f"tu sueldo es de {self.SueldoBase}")

class Gerente(Empleado):
    def __init__(self, Nombre, SueldoBase, BonoGerente):
            super().__init__(Nombre, SueldoBase)
            self.BonoGerente = BonoGerente 
    def calcular_sueldo(self):
           self.SueldoBase += self.BonoGerente 
           print(f"el sueldo de gerente es de:{self.SueldoBase}")


Empleado1 = Empleado("riki", 90000) 
Gerente1 = Gerente("soco", 90000, 15000)
Empleado1.calcular_sueldo()
Gerente1.calcular_sueldo()
