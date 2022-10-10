from . import BaseObject

class VespeneGas(BaseObject):
    resource = 0

    def __init__(self, x, y, resource = 5000):
        self.name = "Vespene Gas"
        self.invincibility = True
        self.resource = resource
        self.cors_X = x
        self.cors_Y = y
