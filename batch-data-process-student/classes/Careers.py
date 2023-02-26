from classes.DbMongo import DbMongo

from classes.data import DATA


class Careers:
    
    def __init__(self, nombre, id=""):
        self.client, self.db = DbMongo.getDB()
        self.careers = self.db['Careers']
        self.nombre = nombre
        self.__id = id
        self.__collection = "Careers"
    
    def save(self):
        result = self.careers.insert_one(self.__dict__)
        self.__id = result.inserted_id

    def update(self):
        filterToUse = {'_id': self.__id}
        objStore = {'$set': self.__dict__}
        self.careers.update_one(filterToUse, objStore)

    def delete(self):
        filterToUse = {'_id': self.__id}
        self.careers.delete_one(filterToUse)

    @staticmethod
    def get_list():
        careers = Careers.db["Careers"].find()
        list_careers = []
        for career in careers:
            temp_career = Careers(
                career["nombre"],
                career["_id"]
            )
            list_careers.append(temp_career)
        return list_careers

    @staticmethod
    def delete_all():
        lista_careers = Careers.get_list()
        for career in lista_careers:
            career.delete()

    @staticmethod
    def fill_database():
        # delete all previous data
        Careers.delete_all()

        for career_data in DATA:
            career = Careers(career_data["nombre"])
            career.save()
