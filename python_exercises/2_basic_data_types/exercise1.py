'''
Given three integers, x, y and z representing the dimensions of a cuboid along with an 
int n, print a list of all possible coordinates given by i,j,k on a 3D grid 
where the sum of i + j + k is not equal to n. 

Here 0 < i < x; 0 < j < y; 0 < k < z

Use list comprehensions rather than multiple loops, as a learning exercise.
https://www.w3schools.com/python/python_lists_comprehension.asp
https://www.hackerrank.com/challenges/list-comprehensions/tutorial

Example 

x = 1 
y = 1
z = 2
n = 3

SAMPLE INPUT
1
1
1
2

SAMPLE OUTPUT
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

'''

x = int(input())
y = int(input())
z = int(input())
n = int(input())

print([[a, b, c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n])

'''
Explaination:
Starting with 0, assign a b c a value and print. 
Increment each variable by 1 each loop, until the sum of all three variables equals n. 
'''