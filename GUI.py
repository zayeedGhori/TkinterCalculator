'''
This program is made for the Developing Software for Planet Zorboin module in the 
Learning At Home program from the elearningontario website: 
https://lah.elearningontario.ca/CMS/public/exported_courses/ICS3U/exported/ICS3UU03/ICS3UU03/ICS3UU03A02/_content.html

This program takes spare change from the user and outputs the least number of coins needed to give
in alien currency.

'''

import math
from tkinter import Tk, Button, Label, Frame, Entry, Toplevel, END, E, W
from PIL import Image, ImageTk


# Calculates the least number of coins
class Calculations:

    def __init__(self, initialNumOfVrobits):
        self.vrobitsInit = initialNumOfVrobits # Change later


    # Calculates coin numbers from the biggest value to the smallest value coin
    # via integer division and modulo
    def getNumCoins(self):
        numDrobzits = int(math.floor(self.vrobitsInit / 100000))
        vrobitsRemain = self.vrobitsInit % 100000

        numClickwicks = int(vrobitsRemain / 50000)
        vrobitsRemain = vrobitsRemain % 50000

        numGazoontight = int(vrobitsRemain / 10000)
        vrobitsRemain = vrobitsRemain % 10000

        numFrazoints = int(vrobitsRemain / 1000)
        vrobitsRemain = vrobitsRemain % 1000

        numBlointoints = int(vrobitsRemain / 500)
        vrobitsRemain = vrobitsRemain % 500

        # returns the coin numbers
        return (
            numDrobzits,\
            numClickwicks,\
            numGazoontight,\
            numFrazoints,\
            numBlointoints,\
            vrobitsRemain
        )

