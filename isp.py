'''
an interface is considered, all the methods and properties “exposed”,
thus, everything that a user can interact with that belongs to that class.
'''
from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass


class Mustang(Car):

    def start(self):
        # start implementation
        pass

    def accelerate(self):
        # accelerate implementation
        pass


# After We need to create DeloRean class

class Car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def back_to_the_past(self):
        pass

    @abstractmethod
    def back_to_the_future(self):
        pass


class Mustang(Car):

    def start(self):
        # start implementation
        pass

    def accelerate(self):
        # accelerate implementation
        pass

    def back_to_the_past(self):  # ?
        pass

    def back_to_the_future(self):  # ?
        pass


class DeloRean(Car):
    def start(self):
        # start implementation
        pass

    def accelerate(self):
        # accelerate implementation
        pass

    def back_to_the_past(self):
        pass

    def back_to_the_future(self):
        pass


'''
Above code is the not satisfied the fourth property of the solid principle.
And Below given code is satisfied the fourth property of the solid priciple
'''

from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass


class TimeMachine(ABC):

    @abstractmethod
    def back_to_the_past(self):
        pass

    @abstractmethod
    def back_to_the_future(self):
        pass


class Mustang(Car):

    def start(self):
        pass

    def accelerate(self):
        pass


class DeloRean(Car, TimeMachine):
    def start(self):
        pass

    def accelerate(self):
        pass

    def back_to_the_past(self):
        pass

    def back_to_the_future(self):
        pass