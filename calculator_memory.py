from os import system

class Calculator:
    def __init__(self):
        self.memory = []
        self.last_calculations = []
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

    def print_memory(self):
        system('clear')
        print('Your memory:')
        for count, item in enumerate(self.memory, 1):
            print(count, item)

    def save_to_memory(self, result):
        self.memory.append(result)

    def print_last_calculations(self):
        system('clear')
        print('Last calculations:')
        for count, item in enumerate(self.last_calculations, 1):
            print(count, item)

    def save_to_last_calculations(self, equation):
        self.last_calculations.append(equation)


########################

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

def menu():
    print('Choose what you want and write right number.')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    print('5.Close the calculator')
    print('6.Print memory')
    print('7.Print last calculations')
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
        return "USER_QUIT"
    elif value == 6:
        calculator.print_memory()
    elif value == 7:
        calculator.print_last_calculations()
    else:
        system('clear')
        print('You write wrong number' + str(value))

def main():
    print('Welcome to my calculator!')
    while True:
        if menu() == "USER_QUIT":
            break

if __name__ == '__main__':
    system('clear')
    calculator = Calculator()
    main()
