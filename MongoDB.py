from pymongo import MongoClient
class DB:
    def __init__(self,db_name:str):
        self.CONNECTION_STRING =f"mongodb://0.0.0.0:27017/{db_name}"
        self.client = MongoClient(self.CONNECTION_STRING)
        self.db=self.client[db_name]

    def get_database(self): return self.client

    def get_table(self,tableName:str):return self.db[tableName]


