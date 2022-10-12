



from operator import truediv
from tabnanny import check
from tkinter import Checkbutton


def main(level, starforce):
    LP = LevelPower(level)
    SP = StarforcePower(starforce)


    return LP + SP + 12500


def LevelPower(level):

    modi = 0
    if checkBetween(level, 60, 99):
        modi = 0.5
    elif checkBetween(level, 100,139):
        modi = 0.4
    elif checkBetween(level, 140,179):
        modi = 0.7
    elif checkBetween(level, 180,199):
        modi = 0.8
    elif checkBetween(level, 200,209):
        modi = 1
    elif checkBetween(level, 210,219):
        modi = 1.1
    elif checkBetween(level, 220,229):
        modi = 1.15
    elif checkBetween(level, 230,239):
        modi = 1.2
    elif level >= 240:
        modi = 1.25


    return modi * (level **3)


def StarforcePower(starforce):
    l1 = 0
    l2 = 0
    l3 = 0
    l4 = 0

    if checkBetween(starforce, 0, 59):
        l1 = 0.1
        l2 = 15
        l3 = 750
    elif checkBetween(starforce, 60, 119):
        l1 = 0.11
        l2 = 16.5
        l3 = 825
        l4 = 1250
    elif checkBetween(starforce, 120, 179):
        l1 = 0.12
        l2 = 18
        l3 = 900
        l4 = 2500
    elif checkBetween(starforce, 180, 229):
        l1 = 0.13
        l2 = 19.5
        l3 = 975
        l4 = 3750
    elif checkBetween(starforce, 230, 259):
        l1 = 0.14
        l2 = 21
        l3 = 1050
        l4 = 5000
    elif checkBetween(starforce,260, 289):
        l1 = 0.15
        l2 = 22.5
        l3 = 1125
        l4 = 6250
    elif checkBetween(starforce, 290, 319):
        l1 = 0.16
        l2 = 24
        l3 = 1200
        l4 = 7500

    elif checkBetween(starforce, 320, 349):
        l1 = 0.17
        l2 = 25.5
        l3 = 1275
        l4 = 8750
    elif starforce >= 350:
        l1 = 0.18
        l2 = 27
        l3 = 1350
        l4 = 10000

    starforcepower = (l1 * (starforce **3)) + (l2 * (starforce ** 2)) + (l3 * starforce) + l4

    return starforcepower


def checkBetween(number, start, end):
    if number >= start and number <= end:
        return True
    else:
        return False




if __name__ == "__main__":
    Power = main(250, 232)
    print(f'{Power:,}')
    