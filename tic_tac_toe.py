a = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
count = 0


def printTicTocToe():
    for i in a:
        for k in i:
            print(str(k)+" ", end="")
        print("\n")


def isEmpty():
    for i in a:
        for k in i:
            if k == -1:
                return True
    return False


def isValidCheck(x, y):
    if (x <= 2 and y <= 2 and a[x][y] == -1):
        return True
    else:
        return False


def checkLeftRight(x, z):
    for y in range(3):
        if(a[x][y] != z):

            return False

    return True


def checkUpDown(y, z):
    for x in range(3):
        if(a[x][y] != z):
            return False

    return True


def checkDiagonal(x, y, z):
    if (x == 1 and y == 1) or (x == 0 and y == 2) or (x == 2 and y == 0) or (x == 0 and y == 0) or (x == 2 and y == 2):
        if(a[1][1] == z and a[0][2] == z and a[2][0] == z):
            return True
        elif(a[1][1] == z and a[0][0] == z and a[2][2] == z):
            return True
        else:
            return False


while (isEmpty()):
    count += 1
    printTicTocToe()
    print("Enter Comma seperated coordinants For placing your move")

    x, y = input().split()

    x = int(x)
    y = int(y)
    if (isValidCheck(x, y)):
        if(count % 2 == 0):
            z = 0
            a[x][y] = z
        else:
            z = 1
            a[x][y] = z

        if(checkLeftRight(x, z) or checkUpDown(y, z) or checkDiagonal(x, y, z)):
            printTicTocToe()
            print("Congratulations u win this game.")
            break

    else:
        count -= 1
        print("Invalid co-ordinates!")

else:
    print("No space left")
