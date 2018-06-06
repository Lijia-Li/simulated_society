import numpy


class Agent:
    def __init__(self, gender):
        self.health = 100
        self.age = 0
        self.gender = gender
        self.effectiveness = 100

    def get_health(self):
        return self.health

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    # todo: def __getattribute__(self, item):

    # todo: effectiveness calculation
    def update_effectiveness(self):
        """update the eff with age and health"""
        return

    def update(self):
        self.health -= 1
        self.age += 0.01

        # if self.age > 35:
        #     die()
        return

    def eat(self):
        self.health += 10
        return


class Man(Agent):
    def __init__(self):
        Agent.__init__(self, "male")
        self.think_ability = numpy.random.beta(0.5, 0.5)

    # todo: reason and make commands
    def reason(self):
        return


class Woman(Agent):
    def __init__(self):
        Agent.__init__(self, "female")
        self.pregnant = False
        self.pregnant_ts = 0  # ts as in timestamp
        # self.birth_mort_rate = numpy.random.beta(0.5, 0.5)

    # todo: perhaps using await?
    def pregnant(self):
        """the pregnant general function"""
        self.pregnant = True
        self.pregnant_ts += 0.01

        if self.pregnant_ts > 0.83:
            return self.give_birth()

    def give_birth(self):
        # todo: died by giving birth
        self.pregnant = False
        self.pregnant_ts = 0

        choice = numpy.random.choice(2,1)[0]
        if choice ==  0:
            return Man()
        elif choice == 1:
            return Woman()

    def is_pregnant(self):
        if self.pregnant:
            return True
        else:
            return False

    def update_effectiveness(self):
        """update the eff with age and health and pregnant situ"""
        # todo: effectiveness decrese with regard to pregnant timestamp?
        if self.is_pregnant():
            if self.effectiveness > 60:
                self.effectiveness -= 60
            else:
                self.effectiveness == 0
        return


class Slave(Agent):
    def __init__(self, gender):
        Agent.__init__(self, gender)

