# Name: Joshua Jansen
# OSU Email: Jansejos@oregonstate.edu
# Course: CS325
# Assignment: 5

def feedDog(hunger_level, biscuit_size):
    """
    Matches two arrays of integers against each other to find how many integers in one array are greater than or equal
    to the other array.
    :param hunger_level: Array of integers.
    :param biscuit_size: Array of integers.
    :return: Number of integers from :param biscuit_size: that are pared with :param hunger_level: that are greater
    than or equal to.
    """
    hunger_level.sort()
    biscuit_size.sort()
    count = 0
    size = 0
    hunger = 0
    while size < len(biscuit_size) and hunger < len(hunger_level):
        if biscuit_size[size] >= hunger_level[hunger]:
            count += 1
            hunger += 1
            size += 1
        else:
            size += 1
    return count
