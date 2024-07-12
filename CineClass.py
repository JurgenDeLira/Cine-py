class Cine:
    def __init__(self, cine, direccion, funciones):
        self.cine = cine
        self.direccion = direccion
        self.funciones = funciones
        self.open = True

    def info(self):
        print(f"Cine: {self.cine} \nDirección: {self.direccion}")
    
    def mostrarFunciones(self):
        print("\nFunciones disponibles del día de hoy:\n")
        for funcion in self.funciones:
            if not funcion.finished:
                funcion.info()

    def obtenerLugares(self, funcion):
        self.funciones[funcion].pelicula.info()
        for asiento in self.funciones[funcion].sala.asientos:
            estado = "Ocupado" if asiento.ocupado else "Disponible"
            print(f"{asiento.numero}{asiento.fila} Estado: {estado}")