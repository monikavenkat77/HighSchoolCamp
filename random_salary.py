"""
title: random_salary
author: Monika
date: 2019-06-12 09:50
"""


name = input("Enter you name:")
salary = int(input("Enter your salary:"))
print(f"{name}, your current salary is {salary}")

import random
raise_per = random.randint(0, 100)

print(f"Your raise is {raise_per}% of {salary}")
raise_amount = salary + salary*(raise_per/100)

print(f"Your new salary is {raise_amount}")
