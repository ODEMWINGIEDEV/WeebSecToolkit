#!/usr/bin/env python
import sys, os
import pyfiglet
from pyfiglet import Figlet

def menu():
    valid_input = False
    while True:
        print("\n TOOLS")
        print("=======")
        tools = ["autism", "dead"]
        for i in range(len(tools)):
            print(str(i+1)+ ") " + tools[i])
            
        try:
            selection = int(input("\n\nPlease select the # of the " \
                            + "tool that you would like to use\n    "))
            if selection >= len(tools)+1 or selection <= 0:
                print("\nERROR: Invalid tool #\n\n")
                valid_input = False
            else:
                valid_input = True
        except ValueError:
            print("\nERROR: Numeric values only\n\n")
        if valid_input == True:
            break
            


    print("\nyou did it retard")

def main():
    main_font = Figlet(font="banner3") #Setup ASCII font
    banner = main_font.renderText("Weeb | Sec") #Create banner
    print(banner)

    selection = menu()
    
    

main()
