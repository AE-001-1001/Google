# Main App File
import os
from time import strftime
from BackEnd import App

# create a function that cleans the console window

# create a function that creates a new window

def main():
    os.system('cls')
    current_time = strftime("%H:%M:%S")
    App.new_window("Main Window {}".format(current_time))
    return
        

if __name__ == '__main__':
    main()
    