# This class handles the input and output to the user
class GUI:

    def __init__(self, window):
        # Main window
        self.master = window
        window.title("ZirboinFinancial Coin Calculator")
        window.geometry('500x300')
        window.resizable(False, False)

        # Error
        self.bErrorVisible = False

        # Bank label
        self.corpLabel = Frame(master=window)

        image = Image.open('ZirboinFinancial.jpeg')
        photo = ImageTk.PhotoImage(image)
        icon = Label(master=self.corpLabel, image=photo, width=30, height=30)
        icon.image = photo
        icon.grid(row=0, column=0)

        corpTxt = Label(master=self.corpLabel, text='ZirboinFinancial')
        corpTxt.grid(row=0, column=1)
        
        self.corpLabel.grid(
            row = 0,
            column = 0,
            columnspan=2,
            pady = 20,
            padx = window.winfo_width()/2 + 10
        )
        
        # Quit Button
        self.closeButton = Button(master=window, text='Close', command=window.quit)
        self.closeButton.grid(
            row=8,
            column=1,
            columnspan=2,
            pady = 20,
            padx = window.winfo_width()/2 + 10
        )


        # # Vrobit input
        # Text
        self.inputText = Label(master=window, text='Vrobit Change:')
        self.inputText.grid(row=1, column=0, sticky=E)

        # Box
        self.inputBox = Entry(master=window, width=50)
        self.inputBox.delete(0, END)
        self.inputBox.insert(0, 'Enter the amount of vrobit change to be converted')

        self.inputBox.grid(row=1, column=1)

        # Button
        self.inputBut = Button(master=window, text='Enter', command=self.displayCoinOutput)
        self.inputBut.grid(row=1, column=2)

        # # # Coin Boxes

        # # Drobits

        # Text
        self.drobitText = Label(master=window, text='Number of Drobits:')
        self.drobitText.grid(row=2, column=0, sticky=E)

        # Box
        self.drobitBox = Entry(master=window, width=50)
        self.drobitBox.delete(0, END)

        self.drobitBox.grid(row=2, column=1)

        
        # # Clickwicks

        # Text
        self.clickwickText = Label(master=window, text='Number of Clickwicks:')
        self.clickwickText.grid(row=3, column=0, sticky=E)

        # Box
        self.clickwickBox = Entry(master=window, width=50)
        self.clickwickBox.delete(0, END)

        self.clickwickBox.grid(row=3, column=1)

                
        # # Gazoontights

        # Text
        self.gazoonText = Label(master=window, text='Number of Gazoontights:')
        self.gazoonText.grid(row=4, column=0, sticky=E)

        # Box
        self.gazoonBox = Entry(master=window, width=50)
        self.gazoonBox.delete(0, END)

        self.gazoonBox.grid(row=4, column=1)

        
        # # Frazoints

        # Text
        self.frazText = Label(master=window, text='Number of Frazoints:')
        self.frazText.grid(row=5, column=0, sticky=E)

        # Box
        self.frazBox = Entry(master=window, width=50)
        self.frazBox.delete(0, END)

        self.frazBox.grid(row=5, column=1)

        # # Blointoints

        # Text
        self.bloinText = Label(master=window, text='Number of Blointoints:')
        self.bloinText.grid(row=6, column=0, sticky=E)

        # Box
        self.bloinBox = Entry(master=window, width=50)
        self.bloinBox.delete(0, END)

        self.bloinBox.grid(row=6, column=1)

        # # Remaining Vrobits

        # Text
        self.vrobitText = Label(master=window, text='Number of Vrobits:')
        self.vrobitText.grid(row=7, column=0, sticky=E)

        # Box
        self.vrobitBox = Entry(master=window, width=50)
        self.vrobitBox.delete(0, END)

        self.vrobitBox.grid(row=7, column=1)






    # gets input from the user and error handles by repeatedly asking the user
    def getNumVrobits(self):
        try:
            vrobits = int(self.inputBox.get())

            return vrobits
        
        except ValueError:
            # self.errorMsg = ErrorMsg(self.master)
            # print("Incorrect Input")
            self.raiseError()

            return False
            
    
    
    # Prints the least number of coins
    def displayCoinOutput(self):

        calc = Calculations(self.getNumVrobits())
        self.coinNums = calc.getNumCoins()
        
        # clear
        self.inputBox.delete(0, END)
        self.drobitBox.delete(0, END)
        self.clickwickBox.delete(0, END)
        self.gazoonBox.delete(0, END)
        self.frazBox.delete(0, END)
        self.bloinBox.delete(0, END)
        self.vrobitBox.delete(0, END)

        # display
        self.drobitBox.insert(0, self.coinNums[0])
        self.clickwickBox.insert(0, self.coinNums[1])
        self.gazoonBox.insert(0, self.coinNums[2])
        self.frazBox.insert(0, self.coinNums[3])
        self.bloinBox.insert(0, self.coinNums[4])
        self.vrobitBox.insert(0, self.coinNums[5])
    

    # This function displays an error box when the user enters an incorrect input
    def raiseError(self):

        width = 400
        height = 125

        self.errorMsg = Toplevel(master=self.master, height=height, width=width)
        self.errorMsg.title("Invalid Number")
        self.errorMsg.resizable(False, False)

        # screenWidth = self.errorMsg.winfo_screenwidth()
        # screenHeight = self.errorMsg.winfo_screenheight()

        # x = width/2 - screenWidth
        # y = height/2 - screenHeight

        # self.errorMsg.geometry("+%d+%d" % (x, y))

        image = Image.open('WindowsError.png').convert('RGB')
        photo = ImageTk.PhotoImage(image)
        icon = Label(master=self.errorMsg, image=photo, width=30, height=30)
        icon.image = photo
        icon.grid(row=0, column=0)

        msg = Label(master=self.errorMsg, text="Please enter a valid number.")
        msg.grid(row=0, column=1)

        self.closeButton = Button(self.errorMsg, text="Close", command=self.destroyError)
        self.closeButton.grid(
            row = 1,
            column = 0,
            padx = (self.errorMsg.winfo_width() - self.closeButton.winfo_width())/2,
            pady = 5,
            columnspan = 2
        )
        
        self.bErrorVisible = True
        self.master.wait_variable(name=self.bErrorVisible)
    
    def destroyError(self):
        self.bErrorVisible = False
        self.errorMsg.destroy()



class ErrorMsg:

    def __init__(self, master):
        width = 400
        height = 125

        self.errorMsg = Toplevel(master=master, height=height, width=width)
        self.errorMsg.title("Invalid Number")
        self.errorMsg.resizable(False, False)

        # screenWidth = self.errorMsg.winfo_screenwidth()
        # screenHeight = self.errorMsg.winfo_screenheight()

        # x = width/2 - screenWidth
        # y = height/2 - screenHeight

        # self.errorMsg.geometry("+%d+%d" % (x, y))

        self.label = Frame(master=self.errorMsg)

        image = Image.open('WindowsError.png').convert('RGB')
        photo = ImageTk.PhotoImage(image)
        icon = Label(master=self.label, image=photo, width=30, height=30)
        icon.image = photo
        icon.grid(row=0, column=0)

        msg = Label(master=self.label, text="Please enter a valid number.")
        msg.grid(row=0, column=1)

        # self.label.pack(
        #     padx=(self.errorMsg.winfo_width() - self.label.winfo_width())/2,
        #     pady=20
        # )

        self.closeButton = Button(self.errorMsg, text="Close", command=self.errorMsg.destroy)
        self.closeButton.pack()

# main
root = Tk()
gui = GUI(root)
root.mainloop()
