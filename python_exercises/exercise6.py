'''
The included code stub will read an in n from STDIN

Without using any string methods, try to print the following:

123...n 
Note that ... represents the consecutive values in between.

Example: 
n = 5
print the string 12345

'''


n = int(input())
i = 0

while(i<n):
    i+=1
    print (i, end ="")


# Don't think this is what they were looking for, but passed challenge, good enough for now.