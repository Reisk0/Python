class Libro: 
    def __init__(self, titulo, autor, estado):
        self.titulo = titulo
        self.autor = autor
        self.estado = estado

    def info_libro(self): 
        print(f"Titulo: {self.titulo}|| Autor: {self.autor} || Estado: {self.estado}")

    def prestar(self):
        if self.estado.lower() == "disponible":
            self.estado = "Prestado"
            print(f"El libro '{self.titulo}' ahora está prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible para prestar.")
    def devolver(self): 
        if self.estado.lower() == "prestado": 
            self.estado = "Devuelto"
            print(f"El libro {self.titulo} ha sido devuelto.")
        else: 
            print(f"El libro {self.titulo} aun no ha sido devuelto.")

class Dorian_Gray(Libro):
    def __init__(self, titulo, autor, estado):
        super().__init__(titulo, autor, estado)


libro_biblioteca = Dorian_Gray("El_Retrato_de_Doria_Gray", "Oscar Wilde", "Disponible")

libro_biblioteca.info_libro()  # Estado inicial
libro_biblioteca.prestar()     # Cambia estado a "Prestado"
libro_biblioteca.info_libro()  # Estado actualizado
libro_biblioteca.devolver()
libro_biblioteca.info_libro()