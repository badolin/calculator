import sys
from os import system

class Calculator:
    def add(self, value1_add, value2_add):
        result_add = value1_add + value2_add
        print('Your Result =' + str(result_add))

    def subtract(self, value1_subtract, value2_subtract):
        result_subtract = value1_subtract + value2_subtract
        print('Your Result =' + str(result_subtract))

    def multiply(self, value1_multiply, value2_multiply):
        result_multiply = value1_multiply + value2_multiply
        print('Your Result =' + str(result_multiply))

    def divide(self, value1_divide, value2_divide):
        result_divide = value1_divide + value2_divide
        print('Your Result =' + str(result_divide))

def main():
    cal = Calculator()
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
            value1_add = float(input('Write your first number'))
            value2_add = float(input('Write your second number'))
            cal.add(value1_add, value2_add)
        elif value == 2:
            system('clear')
            value1_subtract = float(input('Write your first number'))
            value2_subtract = float(input('Write your second number'))
            cal.subtract(value1_subtract, value2_subtract)
        elif value == 3:
            system('clear')
            value1_multiply = float(input('Write your first number'))
            value2_multiply = float(input('Write your second number'))
            cal.multiply(value1_multiply, value2_multiply)
        elif value == 4:
            system('clear')
            value1_divide = float(input('Write your first number'))
            value2_divide = float(input('Write your second number'))
            cal.divide(value1_divide, value2_divide)
        elif value == 5:
            sys.exit()
        else:
            system('clear')
            print('You write wrong number' + str(value))
            main()
    except ValueError:
        system('clear')
        print('You dont write a number')
        main()
    except ZeroDivisionError:
        print('You cant write 0')
        main()
    main()
if __name__ == '__main__':
    print('Welcome to my calculator!')
    main()
