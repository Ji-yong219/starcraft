from . import BaseObject

class Mineral(BaseObject):
    resource = 0

    def __init__(self, x, y, resource = 1500):
        self.name = "Mineral"
        self.invincibility = True
        self.resource = resource
        self.cors_X = x
        self.cors_Y = y
