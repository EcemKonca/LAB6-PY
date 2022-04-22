x = lambda n: (n - 3) / n ** 2
number = int(input("Enter the number: "))
List = []
for i in range(1, number + 1, 1):
    List.append(x(i))
print("Your result is:", sum(List))


def function1(n):
    """This function calculates product recursively"""
    if n == 0:
        return 1
    else:
        return (n / (n + 2) - 10) * function1(n - 1)


number2 = int(input("Enter the number: "))
print("Your result is:", function1(number2))
print(function1.__doc__)
