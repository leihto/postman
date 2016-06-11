import sqlite3


class Db:

    Handler = None
    Cursor = None

    def __init__(self):
        self.Handler = sqlite3.connect("postman.db")
        self.create_database()

    def get_cursor(self):
        self.Cursor = self.Handler.cursor()

    def create_database(self):
        self.get_cursor()
        self.Cursor.execute('''CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY,
            address TEXT,
            method TEXT,
            content_type TEXT,
            content TEXT,
            response_code INTEGER,
            response_body TEXT,
            request_time REAL
        )''')
        self.Handler.commit()

    def insert(self, address, method, content_type, content, response_code, response_body, request_time):
        self.get_cursor()
        self.Cursor.execute('INSERT INTO requests VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)',
                            (str(address), str(method), str(content_type), str(content), response_code,
                                str(response_body), request_time))
        self.Handler.commit()

    def fetch_all(self):
        self.get_cursor()
        d = self.Cursor.execute('SELECT * FROM requests ORDER BY id DESC')
        self.Handler.commit()
        return d

    def fetch_one(self, index):
        self.get_cursor()
        d = self.Cursor.execute('SELECT * FROM requests WHERE id = ?', (index,))
        self.Handler.commit()
        return d.fetchone()

    def __del__(self):
        self.Handler.close()
