from os import system
import sys
import json

class Calculator:
    def __init__(self):
        try:
            with open("memory.txt", "r") as file:
                self.memory= json.load(file)
        except FileNotFoundError:
            with open("memory.txt", "w") as file:
                self.memory = []
                json.dump(self.memory , file)
        try:
            with open("last_calculations.txt", "r") as file:
                self.last_calculations= json.load(file)
        except FileNotFoundError:
            with open("last_calculations.txt", "w") as file:
                self.last_calculations = []
                json.dump(self.last_calculations , file)

    @staticmethod
    def add(value1_add, value2_add):
        return value1_add + value2_add

    @staticmethod
    def subtract(value1_subtract, value2_subtract):
        return value1_subtract - value2_subtract

    @staticmethod
    def multiply(value1_multiply, value2_multiply):
        try:
            return value1_multiply * value2_multiply
        except TypeError:
            print(value1_multiply)
            print(value2_multiply)

    @staticmethod
    def divide(value1_divide, value2_divide):
        try:
            return value1_divide / value2_divide
        except ZeroDivisionError:
            print('You cant write 0')

    @staticmethod
    def power(value1_power, value2_power):
        return value1_power**value2_power

    @staticmethod
    def root(value1_root, value2_root):
        return value1_root**(1/value2_root)

    def print_memory(self):
        system('clear')
        print('Your memory:')
        for count, item in enumerate(self.memory, 1):
            print(count, item)

    def save_to_memory(self, result):
        self.memory.append(result)
        with open("memory.txt", "w") as file:
            json.dump(self.memory, file)

    def print_last_calculations(self):
        system('clear')
        print('Last calculations:')
        for count, item in enumerate(self.last_calculations, 1):
            print(count, item)

    def save_to_last_calculations(self, equation):
        self.last_calculations.append(equation)
        with open("last_calculations.txt", "w") as file:
            json.dump(self.last_calculations, file)


################################################
################################################
################################################

def input_index_memory():
    calculator.print_memory()
    try:
        position= int(input("Write which position you want to use"))
        return calculator.memory[position-1]
    except:
        print('You dont write a good number')
        return None


def input_float_or_Y(text):
    x = input(text)
    if x == 'Y':
        return input_index_memory()
    else:
        try:
            return float(x)
        except:
            print('You dont write a number')
            return None

def print_result(result):
    print(result)
    if input("Write Y if you want save this result on memory") == 'Y':
        calculator.save_to_memory(result)

################################################
################################################
################################################

def menu_add():
    system('clear')
    print('You chose addition.')
    value1_add = None
    value2_add = None
    while value1_add == None:
        value1_add = input_float_or_Y("Write your first number or write Y when you want use result from memory")
    while value2_add == None:
        value2_add = input_float_or_Y("Write your second number or write Y when you want use result from memory")
    result = Calculator.add(value1_add, value2_add)
    calculator.save_to_last_calculations(str(value1_add) + '+' + str(value2_add) + '=' + str(result))
    print_result(result)

def menu_subtract():
    system('clear')
    print('You chose subtraction.')
    value1_subtract = None
    value2_subtract = None
    while value1_subtract == None:
        value1_subtract = input_float_or_Y("Write your first number or write Y when you want use result from memory")
    while value2_subtract == None:
        value2_subtract = input_float_or_Y("Write your second number or write Y when you want use result from memory")

    result = Calculator.subtract(value1_subtract, value2_subtract)
    calculator.save_to_last_calculations(str(value1_subtract) + '-' + str(value2_subtract) + '=' + str(result))
    print_result(result)

def menu_multiply():
    system('clear')
    print('You chose multiplication.')
    value1_multiply = None
    value2_multiply = None
    while value1_multiply == None:
        value1_multiply = input_float_or_Y("Write your first number or write Y when you want use result from memory")
    while value2_multiply == None:
        value2_multiply = input_float_or_Y("Write your second number or write Y when you want use result from memory")
    result = Calculator.multiply(value1_multiply, value2_multiply)
    calculator.save_to_last_calculations(str(value1_multiply) + '*' + str(value2_multiply) + '=' + str(result))
    print_result(result)

