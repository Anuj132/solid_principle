'''
The Liskov substitution principle (LSP)
“Derived classes must be substitutable for their base classes”.
'''

class Person(object):

    def __init__(self, position):
        self.position = position

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_south(self, dist):
        self.position[0] += dist


class Prisoner(Person):  # Prisoner can walk, but shouldn't
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        self.position = self.PRISON_LOCATION
        self.is_free = False

'''
Above given code is violation of lsp.
below given code is not the violation of the lsp.
'''
class FreeMan(object):

    def __init__(self, position):
        self.position = position

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_south(self, dist):
        self.position[0] += dist


class Prisoner(object):  # Prisoner can't walk
    PRISON_LOCATION = (3, 3)

    def __init__(self):
        self.position = self.PRISON_LOCATION