from socket import socket



"""
This function returns a list of the multiples of four between 1 and 9999
We use this as an example of the use of list comprehensions
[element for element in iterable if condition]
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
"""
def CreateList():
    multiples_of_four = [i for i in range(1, 10000) if i % 4 == 0]
    return multiples_of_four

def main():
    print(CreateList())

if __name__ == "__main__":
    main()