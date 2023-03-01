from classes.DbMongo import DbMongo

class Enrollments:

    def __init__(self, students, courses, id=""):
        self.students = students
        self.courses = courses
        self.__id = id
        self.__collections = "enrollments"
    
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
        collection = db["enrollments"]
        inscripciones = collection.find()

        list_inscripciones = []
        for e in inscripciones:
            temp_enrollments = Enrollments(
                e["students"]
                , e["courses"]
                , e["_id"] 
            )

            inscripciones.append(temp_enrollments)
        return list_inscripciones
    
    @staticmethod
    def delete_all(db):
        lista_e = Enrollments.get_list(db)
        for e in lista_e:
            e.delete(db)