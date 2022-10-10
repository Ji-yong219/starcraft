from . import BaseObject

class Unit(BaseObject):
    require_mineral = None
    require_gas = None
    require_population = None


    fly_level = None
    # 1 : Ground
    # 2 : Hover
    # 3 : Air

    view_range = None
    move_speed = None

    attack_target = None
    # 1 : ground
    # 2 : air
    # 3 : both

    ground_attack_type = None
    # 1 : Normal
    # 2 : Explosive
    # 3 : Concussive

    ground_attack_range = None
    ground_attack_cooltime = None
    ground_attack_projectile = None
    ground_attack_damage = None
    

    air_attack_type = None
    # 1 : Normal
    # 2 : Explosive
    # 3 : Concussive

    air_attack_range = None
    air_attack_cooltime = None
    air_attack_projectile = None
    air_attack_damage = None

    cloaking = None
    kill_count = None

    def move(self, x, y):
        pass

    def stop(self):
        pass

    def attack(self, x, y):
        pass

    def patrol(self, x, y):
        pass

    def hold(self):
        pass

    def gather(self, target):
        pass

    def build(self, target):
        pass