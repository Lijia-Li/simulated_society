import numpy as np
from Agent import *
from environment import *
from collections import namedtuple


def main():
    # initialize parameters
    num_men, num_women, num_slave = [20, 20, 50]
    agents = []
    max_ts = 1000

    # # construct agents:
    # men_ls = [Man() for i in range(num_men)]
    # women_ls = [Woman() for i in range(num_women)]
    # slave_ls = [Slave() for i in range(num_slave)]
    # agents = men_ls + women_ls + slave_ls
    #
    # for agent in agents:
    #     print(agent)

    # construct households
    household_ls = [Household(Man(), Woman(), [Slave() for i in range(np.random.choice(5,1)[0])]) for x in range(10)]

    # testing households
    for household in household_ls:
        print(household.master)
        print(household.slaves)

    for time in range(max_ts):
        # hazard might happen







if __name__ == '__main__':
    main()