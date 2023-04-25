"""
Backend app for to store college building details

"""

from .Model import Model
import sqlite3
DB_FILE = 'buildings.db'

class model(Model):
    def __init__(self):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()

        try:
            cursor.execute("select count(rowid) from building")
        
        except sqlite3.OperationalError:
            cursor.execute("create table building (bname text, bcode text, bfloor integer, closeRoomNumber integer, rating real )")

        cursor.close()

    def select(self):
        """
        This is used to get all the rows from the database
        Each row will have: Building name, Building code, building floor, Closest Room Number and rating.
        :return: List of lists containing all rows of database
        """

        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM building")
        return cursor.fetchall()

    def insert(self, bname, bcode, bfloor, closeRoomNumber, rating):
        """
        Inserts entries to database
        :param bname: String
        :param bcode: String
        :param bfloor: Int
        :param closeRoomNumber: Int
        :param rating: Float
        :return: True
        :raises: Database error on connection and insertion
        """

        params = {'bname':bname, 'bcode':bcode, 'bfloor':bfloor, 'closeRoomNumber':closeRoomNumber, 'rating':rating}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into building (bname, bcode, bfloor, closeRoomNumber, rating) VALUES(:bname, :bcode, :bfloor, :closeRoomNumber, :rating)", params)
        connection.commit()
        cursor.close()
        return True
