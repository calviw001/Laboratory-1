# lab1.py

# Starter code for lab 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Calvin Wong
# calviw8@uci.edu
# 36522374


def welcome():
    print("Welcome to ICS 32 PyCalc!\n")


def get_first_operand():
    operand_1 = int(input("Enter your first operand: "))
    return operand_1


def get_second_operand():
    operand_2 = int(input("Enter your second operand: "))
    return operand_2


def get_operator():
    operator = input("Enter your desried operator (+, -, or x): ")
    return operator


def calc_result():
    result = 0
    first_operand = get_first_operand()
    second_operand = get_second_operand()
    desried_operator = get_operator()
    if desried_operator == 'x':
        result = first_operand * second_operand
    elif desried_operator == '-':
        result = first_operand - second_operand
    elif desried_operator == '+':
        result = first_operand + second_operand
    return result


def display_result(result):
    print(f"\nThe result of your calculation is: {result}")


def main():
    welcome()
    end_result = calc_result()
    display_result(end_result)


main()
