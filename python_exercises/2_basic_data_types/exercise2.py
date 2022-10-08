'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. 
Store them in a list, find the score of the runner-up, print it.

The first line contains n.
The second line contains an array A[] of n integers each separated by a space
'''

n = int(input()) # number of scores
x = list(map(int, input().split())) [:n] #creating list from input, until n reached
z = max(x) # storing max value 
while max(x) == z: # if max value in list is equal to currently stored max, get rid fo it. 
    x.remove(z)
print(max(x)) # print "runner up" score