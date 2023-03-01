import pymongo
from classes import DATA, Dataprocess, Students, Careers, Courses, Enrollments, DbMongo, data
from dotenv import load_dotenv
from classes.Careers import Careers
from classes.Courses import Courses
from classes.Enrollments import Enrollments
from classes.Students import Students
from classes.DbMongo import DbMongo
from classes.data import DATA
from classes.Careers import Careers

#def main():

 #   client,db = DbMongo.getDB()
#    pipeline = Dataprocess(DATA)
    

    
    #pipeline.create_careers(db)
    
    #pipeline.create_courses(db)

  #  pipeline.create_students( db)
   # db.students.drop()
    #students = []
    #for students_data in pipeline.data["students"]:
     #   students = {
      #    "numero_cuenta":students_data["numero_cuenta"],
       #   "nombre_completo": students_data["nombre_completo"],
        #   "edad" : students_data["edad"],
         #   "enrollments":[]
            
       # }
        #students.append(students)
   # db.students.insert_many(students)
    #Students.get_list(db)

    #estudiante= Students("Maria Ocon","20191004549","22")
    #Students.delete_all(db)
    #client.close()

    #pipeline.create_enrollments(db)
    #print(DATA[0])

    #return True
def main():
    # Conectarse a la base de datos
    client, db = DbMongo.getDB()

    # Eliminar todos los registros previos en la colección Careers
    Careers.delete_all()

    # Agregar las carreras a la base de datos
    for carrera_data in DATA:
        carrera = Careers(carrera_data["nombre"])
        carrera.save()

    # Obtener la lista de carreras
    lista_carreras = Careers.get_list()

    

if __name__ == '__main__':
    main()
    load_dotenv()
    