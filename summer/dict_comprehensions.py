"""
Example of how to instance a new dictionary with given values. In this
case, we create a dict with the first 100 natural numbers as key and
its value when they are powered to three. We use the following syntax:
{key:value for value in iterable if condition}
"""

def main():

    # BORING WAY
    # my_dict = {}
    # for i in range(1, 101):
    #     if i % 3 !=0:
    #         my_dict[i] = i**2
    # print(my_dict)

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)


if __name__ == "__main__":
    main()