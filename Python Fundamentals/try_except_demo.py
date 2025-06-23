'''
Portofolio Build: Try-Except Demo Script
Created by:
    - Alfriando C Vean
    - Bonifasius Sinurat

This script demonstrates various use cases of Python's try-except block, including:
    - Handling input validation
    - Using else and finally
    - Avoiding bad practice in exception handling   
'''


import os
def clear_terminal(): # Function to clear the terminal screen
    """Clears the terminal screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')
clear_terminal()


# === Basic try-except Example ===
# Demonstrates how to use try-except to catch specific errors in Python

# Example of try-except basic syntax in Python
try:
    # do something
    divide = '8' / 2
# except Exception:
except TypeError:
    # how to handle the error
    print("You can't divide a string by a number!")


# Example of try-except with else and finally clauses 
try:
    # this code might raise an error
    divide = '8' / 2
except TypeError:
    # handle the error by printing a message
    print("You can't divide a string by a number!")
else:
    # if no error occurs
    print("Division successful:", divide)
finally:
    # always executed
    print("This will always be executed, regardless of an error.")
    
# STRENGTH
# Without try-except, the program will crash if an error occurs
'''Uncomment below to test both input scenarios'''
# counter = 0
# while counter < 3:
#     user_input_str = input('Add Counter: ')
#     if int(user_input_str) < 0:
#         print('Input must be a positive number!')
#         continue
    
#     counter += int(user_input_str)
# print('Program finished')


# With try-except, the program will not crash if an error occurs
# It will handle the error gracefully and continue running
counter = 0
while counter < 3:
    try:
        user_input_str = input('Add Counter: ')
        if int(user_input_str) < 0:
            print('Input must be a positive number!')
            continue
        counter += int(user_input_str)
    except ValueError:
        print("That's not a valid number.")
        continue    
print('Program finished')

# WEAKNESS
# without specific exception, we won't know the real error because is excepts all errors
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
    file.close()
except:
    print("Something went wrong.")

# with specific exception, we can specificly catch a kind of error and the message is clearer.
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("The file 'data.txt' was not found. Please check the file name.")
    
    
def divide_numbers(a, b):
    '''Wrap it up in a function to demonstrate try-except with parameters'''
    try:
        result = a / b
    except ZeroDivisionError:
        print("[ZeroDivisionError] Cannot divide by zero.")
    else:
        print("Result is:", result)
    finally:
        print("Operation complete")
divide_numbers(10, 2) # Example of successful division
divide_numbers(10, 0) # Example of division by zero, which will raise an exception