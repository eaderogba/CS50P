def main():
    # Prommpt user for input
    expression = input("Enter an arithmetic expression: ")

    # Input is split into three variable: x, y, z; y variable takes the operator
    x, y, z = expression.split(" ")

    # x and y is converted to integer
    x = int(x)
    z = int(z)

    result = calculate_input(x, y, z)

    # Print the result formatted to one decimal place
    print(f"Result: {result:.1f}")


def calculate_input(x, y, z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z
    else:
        print("Can't perform such expressions")


main()
