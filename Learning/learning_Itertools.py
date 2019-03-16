import itertools
import operator

#Count function -- begins at START paramater and creates values incremented by STEP parameter
for i in itertools.count(10,3):
    print(i)
    if i>20:
        break

#repeat - itertools.repeat(value,limit)

#accumulate -- takes parameters of a list of values and a function. The iterating calls then use the 
    #value returned by the last call and the next value in the original list to call the next iteration

