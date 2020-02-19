print (1,2,3)

def myfunct (x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec  = {'x': 1, 'y': 0, 'z': 1}

myfunct(*tuple_vec)
myfunct(*dict_vec)
myfunct(**dict_vec)

x = [1,2,3][:2]

type(x)
