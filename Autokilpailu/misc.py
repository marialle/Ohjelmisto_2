import settings


def foo(s):
    ret = ''
    i = True # capitalize
    for char in s:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != '':
            i = not i
    return ret


def bye():
    s = settings.game['input']
    hehe = foo(s)
    for i in range(3):
        print(hehe)


def finished():
    print(f"Voittaja on {settings.game['winner']}!")
    print(f"Peli kesti {settings.game['time']} tuntia.")
    print(f"Hyvin pelattu {settings.game['player']}.\n")