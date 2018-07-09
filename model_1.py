from collections import namedtuple
import numpy as np

Coordinate = namedtuple("Coordinate", ["y", "x"])
Perception = namedtuple("Perception", ["agent_ls", "ripen_food_ls", "unripen_food_ls"])

rep_empty = "  "
rep_agent = "@ "
rep_ripen_food = "+ "
rep_unripen_food = "- "


class Environment:
    def __init__(self, height, width):
        self.agents = []
        self.plants = []
        self.height = height
        self.width = width
        self.map = []
        for i in range(height):
            self.map.append([])
            for j in range(width):
                self.map[i].append("  ")

    def update(self):
        for i, agent in enumerate(self.agents):
            agent.update()
            if not agent.is_alive:
                del self.agents[i]
                continue
            # print(agent)
            self.map[agent.y][agent.x] = rep_agent
        for j, plant in enumerate(self.plants):
            plant.update()
            if not plant.is_alive:
                del self.plants[j]
                continue
            # print(plant)
            if plant.is_ripen:
                self.map[plant.y][plant.x] = rep_ripen_food
            else:
                self.map[plant.y][plant.x] = rep_unripen_food

    def print_map(self):
        print("  +" + (self.width * "--") + "+")
        for r, row in enumerate(self.map):
            line = str(r % 10) + " |"
            for col in row:
                line += col
            line += "|"
            print(line)
        print("  +" + (self.width * "--") + "+")
        print("   " + "".join(str(c % 10) + " " for c in range(self.width)))


class Agent:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.coordinate = Coordinate(y, x)
        self.energy = 100
        self.hungry = 0
        self.age = 0
        self.max_age = np.random.normal(30, 5)
        self.is_alive = 1
        self.history = []

    def __repr__(self):
        return "Location[x=%s, y=%s], age: %s, energy: %s, is_alive %s" % \
               (self.x, self.y, self.age, self.energy, self.is_alive)

    def perception(self, environment):
        """check for the environment"""
        # range for perception is x +- 2 and y +- 2
        results = Perception([], [], [])
        for y in range(self.y - 2, self.y + 3):
            for x in range(self.x - 2, self.x + 3):
                instance = environment[y][x]
                if instance == rep_agent:
                    results.agent_ls.append(Coordinate(y, x))
                elif instance == rep_ripen_food:
                    results.ripen_food_ls.append(Coordinate(y, x))
                elif instance == rep_unripen_food:
                    results.unripen_food_ls.append(Coordinate(y, x))
                else:
                    pass
        return results

    # todo: reason about movement using perception
    # def update(self, movement):
    def update(self):
        self.energy -= 10
        self.age += 0.1

        # self.move(movement)
        # if too old, remove
        if self.age >= self.max_age:
            self.is_alive = 0
        if self.energy <= 40:
            self.hungry = 1
        else:
            self.hungry = 0

    def move(self, movement):
        """an agent cannot move to a proximate cell that is also proximate to another agent.
        This ensures that two different agents do not decide to move into the same cell."""

        mov_dict = {"0": [0, 0], "1": [0, 1], "2": [1, 1], "3": [1, 0], "4": [1, -1],
                    "5": [0, -1], "6": [-1, -1], "7": [-1, 0], "8": [-1, 1]}
        # todo: Catch this assertion Error
        assert movement in mov_dict, "The movement is invalid"
        self.x += mov_dict[movement][0]
        self.y += mov_dict[movement][1]

    def eat(self, food):
        if not food.is_ripen or not self.hungry:
            return
        else:
            food.alive = 0
            self.energy += 10


class Plant:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.coordinate = Coordinate(y, x)
        self.is_alive = 1
        self.is_ripen = 0
        self.grown_ts = 0

    def __repr__(self):
        return "Location[x=%s, y=%s], grow time: %s, is_ripen %s is_alive %s" % \
               (self.x, self.y, self.grown_ts, self.is_ripen, self.is_alive)

    def update(self):
        self.grown_ts += 1
        if self.grown_ts == 10:
            self.is_ripen = 1

    # todo(Lijia): def reproduce(self):


def spwan_food(environment):
    environment.plants.append(
        Plant(environment.height//2, environment.width//2)
    )


def put_agent(environment):
    environment.agents.append(
        Agent(np.random.choice(environment.height), np.random.choice(environment.width))
    )


def main():
    timestep = 11
    for i in range(timestep):
        if i == 0:
            env = Environment(height=10, width=10)
            spwan_food(env)
            put_agent(env)
            env.print_map()
        else:
            env.update()
            if i % 5 == 0:
                print("total time step: ", i)
                env.print_map()

if __name__ == '__main__':
    main()