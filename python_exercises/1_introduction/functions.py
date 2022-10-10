'''
https://www.hackerrank.com/challenges/write-a-function

An extra day is added to the calendar almost every four years as Feb 29th. 

It corrects the calendar for the fact Earth takes 365.25 days to orbit the sun. 
A leap year contains a leap day. 

In the Gregorian calendar, three conditions are used to identify leap years:

IS A LEAP YEAR: The year can be evenly divided by 4. 
IS NOT A LEAP YEAR: The year can be evenly divided by 100. UNLESS:
IS A LEAP YEAR: The year can be also evenly divided by 400. 

Given a year, determine whether it is a leap year. 
If it is a leap year, return the Boolean True, otherwise return false. 

'''


from operator import truediv


def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year / 4).is_integer():
        if (year / 100).is_integer(): 
            if (year / 400).is_integer():
                leap = True
        else: leap = True
    return leap

year = int(input())
print(is_leap(year))