class Libro():
    id = ''
    titulo = ''
    genero = ''
    isbn = ''
    editorial = ''
    autor = ''

    def __init__(self, id, titulo, genero, isbn, editorial, autor):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.isb = isbn
        self.editorial = editorial
        self.autor = autor

    def getId(self):
        return self.id

    def setId(self):
        self.id = id

    def getTitulo(self):
        return self.titulo

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero

    def getIsbn(self):
        return self.isbn

    def setIsbn(self, isbn):
        self.isb = isbn

    def getEditorial(self):
        return self.editorial

    def setEditorial(self, editorial):
        self.editorial = editorial

    def getAutor(self):
        return self.autor

    def setAutor(self, autor):
        self.autor = autor


    # Implementar metodos aqui

    # 1| Leer archivo de disco duro
    # 2| Listar libros
    # 3| Agregar libro

    # 4| Eliminar libro
    # 5| Buscar libro
    # 6| Ordenar libros por título

    # 7| Buscar libros por autor, editorial o género
    # 8| Buscar libros por número de autores
    # 9| Editar o actualizar datos de un libro

    # 10| Guardar libros en archivo de disco duro
