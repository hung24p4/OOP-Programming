class Vampire:
    def __init__(self, N, G, P):
        self.name = N
        self.gender = G
        self.power = P

    def intro(self):
        print('My name is', self.name)
        print('I am', self.gender)
        print(self.power, 'is what I can do')

Vampire_A = Vampire('Gabriel', 'Male', 'Shooting beam from eyes')
Vampire_A.intro()
