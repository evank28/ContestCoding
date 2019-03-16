repeats = int(input())
messages = []
for i in range(repeats):
    messages.append(input())

import time
start_time = time.time()

encoding = []

def SetOfListInOrder(incominglist):
    from collections import OrderedDict
    outtemp = OrderedDict()
    for item in incominglist:
        outtemp[item] = None
    return(list(outtemp))


for message in messages:
    final_arr = []
    for diff in SetOfListInOrder(message):
        for letter in diff:
            final_arr.append(str(message.count(letter)) + " " + letter)
    print(" ".join(final_arr))

end_time = time.time()
print(end_time-start_time)