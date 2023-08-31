from enum import Enum
import logging
import os

logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('calculator.log')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

class Operation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    QUIT = 5

def clean_screen():
    os.system('cls')

def add(x, y):
    clean_screen()
    return x + y

def subtract(x, y):
    clean_screen()
    return x - y

def multiply(x, y):
    clean_screen()
    return x * y

def divide(x, y):
    clean_screen()
    if y != 0:
        return x / y
    else:
        logger.warning("Cannot divide by zero: %s")
        return "Cannot divide by zero"
        
def menu():
    clean_screen()
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter choice (1/2/3/4/5): ")

        try:
            choice = int(choice)
            operation = Operation(choice)

            if operation == Operation.QUIT:
                logger.info("Calculator has been closed. %s")
                print("Calculator has been closed.")
                break

            if operation in (Operation.ADD, Operation.SUBTRACT, Operation.MULTIPLY, Operation.DIVIDE):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if operation == Operation.ADD:
                    print("Result:", add(num1, num2))
                elif operation == Operation.SUBTRACT:
                    print("Result:", subtract(num1, num2))
                elif operation == Operation.MULTIPLY:
                    print("Result:", multiply(num1, num2))
                elif operation == Operation.DIVIDE:
                    print("Result:", divide(num1, num2))
            else:
                logger.error("Invalid input %s")
                print("Invalid input")
                
        except ValueError:
            logger.error("Invalid input %s")
            print("Invalid input")
            
if __name__ == "__main__":
    clean_screen()
    menu()
