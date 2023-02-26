import pymongo
from classes import Students,Careers,Courses,Enrollments, DbMongo
from classes.data import DATA
class Dataprocess:

    def __init__(self, data):
        self.__data = data

    def create_careers(self,data,db):
        careers_collection = db["careers"]
        careers = self.__data["careers"]
        result = careers_collection.insert_many(careers)


        #careers_collection = self.db["careers"]
        #careers = self.__data["careers"]
        #result = careers_collection.insert_many(careers)
        ## Do something to create careers on your mongodb collection using __data
        return True
    def create_courses(self):
        #courses_collection = self.db["careers"]
        #courses = self.__data["courses"]
        #result = courses_collection.insert_many(courses)
        ## Do something to create courses on your mongodb collection using __data
        return True
    def create_students(self,db):
        #if "students" not in db.list_collection_names():
         #   db.create_collection("students")
        students_collection = db["students"]
        students = self.__data["students"]
        result = students_collection.insert_many(students)
        ## Do something to create students on your mongodb collection using __data
        
        return True
    def create_enrollments(self):
        #enrollments_collection = self.db["enrollments"]
        #enrollments = self.__data["enrollments"]
        #result = enrollments_collection.insert_many(enrollments)
        ## Do something to create enrollments on your mongodb collection using __data
        return True
    