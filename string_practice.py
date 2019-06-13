"""
title: string_practice
author: Monika
date: 2019-06-11 13:42
"""
#FIRST ONE

answer = input("enter a character:")
print(answer in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')


#SHORT HAND

def short_hand (short):
    short = short.replace("for", "4").replace("and", "&").replace("too", "2").replace("You", "U").replace("you", "U")
    short = short.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
    return short

print(short_hand("How are you today?"))

#REMOVE CASE AND PUNCTUATION

def removing(check):
    check = check.lower()
    check = check.replace(" ","").replace(",", "").replace(":", "").replace("'","").replace(";","")
    return check

print(removing("Madam, I'm Adam"))

#PALINDROME

def palindrome(check):
    check = removing(check)
    return check == check[::-1]

print(palindrome("Computer"))



#CREDENTIALS GENERATOR

#print(input("""first name:
#last name:
#city you were born in:
#university you graduated form:
#name of a relative:
#name of a friend:"""))