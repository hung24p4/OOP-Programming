class Vampire:
    R = 1
    def __init__(self, N, G, P):
        self.name = N
        self.gender = G
        self.power = P
        self.rank = Vampire.R
        Vampire.R += 1

    def intro(self):
        print(str(self.rank) + '. My name is', self.name)
        print('I am', self.gender)
        print(self.power, 'is what I can do')
        print()

Vampire_A = Vampire('Gabriel', 'Male', 'Shooting beam from eyes')
Vampire_A.intro()

Vampire_B = Vampire('Taurius', 'Male', 'Empowering physical strength')
Vampire_B.intro()

Vampire_C = Vampire('Liyana', 'Female', 'Creating illusion')
Vampire_C.intro()