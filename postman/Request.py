import requests


class Request:

    URL = 'http://localhost:8080'
    CONTENT = ''
    CONTENT_TYPE = 'application/json'

    def __init__(self):
        pass

    def send(self, url, method, content, content_type):
        self.URL = url
        self.CONTENT = content
        self.CONTENT_TYPE = content_type
        if method == 'GET':
            self.send_get()
        elif method == 'POST':
            self.send_post()
        elif method == 'PUT':
            self.send_put()
        elif method == 'DELETE':
            self.send_delete()
        else:
            print("Bledna metoda!")

    def send_get(self):
        r = requests.get(self.URL)
        print("Kod odpowiedzi: " + str(r.status_code))
        print(r.content)

    def send_post(self):
        r = requests.post(self.URL, data=self.CONTENT, headers={'Content-Type' : self.CONTENT_TYPE})
        print("Kod odpowiedzi: " + str(r.status_code))
        print(r.content)

    def send_put(self):
        r = requests.put(self.URL, data=self.CONTENT, headers={'Content-Type': self.CONTENT_TYPE})
        print("Kod odpowiedzi: " + str(r.status_code))
        print(r.content)

    def send_delete(self):
        r = requests.delete(self.URL, data=self.CONTENT, headers={'Content-Type': self.CONTENT_TYPE})
        print("Kod odpowiedzi: " + str(r.status_code))
        print(r.content)
