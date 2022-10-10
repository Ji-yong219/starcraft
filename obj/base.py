class BaseObject:
    name = ""
    tribe = ""
    size_X = 0
    size_Y = 0
    cors_X = 0
    cors_Y = 0
    exist_shield = False
    exist_healingfactor = False
    exist_mana = False
    size_type = None
    # 1 : small
    # 2 : medium
    # 3 : large

    material_type = None
    # 1 : normal
    # 2 : Bionic
    # 3 : Mechanic

    invincibility = False
    health = None
    shield = None
    armor = None
    mana = None
    selectable_type = None
    # 1 : impossible
    # 2 : single
    # 3 : multiple

    detecting = None

    def __init__(self, x = 0, y = 0):
        self.cors_X = x
        self.cors_Y = y