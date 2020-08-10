# Sample code to read input and write output:

'''
NAME = raw_input()            # Read input from STDIN
print 'Hello %s' % NAME       # Write output to STDOUT
'''

# Warning: Printing unwanted or ill-formatted
# data to output will cause the test cases to fail

# Write your code here

ints_in = raw_input()
lst = ints_in.split(" ")
print len(lst)
