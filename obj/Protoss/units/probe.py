from unit import Unit

class Probe(Unit):
    def __init__(self):
        self.tribe = "Protoss"
        self.name = "Probe"

        self.size_X = 30
        self.size_Y = 30

        self.require_mineral = 50
        self.require_gas = 0
        self.require_population = 1

        self.exist_shield = True
        self.exist_healingfactor = False
        self.exist_mana = False
        self.size_type = 1
        self.material_type = 1
        self.invincibility = False
        self.health = 20
        self.shield = 20
        self.armor = 0
        self.selectable_type = 3
        
        self.fly_level = 2
        self.view_range = 5
        self.move_speed = 5

        self.ground_attack_damage = 5
        self.ground_attack_range = 2
        self.ground_attack_cooltime = 20
        self.ground_attack_projectile = False
        self.ground_attack_type = 1

        self.detecting = False
        self.cloaking = False
        self.kill_count = 0
