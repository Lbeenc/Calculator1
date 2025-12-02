from decimal import Decimal


output_history = []





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
    elif com == "history":
        print(output_history)
    elif com == "exit":
        return
    else:
        print('that is not a valid input')
    ui()



def add():
    x = input('enter first number')
    y = input('enter second number')
    try:
        print(Decimal(x) + Decimal(y))
        output_history.append(Decimal(x) + Decimal(y))
    except:
        print('that is not a valid number')


def sub():
    x = input('enter first number')
    y = input('enter second number')
    try:
        print(Decimal(x) - Decimal(y))
        output_history.append(Decimal(x) - Decimal(y))

    except:
        print('that is not a valid number')

def mul():
    x = input('enter first number')
    y = input('enter second number')
    try:
        print(Decimal(x) * Decimal(y))
        output_history.append(Decimal(x) * Decimal(y))
    except:
        print('that is not a valid number')
def div():
    x = input('enter first number')
    y = input('enter second number')
    try:
        print(Decimal(x) /Decimal(y))
        output_history.append(Decimal(x) / Decimal(y))
    except:
        print('that is not a valid number')
print('Welcome to Calculator\n')

print('you can add subtract , multiply, and divide.\n')
print('enter "Add" to add numbers.')
print('enter "Subtract" to subtract numbers.')
print('enter "Multiply" to multiply numbers.')
print('enter "Divide" to divide numbers.')
print('enter "History" to show history.')
print('enter "Exit" to exit the program.')

ui()
