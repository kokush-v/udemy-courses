def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return  n1 * n2

def divide(n1, n2):
    return  n1 / n2

def make_calculation(operation_symbol, n1, n2):
    return operation_dict[operation_symbol](n1, n2)

result = 0
continue_calculation = "n"
operation_dict = {"+": add,
                  "-": subtract,
                  "*": multiply,
                  "/": divide}




while True:
    x1 = 0
    if continue_calculation == "n":
        result = 0
        x1 = float(input("Write first number\n"))
    else:
        x1 = result

    operation = input("Select operation:\n" + "".join([f"{key}\n" for key in operation_dict]))
    x2 = float(input("Write second number\n"))
    result = make_calculation(operation, x1, x2)
    continue_calculation = input(
        f"{x1} {operation} {x2} = {result}" + f"\nDo you want continue with last result {result}. y/n")


