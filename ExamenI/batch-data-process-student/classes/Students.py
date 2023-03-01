from classes.DbMongo import DbMongo

class Students:

    def __init__(self, nombre_completo, numero_cuenta, edad, id=""):
        self.nombre_completo = nombre_completo
        self.numero_cuenta = numero_cuenta
        self.edad = edad
        self.__id = id
        self.__collection = "students"

    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

    def update(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )

    @staticmethod
    def get_list(db):
        collection = db["students"]
        estudiante = collection.find()

        list_estudiante = []
        for e in estudiante:
            temp_students = Students(
                e["nombre_completo"]
                , e["numero_cuenta"]
                , e["edad"]
                , e["_id"] 
            )

            list_estudiante.append(temp_students)
        return list_estudiante
    
    @staticmethod
    def delete_all(db):
        lista_e = Students.get_list(db)
        for e in lista_e:
            e.delete(db)