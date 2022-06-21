import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
            host = 'yh.cpos3ccatavx.ap-northeast-2.rds.amazonaws.com',
            database = 'resipe_db1',
            user = 'recipe_user2',
            password = 'recipe1234')
    
    return connection