#Practicing organizing code by using classes, I want to create monsters that can attack eachother, but each have different attributes, abilities ect.

class Monster:
    #Define the monster
    def __init__(self, monster, level, category, armour_level, arm_durability, arm_health_pool, life, weapon_level, wep_durability, wep_health_pool):
        self.monster = monster
        self.level = level
        self.category = category
        self.armour_level = armour_level
        self.arm_durability = arm_durability
        self.arm_health_pool = arm_health_pool
        self.life = life
        self.weapon_level = weapon_level
        self.wep_durability = wep_durability
        self.wep_health_pool = wep_health_pool

    def damage(self):
        total_weapon_damage = self.weapon_level - self.armour_level
        damage_armour = self.arm_durability - self.weapon_level
        damage_weapon = self.wep_health_pool - self.armour_level
        damage_health = self.life - self.weapon_level
        return total_weapon_damage, damage_armour, damage_weapon, damage_health


ogre = Monster(monster = 'ogre', level = 50, category = 'giant', armour_level = 1, arm_durability = 100, arm_health_pool = 100, life = 100, weapon_level = 6, wep_durability = 100, wep_health_pool = 100)

human = Monster(monster = 'Chad', level = 30, category = 'Humanoid', armour_level = 3, arm_durability = 100, arm_health_pool = 100, life = 100, weapon_level = 3, wep_durability = 100, wep_health_pool = 100)

bear = Monster(monster = 'Bear', level = 20, category = 'Mammal', armour_level = 0, arm_durability = 0, arm_health_pool = 100, life = 100, weapon_level = 3, wep_durability = 100, wep_health_pool = 100)

gorilla = Monster(monster = 'Harambe', level = 30, category = 'Mammal', armour_level = 3, arm_durability = 100, arm_health_pool = 100, life = 100, weapon_level = 3, wep_durability = 100, wep_health_pool = 100)

garden_gnome = Monster(monster = 'Gnome', level = 100, category = 'Lawn Decor', armour_level = 6, arm_durability = 100, arm_health_pool = 100, life = 100, weapon_level = 6, wep_durability = 100, wep_health_pool = 100)

def main() -> None:
    monsters = {
        'ogre': ogre,
        'human': human,
        'bear': bear,
        'gorilla': gorilla,
        'garden gnome': garden_gnome
    }

    Fighter1 = input('choose your monster, "Ogre, Human, Bear, Gorilla, or Garden Gnome: ').strip().lower()
    Fighter2 = input('choose opposing monster, "Ogre, Human, Bear, Gorilla, or Garden Gnome: ').strip().lower()

    if Fighter1 in ['ogre','human','bear','gorilla','garden','gnome','garden gnome','gardengnome']:
        print(f'you have selected {Fighter1} and {Fighter2}')
    else:
        print('Invalid creature, please select another')
    
    Fighter1 = monsters[Fighter1]
    Fighter2 = monsters[Fighter2]




if __name__ == '__main__':
    main()