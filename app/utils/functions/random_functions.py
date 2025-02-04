"""Contains functions to generate random values as needed."""
import time
import random
from app.utils.constants import constants

def random_wait():
    """
    Waits for a random amount of time between the max and min stipulated in the constants file.
    """
    wait = random.randint(constants.RandomWait.MIN,constants.RandomWait.MAX)
    time.sleep(wait)

def random_string(length):
    """
    Generates a random string of the given length.
    """
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(letters) for i in range(length))
