import pymongo
#import certifi
import os


class DbMongo:
    
    @staticmethod
    def getDB():
        user = os.environ['USER']
        password = os.environ['PASSWORD']
        cluster = os.environ['CLUSTER']
        query_string = 'retryWrites=true&w=majority'


        ## Connection String
        uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
            user
            , password
            , cluster
            , query_string
        )
        

        print(uri)

        #ca=certifi.where()
        #client = pymongo.MongoClient("mongodb+srv://MAFE:<password>@cluster0.er1gsoz.mongodb.net/?retryWrites=true&w=majority")
        #db = client[os.environ['DB']]
        client = pymongo.MongoClient(uri)
        db = client[os.environ['DB']]

        return client, db