def menu_divide():
    system('clear')
    print('You chose division.')
    value1_divide = None
    value2_divide = None
    while value1_divide == None:
        value1_divide = input_float_or_Y("Write your first number or write Y when you want use result from memory")
    while value2_divide == None:
        value2_divide = input_float_or_Y("Write your second number or write Y when you want use result from memory")
    result = Calculator.divide(value1_divide, value2_divide)
    calculator.save_to_last_calculations(str(value1_divide) + '/' + str(value2_divide) + '=' + str(result))
    print_result(result)

def menu_power():
    system('clear')
    print('You chose raising to a power.')
    value1_power = None
    value2_power = None
    while value1_power == None:
        value1_power = input_float_or_Y("Write your first number or write Y when you want use result from memory")
    while value2_power == None:
        value2_power = input_float_or_Y("Write your second number or write Y when you want use result from memory")
    result = Calculator.power(value1_power, value2_power)
    calculator.save_to_last_calculations(str(value1_power) + '+' + str(value2_power) + '=' + str(result))
    print_result(result)

def menu_root():
    system('clear')
    print('You chose root.')
    value1_root = None
    value2_root = None
    while value1_root == None:
        value1_root = input_float_or_Y("Write your first number or write Y when you want use result from memory")
    while value2_root == None:
        value2_root = input_float_or_Y("Write your second number or write Y when you want use result from memory")
    result = Calculator.root(value1_root, value2_root)
    calculator.save_to_last_calculations(str(value1_root) + '+' + str(value2_root) + '=' + str(result))
    print_result(result)

def menu():
    print('Choose what you want and write right number.')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    print('5.Raising to a power')
    print('6.Root')
    print('7.Print last calculations')
    print('8.Print memory')
    print('9.Close the calculator')
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
        menu_power()
    elif value == 6:
        menu_root()
    elif value == 7:
        calculator.print_last_calculations()
    elif value == 8:
        calculator.print_memory()
    elif value == 9:
        return "USER_QUIT"
    else:
        system('clear')
        print('You write wrong number' + str(value))

################################################
################################################
################################################

def console_add(x, y):
    result = Calculator.add(x, y)
    calculator.save_to_last_calculations(str(x) + '+' + str(y) + '=' + str(result))
    print_result(result)

def console_subtract(x, y):
    result = Calculator.subtract(x, y)
    calculator.save_to_last_calculations(str(x) + '-' + str(y) + '=' + str(result))
    print_result(result)

def console_multiply(x, y):
    result = Calculator.multiply(x, y)
    calculator.save_to_last_calculations(str(x) + '*' + str(y) + '=' + str(result))
    print_result(result)

def console_divide(x, y):
    result = Calculator.divide(x, y)
    calculator.save_to_last_calculations(str(x) + '/' + str(y) + '=' + str(result))
    print_result(result)

def console_power(x, y):
    result = Calculator.power(x, y)
    calculator.save_to_last_calculations(str(x) + '+' + str(y) + '=' + str(result))
    print_result(result)

def console_root(x, y):
    result = Calculator.root(x, y)
    calculator.save_to_last_calculations(str(x) + '+' + str(y) + '=' + str(result))
    print_result(result)

def console_menu():
    if len(argumentList) == 3:
        name_function = str(argumentList[0])
        try:
            first_value = float(argumentList[1])
            second_value = float(argumentList[2])
        except ValueError:
            print("You write the wrong arguments")
            print("Fisrt argument must be one of them:")
            print("--add --subtract --multiply --divide --power --root")
            print("the next two must be numbers")
            print("for example: bulbulator.py --power 3.2 5.1")
            return
        if name_function == '--add':
            console_add(first_value, second_value)
        if name_function == '--subtract':
            console_subtract(first_value, second_value)
        if name_function == '--multiply':
            console_multiply(first_value, second_value)
        if name_function == '--divide':
            console_divide(first_value, second_value)
        if name_function == '--power':
            console_power(first_value, second_value)
        if name_function == '--root':
            console_root(first_value, second_value)

    else:
        print("You write the wrong number of arguments")
        print("Fisrt argument must be one of them:")
        print("--add --subtract --multiply --divide --power --root")
        print("the next two must be numbers")
        print("for example: bulbulator.py --power 3.2 5.1")

################################################
################################################
################################################

def main():
    print('Welcome to my calculator!')
    while True:
        if menu() == "USER_QUIT":
            break

if __name__ == '__main__':
    calculator = Calculator()
    argumentList = sys.argv[1:]
    if len(argumentList) >= 1:
        console_menu()
    else:
        system('clear')
        main()
