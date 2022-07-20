import pymongo
'''client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)'''
client = pymongo.MongoClient("mongodb+srv://root:mongodb123@cluster0.wbaic4i.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
'''hello'''
'''basu is genious'''
d = {
    "name":"nikkie",
    "email" : "nikkiie@gmail.com",
    "surname" : "panday"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )