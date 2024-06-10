import sqlite3
from pathlib import Path
          
class Database:
    PATH= Path(__file__).parent / "database.bd"
    
    def __init__(self):
        self.con= sqlite3.connect(self.PATH)
        self.cur= self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Files (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title VARCHAR(100),
                                file_path VARCHAR(150),
                                file_extension VARCHAR(5))""")
                                
    def query(self, query: str, data= tuple()):
        try:
            self.cur.execute(query, data)
            self.con.commit()
        except Exception as err:
            self.con.rollback()
            raise err
            
    def add_data(self, data: tuple):
        try:
            self.cur.execute("""INSERT INTO Files
                                (title, file_path, file_extension)
                                VALUES ( ?, ?, ?)""", data)
            self.con.commit()
        except Exception as err:
            self.con.rollback()
            raise err
            
    def get_datas(self):
        try:
            self.cur.execute("""SELECT * FROM Files""")
            return self.cur.fetchall()
        except Exception as err:
            self.con.rollback()
            raise err
        
    #delete_data(data)