
def func1(i: int, lst=[]) -> list:
    lst.append(i)
    return lst


for i in range(5):
    print(func1(i))

# def func2(i: int, num=1) -> int:
#     num = 1 + i
#     return num
#
#
# for i in range(5):
#     print(func2(i))
#
