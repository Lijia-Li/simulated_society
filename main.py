from Agent import *
from environment import *

env = simpy.Environment()

def main():
    # initialize parameters
    num_men, num_women, num_slave = [20, 20, 50]
    agents = []
    max_ts = 1000

    start = time.time()

    # construct households
    household_ls = [Household(x, Man(env, x), Woman(env, x), [Slave(env, x, i) for i in range(np.random.choice(5,1)[0])]) for x in range(10)]

    # testing households
    for household in household_ls:
        print(household.master)
        print(household.slaves)
        for slave in household.slaves:
            slave_assignment = Assignments(["cook", "sleep", "harvest", "cook"], [2, 4, 3, 5])
            slave.assign_work(slave_assignment)

    env.run(until=20)

    end = time.time()
    print()
    print("total time spent: %s s" % (end-start))




if __name__ == '__main__':
    main()