"""This file contains environment functions that are used in the simulations."""
import time

from Agent import *


def hazard():
    """simulate the environment's hazards"""
    return


def social():
    """social life simulation for men"""
    return


def resource():
    # aggriculture than hunting
    # seansonal stuff comes in
    # plant -> grow -> harvest
    # multiple resources
        # flax/wool(from sheep/goat)  --> clothing (periodic attention)
        # wheat (periodic attention)
        # olives
        # goat (no need too much attentions) *
        # chickens *
        # bee
        # herbs
        # water *
        # salt
        # dogs * (scare off strangers)

    return


def master(env, slave):
    yield env.timeout(2)
    slave.action.interrupt()


def main():
    start = time.time()
    slaves = []
    for i in range(1):
        slave = Slave(env, i)
        slave.assign_work(env, ["cook", "sleep", "harvest", "cook"], [2, 4, 3, 5])
        slaves.append(slave)

        # env.process(master(env, Slave(env, i)))

    env.run(until=20)

    end = time.time()
    print()
    print("total time spent: %s s" % (end-start))


if __name__ == '__main__':
    main()