def Full_rectangle(n):
    print("Full Triangle")
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


def Increasing_triangle(n):
    print("Increasing Triangle")
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()


def Decreasing_triangle(n):
    print("Decreasing Triangle")
    for i in range(n):
        for j in range(n-i):
            print("*", end=" ")
        print()


def Right_side_triangle(n):
    print("Right Sided Triangle")
    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for k in range(i+1):
            print("*", end=" ")
        print()

def Left_side_triangle(n):
    print("Left Sided Triangle")
    for i in range(n):
        for j in range(i+1):
            print(" ", end = " ")
        for k in range(n-i):
            print("*", end = " ")
        print()


def Hill_Pattern(n):
    print("Hill Pattern")
    for i in range(n):
        for j in range(n-i):
            print(" ", end=" ")
        for k in range(i):
            print("*", end=" ")
        for k in range(i+1):
            print("*", end=" ")
        print()


def Reverse_Hill_Pattern(n):
    print("Reverse Hill Pattern")
    for i in range(n):
        for j in range(i+1):
            print(" ", end=" ")
        for k in range(n-i):
            print("*", end=" ")
        for k in range(i+1, n):
            print("*", end=" ")
        print()


def Diamond_Pattern(n):
    print("Diamond Pattern")
    for i in range(n-1):
        for j in range(n - i):
            print(" ", end=" ")
        for k in range(i):
            print("*", end=" ")
        for k in range(i + 1):
            print("*", end=" ")
        print()
    for i in range(n):
        for j in range(i+1):
            print(" ", end=" ")
        for k in range(n-i):
            print("*", end=" ")
        for k in range(i+1, n):
            print("*", end=" ")
        print()



if __name__ == '__main__':
    n = int(input("Enter number to print: "))
    Full_rectangle(n)
    Increasing_triangle(n)
    Decreasing_triangle(n)
    Right_side_triangle(n)
    Left_side_triangle(n)
    Hill_Pattern(n)
    Reverse_Hill_Pattern(n)
    Diamond_Pattern(n)