
"""
Backend app for to store recipe details

"""

# importing the Model class and sqlite3
from .Model import Model
import sqlite3

# database where we will store all the data
DB_FILE = 'recipes.db'

class model(Model):
    def __init__(self):
        """
        This function is used to initialise the database
        :return: nothing
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()

        try:
            cursor.execute("select count(rowid) from recipe")
        
        except sqlite3.OperationalError:
            cursor.execute("create table recipe (id integer, title text)")

        cursor.close()

    def select(self):
        """
        This is used to get all the rows from the database
        Each row will have: id of the recipe and title of the recipe.
        :return: List of lists containing all rows of database.
        """

        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM recipe")
        return cursor.fetchall()

    def insert(self, id, title):
        """
        Inserts entries to database
        :param id: int
        :param recipe: String
        :raises: Database error on connection and insertion
        """

        params = {'id':id, 'title':title} 
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into recipe (id, title) VALUES(:id, :title)", params)
        connection.commit()
        cursor.close()
        return True
