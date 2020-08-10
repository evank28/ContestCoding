# Sample code to read input and write output:

'''
NAME = input()                # Read input from STDIN
print("Hello " + NAME)        # Write output to STDOUT
'''

# Warning: Printing unwanted or ill-formatted
# data to output will cause the test cases to fail

# Write your code here
int_in = int(input())
bin_rep = bin(int_in)
bin_str = str(bin_rep)
print(bin_str.count('1'))
