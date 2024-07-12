class Funcion:
        
    def __init__(self,pelicula, sala, horario):
        self.pelicula = pelicula
        self.sala = sala
        self.horario = horario
        self.started = False
        self.finished = False

        
    def info(self):
        print(f"Pelicula: {self.pelicula.nombre}, Sala: {self.sala.nombre}, Tipo: {self.sala.tipo}, Horario: {self.horario}")
    
    def ocuparAsiento(self, lugar):
        self.sala.asientos[lugar].ocupado = True
        
    def iniciarFuncion(self):
        self.started = True
        
    def finalizarFuncion(self):
        self.finished = True