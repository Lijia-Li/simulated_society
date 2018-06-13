import numpy as np


class Household:
    def __init__(self, master, wife, slaves):
        # foodstuffs, energy, and the raw materials for making tools and clothing
        self.master = master
        self.wife = wife
        self.children = []
        self.slaves = slaves
        self.storage = 0    # todo: redifine storage and prep
        self.prep = 0

    def __repr__(self):
        return 'master=(%s), wife=(%s), #slave=%s, food=%s' % (
            self.master, self.wife, len(self.slaves), self.storage + self.prep)


class Agent:
    def __init__(self, gender):
        self.health = 100
        self.age = 0
        self.gender = gender
        self.effectiveness = 100
        # physical health
        # fertility
        # perception with understanding
        # reasoning
        # emotional?


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


# a subclass of Agent
class Man(Agent):
    def __init__(self):
        Agent.__init__(self, "male")
        self.think_ability = np.random.beta(0.5, 0.5)  #in interval [0, 1]
        self.spouse = None

    def __repr__(self):
        return 'gend=%s, think_a=%s, eff=%s, h=%s, a=%s' % (
            self.gender, self.think_ability, self.effectiveness, self.health, self.age)

    # todo (Lijia): complete below functions
    def reason(self):
        # gather information
        # reason
        # make command to slave
        return

    def command_to_slave(self):
        # asking to retrieve tools
        # specify which area to harvest in
        # order them to put resource back
        # possibly maintain tools
        return


# a subclass of Agent
class Woman(Agent):
    def __init__(self):
        Agent.__init__(self, "female")
        self.pregnant = False
        self.pregnant_ts = 0  # ts as in timestamp
        self.num_babies = 0
        self.spouse = None

    def __repr__(self):
        return 'gend=%s, #babies=%s, preg?=%s, eff=%s, h=%s, a=%s' % (
            self.gender, self.num_babies, self.pregnant, self.effectiveness, self.health, self.age)

    def prepre_food(self):
        return

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
        self.num_babies += 1

        choice = np.random.choice(2,1)[0]
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
                self.effectiveness = 0
        return


# a subclass of Agent
class Slave(Agent):
    def __init__(self):
        choice = np.random.choice(2, 1)[0]
        if choice == 0:
            Agent.__init__(self, "male")
        elif choice == 1:
            Agent.__init__(self, "female")

    def __repr__(self):
        return 'slave, gend=%s, eff=%s, h=%s, a=%s' % (
            self.gender, self.effectiveness, self.health, self.age)

    # todo (Lijia): complete below functions
    def harvest(self):
        # called when master decide to ask slave to harvest from environment
        return

    def report(self):
        # update master regarding tasks
        return
