"""
title: loop_practice
author: Monika
date: 2019-06-13 13:39
"""

#for loops
for i in [89, 41, 73, 90]:
    print(i)
print()
for j in range(5,16):
    print(j, end = " ") #Reminder: end = " " prints all of the numbers on the same line with a space in between.
print()
for x in range(100,201,10):
    print(x, end = " ")
print()
for m in range(80,24,-8):
    print(m, end = " ")
print()
for L in range(3):
    print("alright")

#while loops
life = 10
while life >= 0:
    print(life, end="-")
    life -= 1

print()
x_input = (input("An integer greater than 0:"))

while x_input <= "0":
    print("waiting")
    x_input = (input("An integer greater than 0:"))

#print()
#first = int(input("enter a number:"))
#second = int(input("enter a second number:"))

#while second <= first:
#    input("First number must be larger!")

#while first < second:
#    print(first)
#    first += 1




#Ask the user to enter two separate integers (The first number must be smaller than the second). Create a while loop that will count from the first number to the second.

#Ask the user to respond by 'Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO'. The function keeps on asking until the user enters the correct information.




