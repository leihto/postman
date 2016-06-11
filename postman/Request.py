import requests
import time


class Request:

    URL = 'http://localhost:8080'
    CONTENT = ''
    CONTENT_TYPE = 'application/json'

    timestamp = 0

    def __init__(self, db):
        self.db_connection = db

    def send(self, url, method, content, content_type):
        self.timestamp = time.time()
        self.URL = url
        self.CONTENT = content
        self.CONTENT_TYPE = content_type
        print("\n")
        if method == 'GET':
            ts = self.send_get()
        elif method == 'POST':
            ts = self.send_post()
        elif method == 'PUT':
            ts = self.send_put()
        elif method == 'DELETE':
            ts = self.send_delete()
        else:
            print("Bledna metoda!")
        print("\nCzas wykonywania zapytania: %.2f" % ts)

    def send_get(self):
        r = requests.get(self.URL)
        print("Kod odpowiedzi: " + str(r.status_code))
        print(r.content)
        ts = time.time() - self.timestamp
        self.db_connection.insert(self.URL, 'GET', self.CONTENT_TYPE, self.CONTENT, r.status_code, r.content, ts)
        return ts

    def send_post(self):
        r = requests.post(self.URL, data=self.CONTENT, headers={'Content-Type': self.CONTENT_TYPE})
        print("Kod odpowiedzi: " + str(r.status_code))
        print(r.content)
        ts = time.time() - self.timestamp
        self.db_connection.insert(self.URL, 'POST', self.CONTENT_TYPE, self.CONTENT, r.status_code, r.content, ts)
        return ts

    def send_put(self):
        r = requests.put(self.URL, data=self.CONTENT, headers={'Content-Type': self.CONTENT_TYPE})
        print("Kod odpowiedzi: " + str(r.status_code))
        print(r.content)
        ts = time.time() - self.timestamp
        self.db_connection.insert(self.URL, 'PUT', self.CONTENT_TYPE, self.CONTENT, r.status_code, r.content, ts)
        return ts

    def send_delete(self):
        r = requests.delete(self.URL, data=self.CONTENT, headers={'Content-Type': self.CONTENT_TYPE})
        print("Kod odpowiedzi: " + str(r.status_code))
        print(r.content)
        ts = time.time() - self.timestamp
        self.db_connection.insert(self.URL, 'DELETE', self.CONTENT_TYPE, self.CONTENT, r.status_code, r.content, ts)
        return ts
