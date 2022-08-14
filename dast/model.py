from enum import Enum

class Dance:
    pass

class Level(Enum):
    NO_EXPERINCE = 1
    MIDDLE = 2
    GOOD = 3

class DanceProfile:
    def __init__(self, dance, level):
        self.dance = dance
        self.level = level

class Dancer:
    def __init__(self, zip_code, dancer_name, age, size):
        self.zip_code = zip_code

class User:
    def __init__(self) :
        self.id = ""


