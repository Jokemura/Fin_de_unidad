import csv

from tabulate import tabulate

from Colors import *


class Libro():
    id = ''
    titulo = ''
    genero = ''
    isbn = ''
    editorial = ''
    autor = ''

    # Diccionario de libros, aqui esta almacenado los libros : Referenciar usando "Libro.libros"
    libros = {}

    # def __init__(self, id):
    #     self.id = id

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

    def getLibros(self):
        return self.libros

    def setLibros(self, libros):
        self.libros = libros

    # Implementar metodos aqui

    # 1| Leer archivo de disco duro
    @staticmethod
    def leerCsv():
        # datos=pd.read_csv('D:/prueba.csv',header=0)
        # print(datos)

        # libros={}
        # with open('D:/prueba.csv') as inp:
        #     reader = csv.reader(inp)
        #     Libros = {rows[0]: rows[1] for rows in reader}
        # print(Libros)

        # print(*csv.DictReader(open('D:/prueba.csv')), sep='\n')

        # Libro.libros = [*csv.DictReader(open('D:/prueba.csv'))]
        try:
            with open('../Tarea1/Libros.csv', 'r') as data_file:
                data = csv.DictReader(data_file, delimiter=",")
                for row in data:
                    item = Libro.libros.get(row['id'],
                                            {'titulo': row['titulo'], 'genero': row['genero'], 'isbn': row['isbn'],
                                             'editorial': row['editorial'], 'autor': row['autor']})
                    Libro.libros[row['id']] = item
            print(GREEN + "--------------------------------------")
            print("- Registros cargados correctamente   -")
            print("--------------------------------------" + RESET)
        except:
            print("An exception occurred")

        # print(*(Libro.libros), sep='\n')
        # print(Libro.libros)

    # 2| Listar libros
    @staticmethod
    def listarlibros():
        print("------------------------------------------------------------------------")
        print("- Libros registrados                                                   -")
        print("------------------------------------------------------------------------")
        headers = ["Codigo", "Titulo", "Genero", "isbn", "Editorial", "Autor"]
        # print(tabulate(Libro.libros, headers="keys", tablefmt="pretty"))

        values = [[name, *inner.values()] for name, inner in Libro.libros.items()]
        print(tabulate(values, headers=headers, tablefmt="pretty"))

        #
        # print(tabulate(values, headers=headers))
        # for p in Libro.libros:
        #     print(p)

        # print(*(Libro.libros), sep='\n')

    # 3| Agregar libro
    @staticmethod
    def agregarLibros():
        opcion = True
        print("----------------------------------------------------------------------")
        print("- Registrar libros                                                   -")
        print("----------------------------------------------------------------------")
        while opcion == True:
            op = input("Desea registrar un nuevo libro  1|si 2|no: ")
            while op not in ('1', '2'):
                op = input("Desea registrar un nuevo libro  1|si 2|no: ")

            if op == '1':
                try:
                    id = input("Id: ")
                    titulo = input("Titulo: ")
                    genero = input("Genero: ")
                    isbn = input("isbn: ")
                    editorial = input("Editorial: ")
                    autor = input("Autor: ")
                    Libro.libros[id] = {'titulo': titulo, 'genero': genero, 'isbn': isbn, 'editorial': editorial,
                                        'autor': autor}
                    print(GREEN + "--------------------------------------")
                    print("- Registro creado correctamente      -")
                    print("--------------------------------------" + RESET)

                except:
                    print("An exception occurred")
            else:
                opcion = False

        # Libro.libros = {
        #     '1': {
        #         'titulo': 'Filosa',
        #         'genero': 'Cuchillos',
        #         'isbn': "2",
        #         'editorial': "2",
        #         'autor': 'fem'
        #     },
        #     '2': {
        #         'titulo': 'Filosa',
        #         'genero': 'Cuchillos',
        #         'isbn': "2",
        #         'editorial': "2",
        #         'autor': 'fem'
        #     }
        # }
        # print(*(Libro.libros), sep='\n')
        # Libro.libros[id] = {'titulo': titulo, 'genero': genero, 'isbn': isbn, 'editorial': editorial,
        #                     'autor': autor}

        # for p in Libro.libros:
        #     print(p, Libro.libros[p])

# 4| Eliminar libro
    

# 5| Buscar libro

# 6| Ordenar libros por título

# 7| Buscar libros por autor, editorial o género
# 8| Buscar libros por número de autores
# 9| Editar o actualizar datos de un libro

# 10| Guardar libros en archivo de disco duro
