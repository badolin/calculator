from os import system

class Calculator:
    memory = None
    last_calculations = None
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
        return value1_multiply * value2_multiply

    @staticmethod
    def divide(value1_divide, value2_divide):
        try:
            return value1_divide / value2_divide
        except ZeroDivisionError:
            print('You cant write 0')

    def print_memory(self):
        system('clear')
        print('Your memory:')
        i = 1
        for x in self.memory:
            print(str(i) + '. ' + str(x))
            i=i+1
    def save_to_memory(self, result):
        self.memory.append(result)

    def print_last_calculations(self):
        system('clear')
        print('Last calculations:')
        for x in self.last_calculations:
            print(x)

    def save_to_last_calculations(self, equation):
        self.last_calculations.append(equation)


########################

def first_number():
    x = input("Write your first number or write Y when you want use result from memory")
    if x == 'Y':
        calculator.print_memory()
        position= int(input("Write which position you want to use"))
        return calculator.memory[position-1]
    else:
        return float(x)

def second_number():
    x = input("Write your second number or write Y when you want use result from memory")
    if x == 'Y':
        calculator.print_memory()
        position= int(input("Write which position you want to use"))
        return calculator.memory[position-1]
    else:
        return float(x)

def print_result(result):
    print(result)
    if input("Write Y if you want save this result on memory") == 'Y':
        calculator.save_to_memory(result)

def menu_add():
    system('clear')
    print('You chose addition.')
    value1_add = first_number()
    value2_add = second_number()
    result = Calculator.add(value1_add, value2_add)
    calculator.save_to_last_calculations(str(value1_add) + '+' + str(value2_add) + '=' + str(result))
    print_result(result)

def menu_subtract():
    system('clear')
    print('You chose subtraction.')
    value1_subtract = first_number()
    value2_subtract = second_number()
    result = Calculator.subtract(value1_subtract, value2_subtract)
    calculator.save_to_last_calculations(str(value1_subtract) + '-' + str(value2_subtract) + '=' + str(result))
    print_result(result)

def menu_multiply():
    system('clear')
    print('You chose multiplication.')
    value1_multiply = first_number()
    value2_multiply = second_number()
    result = Calculator.multiply(value1_multiply, value2_multiply)
    calculator.save_to_last_calculations(str(value1_multiply) + '*' + str(value2_multiply) + '=' + str(result))
    print_result(result)

def menu_divide():
    system('clear')
    print('You chose division.')
    value1_divide = first_number()
    value2_divide = second_number()
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
        try:
            if menu() == "USER_QUIT":
                break
        except ValueError:
            system('clear')
            print('You dont write a number')
            continue

if __name__ == '__main__':
    system('clear')
    calculator = Calculator()
    main()
