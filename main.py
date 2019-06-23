#!/usr/bin/env python
import sys, os
import pyfiglet
from pyfiglet import Figlet

def menu():
    main_font = Figlet(font="poison")
    banner = main_font.renderText("Weeb - Sec")
    print(banner)

def selections():
    exit()

def main():
    menu()
    test = input("")

main()
