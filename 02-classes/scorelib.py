import re

class Voice:
    def __init__(self, name, range):
        self.name = name
        self.range = range


class Person:
    def __init__(self, name, born, died):
        self.name = name
        self.born = born
        self.died = died


class Composition:
    def __init__(self, name, incipit, key, genre, year, voices, persons):
        self.name = name
        self.incipit = incipit
        self.key = key
        self.genre = genre
        self.year = year
        self.voices = voices
        self.authors = persons


class Print():
    def __init__(self, print_id, partiture, editions):
        self.edition = editions
        self.print_id = print_id
        self.partiture = partiture

    @staticmethod
    def parse_print_id(line):
        id_re = re.compile(r"Print Number: (\d+)")
        if id_re.match(line):
            return line.split(':')[1].strip()
        return None

    @staticmethod
    def parse_partiture(line):
        partiture_re = re.compile(r"Partiture: .?")
        match = partiture_re.match(line)
        if match :
            line.split(':')[1].strip()
        return None


    def format(self):
        print("Print Number: {}".format(self.print_id))

    def composition(self):
        return self.edition.composition


class Edition:
    def __init__(self, name, composition, persons):
        self.composition = composition
        self.authors = persons
        self.name = name


def load(filename):
    prints = []
