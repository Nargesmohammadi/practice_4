import math

math.log(10.0)


def printThird(bird):
    print(bird, bird, bird)


printThird('Cold')


def newLine():
    print()


def printParity(y):
    if y % 3 == 0:
        print("You Win")
    else:
        print("You loss")


printParity(30)


def printCompare(x, y):
    if x < y:
        print('x, "is less than", y')
    elif x > y:
        print('x, "is greater than", y')
    else:
        print('x, "and", y, "are equal"')


printCompare(5, 19)


def printDispatch(part1, part2):
    number1 = math.cos(math.pi / 6)
    number2 = math.sin(math.pi / 3)
    if number1 != number2:
        return
    if number1 < 0.2:
        print("Failed")

    else:
        print("You win")



