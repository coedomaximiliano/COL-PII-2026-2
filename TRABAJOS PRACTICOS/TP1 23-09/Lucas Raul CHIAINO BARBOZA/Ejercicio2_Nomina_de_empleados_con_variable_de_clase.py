#Ejercicio 2: Nómina de Empleados con Variable de Clase

#Clase base para todos los empleados
class Empleado:
    #Variable de clase: se compartira entre todos los empleados
    cantidad_empleados = 0

    def __init__(self, nombre, sueldo_base):
        #Varobles de instancia: se crean para cada empleado
        self.nombre = nombre
        self.sueldo_base = sueldo_base

        #Atributo privado para guardar el ultimo sueldo calculado
        self.__ultimo_sueldo = 0

        #Incrementamos la variable de clase cada vez que se crea un nuevo empleado
        Empleado.cantidad_empleados += 1

    #Metodo que devuelve la cantidad total de empleados creados
    @classmethod
    def total_empleados(cls):
        return cls.cantidad_empleados

    #Metodo para calcular el sueldo del empleado
    @property
    def ultimo_sueldo(self):
        return self.__ultimo_sueldo 

    #Cada subbclase implementara su propio metodo calcular_sueldo() que actualizara el atributo privado __ultimo_sueldo
    def calcular_sueldo(self):
        raise NotImplementedError("El método calcular_sueldo() debe ser implementado por cada subclase")    



#Subclase Vendedor
class Vendedor(Empleado):
    def calcular_sueldo(self):
        sueldo = self.sueldo_base * 1.10 #El vendedor cobra un 10% mas que el sueldo base  
        self.__ultimo_sueldo = sueldo #Se guarda el resultado en el atributo privado
        return sueldo


#Subclase Gerente
class Gerente(Empleado):
    def calcular_sueldo(self):
        sueldo = self.sueldo_base * 1.25 #El gerente cobra un 25% mas que el sueldo base
        self.__ultimo_sueldo = sueldo #Se guarda el resultado en el atributo privado    
        return sueldo



#Creo un objeto de cada subclase
vendedor1 = Vendedor("Lucas", 1500000)
gerente1 = Gerente("Florencia", 2500000)

#Guardo los empleados en una lista
empleados = [vendedor1, gerente1]

#Uso el mismo metodo para todos los empleados, cada subclase calcula el sueldo de forma distinta
for empleado in empleados:
    empleado.calcular_sueldo()

    print (f"Nombre: {empleado.nombre}")
    print (f"Ultimo sueldo calculado: {empleado.ultimo_sueldo}")
    print ("-----------------------------")

#Muestro el total usando el classmethod

print(f"Total de empleados creados: {Empleado.total_empleados()}")