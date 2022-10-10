from unit import Unit

class Zealot(Unit):
    def __init__(self):
        self.tribe = "Protoss"
        self.name = "Zealot"

        self.size_X = 30
        self.size_Y = 30
        
        self.require_mineral = 100
        self.require_gas = 0
        self.require_population = 2

        self.exist_shield = True
        self.exist_healingfactor = False
        self.exist_mana = False
        self.size_type = 1
        self.material_type = 2
        self.invincibility = False
        self.health = 80
        self.shield = 100
        self.armor = 1
        self.selectable_type = 3
        
        self.fly_level = 1
        self.view_range = 5
        self.move_speed = 4

        self.ground_attack_damage = 16
        self.ground_attack_range = 1
        self.ground_attack_cooltime = 20
        self.ground_attack_projectile = False
        self.ground_attack_type = 1

        self.detecting = False
        self.cloaking = False
        self.kill_count = 0
        