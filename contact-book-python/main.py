from options import option_print
from option_handler import option_handler

while True: 
    option_print()
    
    choice = input("Enter your choice: ")

    if option_handler(choice):
        break


