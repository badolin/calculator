import sys
from os import system


def main():
    print('Welcome to my calculator!')
    menu()

def menu():
    try:
        print('Choose what you want and write right number.')
        print('1.Addition')
        print('2.Subtraction')
        print('3.Multiplication')
        print('4.Division')
        print('5.Close the calculator')
        value = int(input())
        if value == 1:
            system('clear')
            add()
        elif value == 2:
            system('clear')
            subtract()
        elif value == 3:
            system('clear')
            multiply()
        elif value == 4:
            system('clear')
            divide()
        elif value == 5:
            sys.exit()
        else:
            system('clear')
            print('You write wrong number' + str(value))
            menu()
    except ValueError:
        system('clear')
        print('You dont write a number')
        menu()
    except ZeroDivisionError:
        print('You cant write 0')
        menu()

def add():
    print('You chose addition.')
    value1_add = float(input('Write your first number'))
    value2_add = float(input('Write your second number'))
    result_add = value1_add + value2_add
    print('Result= ' + str(result_add))
    menu()

def subtract():
    print('You chose subtraction.')
    value1_subtract = float(input('Write your first number'))
    value2_subtract = float(input('Write your second number'))
    result_subtract= value1_subtract - value2_subtract
    print('Result= ' + str(result_subtract))
    menu()

def multiply():
    print('You chose multiplication.')
    value1_multiply = float(input('Write your first number'))
    value2_multiply = float(input('Write your second number'))
    result_multiply = value1_multiply * value2_multiply
    print('Result= ' + str(result_multiply))
    menu()

def divide():
    print('You chose division.')
    value1_divide = float(input('Write your first number'))
    value2_divide = float(input('Write your second number'))
    result_divide = value1_divide / value2_divide
    print('Result= ' + str(result_divide))
    menu()


if __name__ == '__main__':
    system('clear')
    main()
