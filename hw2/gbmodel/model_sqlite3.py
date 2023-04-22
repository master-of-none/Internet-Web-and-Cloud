import sqlite3
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
            cursor.execute("select cout(rowid) from building")
        
        except sqlite3.OperationalError:
            cursor.execute("create table building (bname text, bcode text, bfloor integer, closeRoomNumber integer, rating real )")
