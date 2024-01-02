class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation_instance = Operation(nombre1=12, nombre2=3)

print("Nombre 1 est", operation_instance.nombre1)
print("Nombre 2 est", operation_instance.nombre2)