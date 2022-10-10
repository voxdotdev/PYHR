'''
The provided code stub reads an int, n, from STDIN. 
For all non negative ints less than n, i < n, square them and print, i ** 2

'''

n = int(input())

square_range = range(0, n)

for i in square_range:
    print(i ** 2)