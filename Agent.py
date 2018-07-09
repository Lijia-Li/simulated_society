import numpy as np
import simpy
from collections import namedtuple

Assignments = namedtuple('Assignments', ('work_list', 'work_time'))


class Environment:
    def __init__(self):
        self.season = []
        self.weather = []
        self.water = []
        self.food = []


class Household:
    def __init__(self, id, master, wife, slaves):
        # foodstuffs, energy, and the raw materials for making tools and clothing
        self.id = id
        self.master = master
        self.wife = wife
        self.slaves = slaves
        self.children = []
        self.storage = 0  # the amount of food in storage
        self.kitchen = 0  # the amount of food in kitchen
        self.land = 0

    def __repr__(self):
        return 'household #%s master=(%s), wife=(%s), #slave=%s, food=%s' % (
            self.id, self.master, self.wife, len(self.slaves), self.storage + self.kitchen)


class Agent:
    def __init__(self, env, household_id, gender):
        self.household_id = household_id
        self.health = 100
        self.age = 0
        self.gender = gender
        self.effectiveness = 100
        self.env = env
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
    def __init__(self, env, household_id):
        Agent.__init__(self, env, household_id, "male")
        self.think_ability = np.random.beta(0.5, 0.5)  #in interval [0, 1]
        self.spouse = None
        # todo (Lijia): link up the spouse

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

    def mind(self):
        """this function shall simulate the mind model of the world"""
        # a bayesian network to simulate mind stemp


# a subclass of Agent
class Woman(Agent):
    def __init__(self, env, household_id):
        Agent.__init__(self, env, household_id, "female")
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
            return Man(self.env, self.household_id)
        elif choice == 1:
            return Woman(self.env, self.household_id)

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
    def __init__(self, env, household_id, id):
        choice = np.random.choice(2, 1)[0]
        if choice == 0:
            Agent.__init__(self, env, household_id, "male")
        elif choice == 1:
            Agent.__init__(self, env, household_id, "female")
        self.id = id

    def __repr__(self):
        return 'slave #%s, gend=%s, eff=%s, h=%s, a=%s' % (
            self.id, self.gender, self.effectiveness, self.health, self.age)

    def assign_work(self, assignments):
        self.action = self.env.process(self.work(assignments))

    def work(self, assignments):
        if len(assignments) != len(assignments.work_time):
            raise AssertionError('the duration and Assignments are not one to one')
        else:
            while True:
                for i, assignment in enumerate(assignments.work_list):
                    try:
                        if assignment == "harvest":
                            yield self.env.process(self.harvest(assignments.work_time[i]))
                        elif assignment == "rest":
                            yield self.env.process(self.rest(assignments.work_time[i]))
                        elif assignment == "cook":
                            yield self.env.process(self.cook(assignments.work_time[i]))
                        elif assignment == "sleep":
                            yield self.env.process(self.sleep(assignments.work_time[i]))
                        else:
                            raise AttributeError("no such action is available")
                    except simpy.Interrupt:
                        print('# %s slave was interrupted at %s' % (self.id, self.env.now))

    def harvest(self, duration):
        # called when master decide to ask slave to harvest from environment
        print('# %s slave start harvesting at %s' % (self.id, str(self.env.now)))
        yield self.env.timeout(duration)

    def rest(self, duration):
        print('# %s slave start resting at %s' % (self.id, str(self.env.now)))
        yield self.env.timeout(duration)

    def cook(self, duration):
        print('# %s slave start cooking at %s' % (self.id, str(self.env.now)))
        yield self.env.timeout(duration)

    def sleep(self, duration):
        print('# %s slave start sleeping at %s' % (self.id, str(self.env.now)))
        yield self.env.timeout(duration)

    def report(self):
        # update master regarding tasks
        return

    # slave need to control the animals
