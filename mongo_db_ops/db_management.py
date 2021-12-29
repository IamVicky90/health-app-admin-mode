import os
import pymongo
import hashlib
class mongo_db_atlas_ops:
    def __init__(self):
        pass
    def get_mongo_db_connection(self):
        '''Responsible for the connection with MongoDB Atlas'''
        try:
            user=os.environ.get('MONGO_USER')
            mongo_password=os.environ.get('MONGO_PASSWORD')
            con=pymongo.MongoClient(f"mongodb+srv://{user}:{mongo_password}@cluster0.hpbfo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
            return con
        except Exception as e:
            raise e
    def return_entries_from_db(self,client):
        login_credentials=client['Human_and_Plant_Health_SDM']
        fname=[]
        lname=[]
        email=[]
        state=[]
        for items in login_credentials['login_credentials'].find():
            fname.append(items['fname'])
            lname.append(items['lname'])
            email.append(items['email'])
            state.append(items['state'])
        return fname,lname,email,state
mongo_obs=mongo_db_atlas_ops()
client=mongo_obs.get_mongo_db_connection()
mongo_obs.return_entries_from_db(client)

