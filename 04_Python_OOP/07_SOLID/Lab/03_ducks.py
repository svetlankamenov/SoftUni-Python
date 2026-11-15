from abc import abstractmethod, ABC


class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def fly(self):
        pass

class Toy(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class RubberDuck(Toy):
    def make_sound(self):
        return "Squeek"


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    def quack(self):
        return 'Robotic quacking'

    def walk(self):
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0