from classes.DbMongo import DbMongo

class Courses:

    def __init__(self,nombre,cursos_aprobados, cursos_reprobados, id=""):
        self.nombre = nombre
        self.cursos_aprobados = cursos_aprobados
        self.cursos_reprobados = cursos_reprobados
        self.__id = id
        self.__collection = "courses"
    
    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

    def update(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )

    #def delete(self, db):
     #   collection = db[self.__collection]
      #  filterToUse = { '_id' : self.__id }
       # collection.delete_one( filterToUse )

    @staticmethod
    def get_list(db):
        collection = db["courses"]
        cursos = collection.find()

        list_cursos = []
        for e in cursos:
            temp_courses = Courses(
                e["nombre"]
                , e["cursos_aprobados"]
                , e["cursos_reprobados"]
                , e["_id"] 
            )

            list_cursos.append(temp_courses)
        return list_cursos
    
    @staticmethod
    def delete_all(db):
        lista_e = Courses.get_list(db)
        for e in lista_e:
            e.delete(db)