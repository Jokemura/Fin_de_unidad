import csv

from tabulate import tabulate

from Colors import *
import pandas as pd

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
    @staticmethod
    def eliminar():
        op= True
        print("----------------------------------------------------------------------")
        print("- Eliminar libros                                                   -")
        print("----------------------------------------------------------------------")
        while op == True:
            entrada = input('Ingrese el nombre Libro a ELIMINIAR 1|si 2|no: ')
        while entrada not in  ('1', '2'):
            entrada = input('Ingrese el nombre Libro a ELIMINIAR 1|si 2|no: ')

        if entrada == '1':
            book= input('Ingrese nombre del Libro: \n')
                
            for k1, v1 in list(Libro.libros.items()):
                
                    if v1['titulo'] == book:
                        del Libro.libros[k1]
                        print('Libro eliminado exitosamente')
                    else:
                        print('Este Libro no esta Listado, Intente nuevamente')
        else:
            op==False

# 5| Buscar libro
    @staticmethod
    def buscar_libro():
        opcion = True
        print("----------------------------------------------------------------------")
        print("- Buscar libros                                                   -")
        print("----------------------------------------------------------------------")
        while opcion == True:
            op = input("Desea Buscar un nuevo libro por 1|Titulo 2|ISBN: ")
            while op not in ('1', '2'):
                op = input("Desea Buscar un nuevo libro por  1|Titulo 2|ISBN: ")


            if op == '1':
                term_search=input('Ingrese el Titulo del Libro: \n')
                libros_filtrados_indexes = []
                try:
                    for i, j in Libro.libros.items():
                        if term_search == j['titulo']:
                            libros_filtrados_indexes.append(i)
                            libros = [Libro.libros[i] for i in libros_filtrados_indexes]
                            print(tabulate(libros, headers="keys", tablefmt="pretty"))                    
                        else:
                            pass
                except:
                    print("An exception occurred")
            elif op == '2':
                term_search2=input('Ingrese el ISBN del Libro: \n')
                isbn_filtrados_indexes = []
                try:
                    for i, j in Libro.libros.items():
                        if term_search2 == j['isbn']:
                            isbn_filtrados_indexes.append(i)
                            isbns = [Libro.libros[i] for i in isbn_filtrados_indexes]
                            print(tabulate(isbns, headers="keys", tablefmt="pretty"))                    
                        else:
                            pass
                except:
                    print('An exception ocurred')
            else:
                opcion = False
# 6| Ordenar libros por título
    def ordenar_titulos():
        for k,v in Libro.libros.items():
            sorted_values = sorted(v.items(), key=lambda x:x[1])
            print()


# 7| Buscar libros por autor, editorial o género
    def buscarLibros(palabra): #Opcion 7
        data = Libro.libros
        list_id = [codigo for codigo in data]
        for codigo in list_id:
            autores = data[codigo]["autor"].split(",")
            if data[codigo]["editorial"] == palabra:
                print(data[codigo]["titulo"])
            elif data[codigo]["genero"] == palabra:
                 print(data[codigo]["titulo"])           
            for autor_buscado in autores:
                if autor_buscado == palabra:
                    print(data[codigo]["titulo"])

# 8| Buscar libros por número de autores
    def numeroAutores(cant_autores): #Opcion 8
        #reader es iterable
        # cont = 0
        data = Libro.libros
        list_id = [codigo for codigo in data]
        for codigo in list_id:
            autores = data[codigo]["autor"].split(",")
            if len(autores) == cant_autores:    
                print(data[codigo]["titulo"])    

# 9| Editar o actualizar datos de un libro
    def actualizarDatos(id: int, item, palabra): #Opcion 9
        if item == "titulo":
            data = pd.read_csv("D:/Silabuz/CondicionalesBucles/01/Fin_de_unidad/Tarea1/Libros.csv")
            data.iat[id-1, 1] = palabra
            data.to_csv("D:/Silabuz/CondicionalesBucles/01/Fin_de_unidad/Tarea1/Libros.csv", index=False)
        elif item == "genero":
            data = pd.read_csv("D:/Silabuz/CondicionalesBucles/01/Fin_de_unidad/Tarea1/Libros.csv")
            data.iat[id-1, 2] = palabra
            data.to_csv("D:/Silabuz/CondicionalesBucles/01/Fin_de_unidad/Tarea1/Libros.csv", index=False)
        elif item == "isbn":
            data = pd.read_csv("D:/Silabuz/CondicionalesBucles/01/Fin_de_unidad/Tarea1/Libros.csv")
            data.iat[id-1, 3] = palabra
            data.to_csv("D:/Silabuz/CondicionalesBucles/01/Fin_de_unidad/Tarea1/Libros.csv", index=False)            
        elif item == "editorial":
            data = pd.read_csv("D:/Silabuz/CondicionalesBucles/01/Fin_de_unidad/Tarea1/Libros.csv")
            data.iat[id-1, 4] = palabra
            data.to_csv("D:/Silabuz/CondicionalesBucles/01/Fin_de_unidad/Tarea1/Libros.csv", index=False)            
        elif item == "autores":
            data = pd.read_csv("D:/Silabuz/CondicionalesBucles/01/Fin_de_unidad/Tarea1/Libros.csv")      
            data.iat[id-1, 5] = palabra
            data.to_csv("D:/Silabuz/CondicionalesBucles/01/Fin_de_unidad/Tarea1/Libros.csv", index=False)

# 10| Guardar libros en archivo de disco duro
    
