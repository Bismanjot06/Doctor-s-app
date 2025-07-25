'''
MongoDBHelper
database contains colllesctions
and collection contains documents

document:dictionary

user


1. referential technique

collection1:user
    {
        'id':23
        'name':'Hari'
        etc
    }
   
collection2:address 
    {
        'id':'25kf1'
        'adresline':'city'
        etc
        
        
    }  
    loose coupling: User and ddress are 
    saved differently and they have reference saved inside them
    
2. Containerized technique
   tightly coupled 

'''

'''
1. create connection
2.  select the database and the collection
3. create write function (insert, delete, update)
    mongoDB: insert_one(), delete_one, update_one()
4. create read function (retrive/fetch)
    mongoDB: find()
    
    their can be query to delete, update as well find
'''

from pymongo.mongo_client import MongoClient

class mongoDBhelper:
    
    def __init__(self):
        
        # Create a new client and connect to the server
        self.client = MongoClient("mongodb+srv://user:user@cluster0.u3tdbuv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        print('1. [MongoDB]Connection Created :)')

    def select_db(self, db_name='Auribises', collection='users'):
        self.db = self.client[db_name]
        self.collection = self.db[collection]
        print('[MongoDBHelper] DB {} collection{} selected'.format(db_name,collection))

        
    def insert(self, document):
        result = self.collection.insert_one(document)   
        print('[MongoDBHelper] document inserted in collection {}'.format(self.collection.name))
        return result
    
    
    def delete(self, query):
        result = self.collection.insert_one(query)   
        print('[MongoDBHelper] document deleted from collection {}'.format(self.collection.name))
        return result
    
    def update(self, query, document):
        result = self.collection.update_one(query, {'set':document})   
        print('[MongoDBHelper] document [updated] in collection {}'.format(self.collection.name))
        return result
    
    def fetch(self, query=''):
        documents = self.collection.find(query)
        return list(documents)