from mysql.connector import Error
import file_utils
import datetime
import mysql.connector



def insert_movie(title, genre, year):
    # try:
        # connection = mysql.connector.connect(
        #     host='localhost',
        #     database='movies_db',
        #     user='root',
        #     password='admin'
        # )
        cursor = dataBase.cursor()

        # if connection.is_connected():
        # cursor = connection.cursor()
        insert_query = """INSERT INTO movies (title, genre, year) VALUES (%s, %s, %s)"""
        record = (title, genre, year)
        cursor.execute(insert_query, record)
        # connection.commit()
        print("Record inserted successfully into movies table")

    # except Error as e:
    #     print(f"Error: {e}")
    # finally:
    #     if connection.is_connected():
    #         cursor.close()
    #         connection.close()
    #         print("MySQL connection is closed")

def main():
    
    json_file = "IMDB Movies 2000 - 2020.json"
    imdb_movies = file_utils.read_json_data(json_file)
    
    dataBase = mysql.connector.connect(
        host ="localhost",
        user ="admin",
        passwd ="admin",
        database='jpa',
    )
    cursor = dataBase.cursor()
    
    for movie in imdb_movies:
        date_published = datetime.datetime.strptime(movie['date_published'], '%d/%m/%Y').strftime('%Y-%m-%d')
        insert_query = """INSERT INTO movies (id, title, genre, year, created_date) VALUES (UUID(), %s, %s, %s, %s)"""
        record = (movie['title'], movie['genre'], movie['year'], date_published)
        cursor.execute(insert_query, record)
        print("Record inserted successfully into movies table")
    dataBase.commit()
    
if __name__ == "__main__":
    main()