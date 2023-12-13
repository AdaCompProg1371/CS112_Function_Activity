def number():

    for i in range(0, a_1):


        for j in range(0, b_2):


            for k in range(0, c_3):

                result = 0

            return result


def a_1():
    a_1 = eval(input("Enter first number:"))


def b_2():
    b_2 = eval(input("Enter second number:"))


def c_3():
    c_3 = eval(input("Enter third number:"))


def answer():
    if a_1 != b_2 and b_2 != c_3:
        formula = a_1 + b_2 + c_3
    elif a_1 == b_2 and a_1 != c_3:
        formula = a_1 * b_2 + c_3
    elif a_1 != b_2 and a_1 == c_3:
        formula = a_1 + b_2 * c_3
    elif b_2 == c_3 and a_1 != c_3:
        formula = a_1 + b_2 * c_3
    elif b_2 != c_3 and a_1 == c_3:
        formula = a_1 * c_3 + b_2
    else:
        formula = a_1 * b_2 * c_3


def main():

    a_1 = eval(input("Enter first number:"))

    b_2 = eval(input("Enter second number:"))

    c_3 = eval(input("Enter third number:"))


main()
a_1()
b_2()
c_3()
answer()
number()

# Type three numbers
a_1 = eval(input("Enter first number:"))
b_2 = eval(input("Enter second number:"))
c_3 = eval(input("Enter third number:"))

# Answers based on the typed numbers
print("The answer for the given numbers is:", answer)