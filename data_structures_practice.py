"""
title: data_structures
author: Monika
date: 2019-06-13 11:06
"""

#Data structures lab
import random

def shake_ball(options):
    options = ["yes, definitley", "As i see it, yes", 'Ask again later', "Cannot predict now","Don't count on it","Very dpubtful"]
    input("Enter a question:")
    random.choice(options)
    rnd_num = random.randint(0, len(options)-1)
    return options[rnd_num]

#print(shake_ball)

