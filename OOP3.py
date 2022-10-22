# class method
# static method

lst_vam = ['Tayrel - Male - Damage Absorption', 'Avenllion - Female - Ice Manipulation']
class Vampire:
    R = 1
    race = 'Prime'
    def __init__(self, N, G, P):
        self.name = N
        self.gender = G
        self.power = P
        self.rank = Vampire.R
        Vampire.R += 1

    #regularmethod
    def intro(self):
        print(str(self.rank) + '. My name is', self.name)
        print('I am', self.gender)
        print(self.power, 'is what I can do')
        print(self.race)
        print()

    @classmethod
    def update_info(cls,string_vam,new_race):
        lst = string_vam.split('-')
        new_lst = [st.strip() for st in lst]
        name, gender, power = new_lst
        cls.race = new_race
        return cls(name,gender,power)

    @staticmethod
    def pseudo_update_info(self):
        None

Vampire_A = Vampire('Gabriel', 'Male', 'Shooting beam from eyes')
Vampire_A.intro()

Vampire_B = Vampire('Taurius', 'Male', 'Empowering physical strength')
Vampire_B.intro()

Vampire_C = Vampire('Liyana', 'Female', 'Creating illusion')
Vampire_C.intro()

for string_vam in lst_vam:
    Vampire_X = Vampire.update_info(string_vam,"Artificial")
    Vampire_X.intro()

Vampire_Y = Vampire('Krys', 'Male', 'Flying by wings')
Vampire_Y .race = 'Prime'
Vampire_Y.intro()