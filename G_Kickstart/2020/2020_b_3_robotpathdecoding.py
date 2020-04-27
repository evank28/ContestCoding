# Google Kickstart 2020 Round B
# Code By Evan Kanter
# Solved 2020-04-18, live
import string


def move(direction:str, w:int, h:int) -> tuple:
    if direction == "N":
        if h > 1:
            h -= 1
        else:
            h = 10 ** 9
    elif direction == "S":
        if h < 10 ** 9:
            h += 1
        else:
            h = 1
    elif direction == "E":
        if w < 10 ** 9:
            w += 1
        else:
            w = 1
    elif direction == "W":
        if h > 1:
            w -= 1
        else:
            w = 10 ** 9
    return w,h


def index_of_close_bracket(program_string:str) -> int:
    """Precondition: First character should be the character after an open
     bracket, so the string is not balanced."""
    i = 0
    open_count = 0
    while i < len(program_string):
        c = program_string[i]
        if c == "(":
            open_count += 1
        elif c == ")":
            if open_count == 0:
                return i
            else:
                open_count -= 1
        else:
            pass
        i += 1
    raise AssertionError


# def evaluate(instructions: str, w: int, h: int) -> tuple:
#     i = 0
#     while i < len(instructions):
#         c = instructions[i]
#         if c in string.ascii_uppercase:
#             w, h = move(c, w, h)
#             i += 1
#         elif c in string.digits:
#             open_bracket = i+1
#             close_bracket = index_of_close_bracket(instructions[i+2:]) + 2 + i
#             for _ in range(int(c)):
#                 w, h = evaluate(instructions[open_bracket+1:close_bracket],
#                                 w, h)
#             i = close_bracket + 1
#         else:
#             raise AssertionError
#     return w, h


def convert_to_directions(program_string: str) -> str:
    """
    >>> convert_to_directions("EEEE4(N)2(SS)")
    'EEEENNNNSSSS'
    """
    out = ""
    i = 0
    while i < len(program_string):
        c = program_string[i]
        if c in string.ascii_uppercase:
            out += c
            i += 1
        elif c in string.digits:
            open_bracket = i + 1
            close_bracket = index_of_close_bracket(program_string[i+2:]) + 2 + i
            out += int(c) * convert_to_directions(program_string[open_bracket+1:
                                                                 close_bracket])
            i = close_bracket + 1
        else:
            raise TypeError
    return out


if __name__ == "__main__":
    t = int(input())
    for t in range(1,t+1):
        program = str(input())
        w = 1
        h = 1
        # w, h = evaluate(program, w, h)
        directions = convert_to_directions(program)
        for d in directions:
            w, h = move(d, w, h)
        print("Case #{}: {} {}".format(t, w, h))
