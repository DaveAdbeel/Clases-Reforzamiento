from config.mysqlconnection import connectToMySQL

class Users:
    def __init__( self , data ):
        self.user_id = data['user_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL().query_db(query)
        print(results)
        return results
    
