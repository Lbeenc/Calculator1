#for allowing decimal points
from decimal import Decimal

last_output = []
output_history = []
clean_history= []
Output = [0]



#basic ui functions
def ui():
    com = input('what would you like to do?').lower()
    if com == "add":
        add()
    elif com == "subtract":
        sub()
    elif com == "multiply":
        mul()
    elif com == "divide":
        div()
    elif com == "power":
        pow()
    elif com == "root":
        root()

    elif com == "history":
        phrase = 'Decimal'
        print(output_history)
        clean_history = (str(output_history).replace(phrase,""))
        print(clean_history)
        print('last output:', Output[0])

    elif com == "save":
        save()
    elif com == "exit":
        return
    else:
        print('that is not a valid input')
    ui()


#math functions
def add():
    x = input('enter first number')
    y = input('enter second number')
    try:
        output =  Decimal(x) + Decimal(y)
        print(output)
        output_history.append(output)
        Output[0] = output
    except:
        print('that is not a valid number')


def sub():
    x = input('enter first number')
    y = input('enter second number')
    try:
        output = Decimal(x) - Decimal(y)
        print(output)
        output_history.append(output)
        Output[0] = output

    except:
        print('that is not a valid number')

def mul():
    x = input('enter first number')
    y = input('enter second number')
    try:
        output = Decimal(x) * Decimal(y)
        print(output)
        output_history.append(output)
        Output[0] = output
    except:
        print('that is not a valid number')
def div():
    x = input('enter first number')
    y = input('enter second number')
    try:
        output = Decimal(x) /Decimal(y)
        print(output)
        output_history.append(output)
        Output[0] = output
    except:
        print('that is not a valid number')

def pow():
    x = input('enter first number')
    y = input('enter second number (exponent)')
    try:
        output = Decimal(x) ** Decimal(y)
        print(output)
        output_history.append(output)
        Output[0] = output
    except:
        print('that is not a valid number')

def root():
    x = input('enter number to find the square root of')
    try:
        output = Decimal(x) ** 0.5
        print(output)
        Output[0] = output

    except:
        print('that is not a valid number')

#saving to log file function
def save():
    print('saved output history to file')
    with open('calc_output.txt', 'a') as f:
        f.write('log' + str(output_history) + '\n')



print('Welcome to Calculator\n')

print('you can add subtract , multiply, and divide.\n')
print('enter "Add" to add numbers.')
print('enter "Subtract" to subtract numbers.')
print('enter "Multiply" to multiply numbers.')
print('enter "Divide" to divide numbers.')
print('enter "Power" to raise to the power of numbers.')
print('enter "Root" to take the root of the number.')
print('enter "History" to show history.')
print('enter "Save" to save output history.')
print('enter "Exit" to exit the program.')

ui()

