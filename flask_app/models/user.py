from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User:
    def __init__( self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "Select * from users;"
        results = connectToMySQL('portfolio').query_db(query)
        users = []

        print(users)
        for user in results:
            users.append( cls(user) )
        
        return users

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name, last_name , email , password) VALUES ( %(first_name)s , %(last_name)s, %(email)s , %(password)s);"
        result =connectToMySQL('portfolio').query_db( query, data )
        print(result)
        return result