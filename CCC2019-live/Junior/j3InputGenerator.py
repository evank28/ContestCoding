import random, string
N = 100
print(N)
for row in range(N):
    line = ""
    for set in range (0,random.randint(1,20)):
        line += random.randint(1,10) * random.choice(string.ascii_letters + string.digits + string.punctuation)
    print(line)
