def solving_sum(a, b, c):
    total = a + b + c

    if a == b == c:
        return a * b * c
    elif a == c:
        return a * c + b
    elif b == c:
        return b * c + a
    elif a == b:
        return a * b + c
    else:
        return total

print("")
a = eval(input("Enter first number:"))
b = eval(input("Enter second number:"))
c = eval(input("Enter third number:"))

answer = solving_sum(a, b, c)
print("")
print("The answer to the given three numbers will be: ", answer)
