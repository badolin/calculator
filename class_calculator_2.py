from os import system

class Calculator:

    @staticmethod
    def add(value1_add, value2_add):
        return value1_add + value2_add

    @staticmethod
    def subtract(value1_subtract, value2_subtract):
        return value1_subtract - value2_subtract

    @staticmethod
    def multiply(value1_multiply, value2_multiply):
        return value1_multiply * value2_multiply

    @staticmethod
    def divide(value1_divide, value2_divide):
        return value1_divide / value2_divide


def menu_add():
    system('clear')
    print('You chose addition.')
    value1_add = float(input('Write your first number'))
    value2_add = float(input('Write your second number'))
    print(Calculator.add(value1_add, value2_add))

def menu_subtract():
    system('clear')
    print('You chose subtraction.')
    value1_subtract = float(input('Write your first number'))
    value2_subtract = float(input('Write your second number'))
    print(Calculator.subtract(value1_subtract, value2_subtract))

def menu_multiply():
    system('clear')
    print('You chose multiplication.')
    value1_multiply = float(input('Write your first number'))
    value2_multiply = float(input('Write your second number'))
    print(Calculator.multiply(value1_multiply, value2_multiply))

def menu_divide():
    system('clear')
    print('You chose division.')
    value1_divide = float(input('Write your first number'))
    value2_divide = float(input('Write your second number'))
    print(Calculator.divide(value1_divide, value2_divide))

def menu():
    print('Choose what you want and write right number.')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    print('5.Close the calculator')
    value = int(input())
    if value == 1:
        menu_add()
    elif value == 2:
        menu_subtract()
    elif value == 3:
        menu_multiply()
    elif value == 4:
        menu_divide()
    elif value == 5:
        return
    else:
        system('clear')
        print('You write wrong number' + str(value))

def main():
    print('Welcome to my calculator!')
    n=0
    while n<3:
        try:
            menu()
            n=n+1
        except ValueError:
            system('clear')
            print('You dont write a number')
            n=n+1
            continue
        except ZeroDivisionError:
            print('You cant write 0')
            n=n+1
            continue


if __name__ == '__main__':
    system('clear')
    main()
