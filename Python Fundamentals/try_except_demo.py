"""
Portofolio Build: Try-Except Demo Script
Created by:
    - Alfriando C Vean
    - Bonifasius Sinurat

This script demonstrates various use cases of Python's try-except block, including:
    - Handling input validation
    - Using else and finally
    - Avoiding bad practice in exception handling
"""

# ==== CASE 1: Basic try-except ====

def basic_try_except_example():
    """Demonstrates TypeError handling with string-number division"""
    try:
        divide = '8' / 2
    except TypeError:
        print("[TypeError] You can't divide a string by a number!")

# ==== CASE 2: With else and finally ====

def try_except_else_finally_example():
    """Demonstrates else and finally behavior"""
    try:
        divide = 8 / 2
    except TypeError:
        print("[TypeError] Something went wrong with division.")
    else:
        print("[Success] Division successful:", divide)
    finally:
        print("[Finally] This block always runs.")

# ==== CASE 3: Input Handling Without try-except ====

def input_loop_without_exception():
    """Program crashes if input is not a valid integer"""
    print("\n[Without Try-Except] Program may crash with invalid input")
    counter = 0
    while counter < 3:
        user_input_str = input('Add Counter: ')
        if int(user_input_str) < 0:
            print('Input must be a positive number!')
            continue
        counter += int(user_input_str)
    print('Program finished\n')

# ==== CASE 4: Input Handling With try-except ====

def input_loop_with_exception():
    """Safely handles input using try-except to avoid crashing"""
    print("[With Try-Except] Handling input gracefully")
    counter = 0
    while counter < 3:
        try:
            user_input_str = input('Add Counter: ')
            if int(user_input_str) < 0:
                print('Input must be a positive number!')
                continue
            counter += int(user_input_str)
        except ValueError:
            print("[ValueError] That's not a valid number.")
            continue    
    print('Program finished\n')

# ==== CASE 5: Bad Practice – Catching All Exceptions ====

def catch_all_example():
    """Example of bad practice: using a general except"""
    try:
        file = open("data.txt", "r")
        content = file.read()
        print(content)
        file.close()
    except:
        print("[General Except] Something went wrong (but unclear what).")

# ==== CASE 6: Good Practice – Specific Exception ====

def specific_exception_example():
    """Catching a specific FileNotFoundError with a clear message"""
    try:
        file = open("data.txt", "r")
        content = file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        print("[FileNotFoundError] 'data.txt' not found. Please check the filename.")

# ==== CASE 7: Function with division logic ====

def divide_numbers(a, b):
    """Divides two numbers and demonstrates try-except-else-finally structure"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("[ZeroDivisionError] Cannot divide by zero.")
    else:
        print("Result is:", result)
    finally:
        print("Operation complete")

# ==== MAIN RUN ====

if __name__ == "__main__":
    basic_try_except_example()
    try_except_else_finally_example()

    # Uncomment below to test both input scenarios
    # input_loop_without_exception()  # ← will crash if invalid input
    input_loop_with_exception()    # ← handles invalid input

    catch_all_example()
    specific_exception_example()

    divide_numbers(10, 2)
    divide_numbers(10, 0)
