import mysql.connector

class DBHandler:
    def __init__(self,
                 username: str = 'root',
                 password: str = 'password',
                 data_base: str = 'StarkIndustries'
                 ) -> None:
        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = username,
            passwd = password
            )
        self.my_cursor = self.mydb.cursor()
        self.db = data_base

    def _list_db(self):
        self.my_cursor.execute('SHOW DATABASES')
        for db in self.my_cursor:
            print(db)

    def create_db(self):
        self.my_cursor.execute(f'CREATE DATABASE {self.db}')
        print(f'DB "{self.db}" created:')
        self._list_db()
        print()

    def delete_db(self):
        self.my_cursor.execute(f'DROP DATABASE {self.db}')
        print(f'DB "{self.db}" deleted:')
        self._list_db()
        print()
    
    def reset_db(self):
        self.my_cursor.execute('SHOW DATABASES')
        all_dbs: tuple[str] = ()
        for db in self.my_cursor:
            all_dbs += db
        if self.db in all_dbs:
            self.delete_db()
        self.create_db()

if __name__ == '__main__':
    db_handler = DBHandler()
    db_handler.reset_db()