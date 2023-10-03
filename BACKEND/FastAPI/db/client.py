from pymongo import MongoClient

#BBDD local
#db_client = MongoClient().local # si es vacio es localhost

#BBBDD remota 
db_client = MongoClient("mongodb+srv://test:test@cluster0.hp9vrad.mongodb.net/?retryWrites=true&w=majority").test