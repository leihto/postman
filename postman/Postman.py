from postman.Request import Request


class Postman:

    URL = 'http://localhost:8080'
    METHOD = 'GET'
    CONTENT = ''
    CONTENT_TYPE = 'application/json'

    def __init__(self):
        print("Postman v.1.0.0")
        while True:
            command = input("Podaj komende: ")
            if command.find('!seturl ') == 0:
                self.set_url(command.replace('!seturl ', ''))
            if command.find('!setmethod ') == 0:
                command = command.replace('!setmethod ', '')
                if self.validate_methods(command):
                    self.set_method(command)
                else:
                    print("Niepoprawna metoda! Poprawne metody to: POST, GET, PUT, DELETE")
            if command.find('!setcontent ') == 0:
                self.set_content(command.replace('!setcontent ', ''))
            if command.find('!setcontenttype ') == 0:
                self.set_content_type(command.replace('!setcontenttype ', ''))
            if command.find('!send') == 0:
                print("Wysylanie requestu pod adres " + self.URL)
                request = Request()
                request.send(self.URL, self.METHOD, self.CONTENT.replace("\\", ""), self.CONTENT_TYPE)
            if command.find('!exit') == 0:
                break

        print("Dzieki za korzystanie z programu!")

    def set_url(self, url):
        self.URL = url

    def set_method(self, method):
        self.METHOD = method

    def set_content(self, content):
        self.CONTENT = content

    def set_content_type(self, content_type):
        self.CONTENT_TYPE = content_type

    def validate_methods(self, method):
        return method in ['POST', 'PUT', 'GET', 'DELETE']
