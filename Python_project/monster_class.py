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
        self.life -= life_damage
        return self.life

    def attack(self, other):
        damage_dealt = self.weapon_level - other.armour_level
        if damage_dealt > 0:
            other.damage(damage_dealt)
            return(damage_dealt)
        else:
            other.damage(1)
            return(damage_dealt)
    


ogre = Monster(monster = 'ogre', level = 50, category = 'giant', armour_level = 1,life = 100, weapon_level = 6,)

human = Monster(monster = 'Chad', level = 30, category = 'Humanoid', armour_level = 3, life = 100, weapon_level = 3,)

bear = Monster(monster = 'Bear', level = 20, category = 'Mammal', armour_level = 0, life = 100, weapon_level = 3,)

gorilla = Monster(monster = 'Harambe', level = 30, category = 'Mammal', armour_level = 3, life = 100, weapon_level = 3,)

garden_gnome = Monster(monster = 'Gnome', level = 100, category = 'Lawn Decor', armour_level = 6, life = 100, weapon_level = 6,)

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

    if Fighter1 in monsters and Fighter2 in monsters:
        fighter1 = monsters[Fighter1]
        fighter2 = monsters[Fighter2]
        
        while fighter1.life > 0 and fighter2.life > 0:

            fighter1.attack(fighter2)
            print(f'{fighter1.monster} swings at {fighter2.monster} dealing {fighter1.attack} damage!')

            if fighter2.life <= 0:
                print(f'{fighter2.monster} is defeated! {fighter1.monster} is victorious!')
                break
            
            fighter2.attack(fighter1)
            print(f'{fighter2.monster} swings at {fighter2.monster} dealing {fighter2.monster} damage!')

            if fighter1.life <= 0:
                print(f'{fighter1.monster} is defeated! {fighter2.monster} is victorious!')
        

if __name__ == '__main__':
    main()