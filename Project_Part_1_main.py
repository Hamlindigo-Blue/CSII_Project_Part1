from Project_Part_1_gui import *


def main():
    """
    - Change the window title to 'Lab 10'.
    - Set its length to 250 and height to 180.
    - Make the window non-resizable.
    """
    window = Tk()
    window.title('Project Part 1')
    window.geometry('500x150')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()



if __name__ == '__main__':
    main()