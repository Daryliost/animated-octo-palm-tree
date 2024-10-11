#Practicing organizing code by using classes, I want to create monsters that can attack eachother, but each have different attributes, abilities ect.

class Monster:
    #Define the monster
    def __init__(self, monster, level, category, armour_level, life, weapon_level):
        self.monster = monster
        self.level = level
        self.category = category
        self.armour_level = armour_level
        self.life = life
        self.weapon_level = weapon_level

    def damage(self, life_damage):
        life_damage = self.life - self.weapon_level
        return life_damage
    


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