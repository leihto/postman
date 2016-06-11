from postman.Request import Request
from postman.Db import Db


class Postman:

    URL = 'http://localhost:8080'
    METHOD = 'GET'
    CONTENT = ''
    CONTENT_TYPE = 'application/json'

    COMMANDS = [
        '!seturl ', '!setmethod ', '!setcontent ', '!setcontenttype ', '!send',
        '!exit', '!showhistory', '!setfromhistory ', '!showrecord ', '!help'
    ]

    HELP = [
        'ustawiania adresu url na ktory postman ma uderzyc.\n\nPrzykladowe uzycie: %s%s' % (COMMANDS[0], URL),
        'ustawienia metody zapytania w postmanie.\n\nPrzykladowe uzycie: %s%s' % (COMMANDS[1], METHOD),
        'ustawienia contentu zapytania.\n\nPrzykladowe uzycie: %sZawartosc zapytania' % COMMANDS[2],
        'ustawienia typu contentu zapytania.\n\nPrzykladowe uzycie: %s%s' % (COMMANDS[3], CONTENT_TYPE),
        'wyslania requesta na podany adres.\n\nPrzykladowe uzycie: %s' % COMMANDS[4],
        'zamkniecia programu.\n\nPrzykladowe uzycie: %s' % COMMANDS[5],
        'pokazywania historii zapytan.\n\nPrzykladowe uzycie: %s' % COMMANDS[6],
        'ustawienia parametrow zapytania z historii.\n\nPrzykladowe uzycie: %s5' % COMMANDS[7],
        'wyswietlenia pelnych danych oraz odpowiedzi zapytania.\n\nPrzykladowe uzycie: %s5' % COMMANDS[8],
        'wyswietlenia tej pomocy.\n\nPrzykladowe uzycie: %s' % COMMANDS[9]
    ]

    Connection = None

    def __init__(self):
        self.Connection = Db()
        print("\n\nPostman v.0.0.1\n")
        while True:
            command = input("Podaj komende: ")
            if command.find(self.COMMANDS[0]) == 0:
                self.set_url(command.replace(self.COMMANDS[0], ''))
            if command.find(self.COMMANDS[1]) == 0:
                command = command.replace(self.COMMANDS[1], '')
                if self.validate_methods(command):
                    self.set_method(command)
                else:
                    print("Niepoprawna metoda! Poprawne metody to: POST, GET, PUT, DELETE")
            if command.find(self.COMMANDS[2]) == 0:
                self.set_content(command.replace(self.COMMANDS[2], ''))
            if command.find(self.COMMANDS[3]) == 0:
                self.set_content_type(command.replace(self.COMMANDS[3], ''))
            if command.find(self.COMMANDS[4]) == 0:
                print("Wysylanie requestu pod adres " + self.URL)
                request = Request(self.Connection)
                request.send(self.URL, self.METHOD, self.CONTENT.replace("\\", ""), self.CONTENT_TYPE)
            if command.find(self.COMMANDS[5]) == 0:
                break
            if command.find(self.COMMANDS[6]) == 0:
                data = self.Connection.fetch_all()
                self.show_all(data)
            if command.find(self.COMMANDS[7]) == 0:
                try:
                    index = int(command.replace(self.COMMANDS[7], ''))
                    if index > 0:
                        row = self.Connection.fetch_one(index)
                        if row is None:
                            print("Podany rekord nie istnieje! Wybierz inny...")
                        else:
                            self.set_url(row[1])
                            self.set_method(row[2])
                            self.set_content_type(row[3])
                            self.set_content(row[4])
                            print("Ustawiono dane z rekordu: %i" % row[0])
                    else:
                        print("Bledny klucz. Klucz moze byc tylko liczba wieksza od 0!")
                except ValueError:
                    print("Bledny typ klucza. Klucz moze byc tylko liczba!")
            if command.find(self.COMMANDS[8]) == 0:
                try:
                    index = int(command.replace(self.COMMANDS[8], ''))
                    if index > 0:
                        row = self.Connection.fetch_one(index)
                        if row is None:
                            print("Podany rekord nie istnieje! Wybierz inny...")
                        else:
                            self.show_record(row)
                    else:
                        print("Bledny klucz. Klucz moze byc tylko liczba wieksza od 0!")
                except ValueError:
                    print("Bledny typ klucza. Klucz moze byc tylko liczba!")
            if command.find(self.COMMANDS[9]) == 0:
                self.show_help()
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

    def show_record(self, data):
        print('Rekord: %i\n\nAdres url: %s\nMetoda: %s\nTyp zapytania: %s\n'
              'Zapytanie: %s\n\nKod odpowiedzi: %i\nCzas wykonania: %.2fs\n\n'
              'Odpowiedz serwera: %s\n\n' % (data[0], data[1], data[2], data[3], data[4], data[5], data[7], data[6]))

    def show_all(self, data):
        print("Klucz\t | \tUrl\t | \tMetoda\t | \tTyp zapytania\t | \tZapytanie\t | \tStatus\t | \tCzas wykonania\t\n")
        for row in data:
            print("%i | %s | %s | %s | %s | %i | %.2f\n" % (row[0], row[1], row[2], row[3], row[4], row[5], row[7]))

    def show_help(self):
        print("Postman v.0.0.1 by Wojciech Pitek\n")
        for i in range(0, self.COMMANDS.__len__()):
            print('---------------------------------------------------------------\n')
            print('Komenda %s\nKomenda sluzy do %s\n' % (self.COMMANDS[i], self.HELP[i]))
