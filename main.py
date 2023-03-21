import math


def intro():
    print("WELCOME TO THE FIB SEQUENCE!")
    print("Please enter a positive int: ")
    try:
        A = int(input())
        if A >= 0:
            if A > 20:
                print("Larger values may take longer to calculate, please wait...\n")
            fib1 = fib_recursion(A)
            fib2 = fib_equation(A)
            print("fib1 (recursion) = " + str(fib1))
            print("fib2 (equation) = " + str(fib2))
            ##intro()
        else:
            print("ERROR: Please enter a positive int!\n")
            intro()
    except ValueError:
        print("ERROR: That was not a int, try again!\n")
        intro()

def fib_recursion(n): ##first few numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        sum = (fib_recursion(n-1) + fib_recursion(n-2))
        return sum


def fib_equation(n): ##Fn = 1/Sqrt of 5 * (1 + sqrt5 / 2) ^ n - 1/sqrt of 5 * (1 - sqrt5 / 2) ^ n
    ##c1 * A + c2 * b
    c1 = 1/math.sqrt(5)
    A = ((1 + math.sqrt(5)) / 2) ** n
    c2 = 1/math.sqrt(5) ### put - in final
    B = ((1 - math.sqrt(5)) / 2) ** n
    Fn = c1 * A - c2 * B
    return round(Fn)

intro()