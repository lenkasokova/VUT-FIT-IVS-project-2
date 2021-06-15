#!/usr/bin/env python3

##
# @file GUI.py
# @brief GUI for calculator
# @author Samuel Smekal <xsmeka16>
#

###############################################################################
# Project name: IVS Project 2
# Authors: Samuel Smekal <xsmeka16>
# File: GUI.py
# Last modified: 29.4.2021
# Date: 11.3.2021
###############################################################################

from tkinter import *
from GUI_mediator import *

main = Tk()
main.title("Kalkulačka")
main.minsize(420,420)
main.maxsize(420,420)
main.configure(bg='grey')

# Functions

def showResult():
    """
    showResult function
    Loads the input, calculates it and then prints the result on display
    """
    displayInput = Input.get()
    displayInput = calculate(displayInput)

    if displayInput is False:
        displayInput = "Math error"

    Input.delete(0,END)
    Input.insert(0, str(displayInput))


def errorcheck():
    """
    errorcheck function
    Check if there was a math error on the last use of = and deletes the error message when next button is pressed
    """
    if Input.get() == "Math error":
        Input.delete(0,END)

def sin():
    """
    sin function
    prints sin( at the end of display
    """
    errorcheck()
    Input.insert(END,"sin(")

def cos():
    """
    cos function
    prints cos( at the end of display
    """
    errorcheck()
    Input.insert(END,"cos(")

def tg():
    """
    sin function
    prints tg( at the end of display
    """
    errorcheck()
    Input.insert(END,"tg(")

def delete():
    """
    delete function
    deletes the last character on display
    """
    errorcheck()
    Input.delete(len(Input.get())-1,END)

def square():
    """
    square function
    prints ^2 at the end of display
    """
    errorcheck()
    Input.insert(END,"^2")

def powered():
    """
    powered function
    prints ^ at the end of display
    """
    errorcheck()
    Input.insert(END,"^")

def sqrt():
    """
    sqrt function
    prints 2 rt( at the end of display
    """
    errorcheck()
    Input.insert(END,"2 rt(")

def rt():
    """
    sqrt function
    prints 2 rt( at the end of display
    """
    errorcheck()
    Input.insert(END," rt(")

def factor():
    """
    factor function
    prints ! at the end of display
    """
    errorcheck()
    Input.insert(END,"!")

def leftb():
    """
    leftb function
    prints ( at the end of display
    """
    errorcheck()
    Input.insert(END,"(")

def rightb():
    """
    rightb function
    prints ) at the end of display
    """
    errorcheck()
    Input.insert(END,")")

def divis():
    errorcheck()
    """
    divis function
    prints / at the end of display
    """
    Input.insert(END,"/")

def seven():
    """
    seven function
    prints 7 at the end of display
    """
    errorcheck()
    Input.insert(END,"7")

def eight():
    """
    eight function
    prints 8 at the end of display
    """
    errorcheck()
    Input.insert(END,"8")

def nine():
    """
    nine function
    prints 9 at the end of display
    """
    errorcheck()
    Input.insert(END,"9")

def multip():
    """
    multip function
    prints * at the end of display
    """
    errorcheck()
    Input.insert(END,"*")

def four():
    """
    four function
    prints 4 at the end of display
    """
    errorcheck()
    Input.insert(END,"4")

def five():
    """
    five function
    prints 5 at the end of display
    """
    errorcheck()
    Input.insert(END,"5")

def six():
    """
    six function
    prints 6 at the end of display
    """
    errorcheck()
    Input.insert(END,"6")

def minus():
    """
    minus function
    prints - at the end of display
    """
    errorcheck()
    Input.insert(END,"-")

def one():
    """
    one function
    prints 1 at the end of display
    """
    errorcheck()
    Input.insert(END,"1")

def two():
    """
    two function
    prints 2 at the end of display
    """
    errorcheck()
    Input.insert(END,"2")

def three():
    """
    three function
    prints 3 at the end of display
    """
    errorcheck()
    Input.insert(END,"3")

def plus():
    """
    plus function
    prints + at the end of display
    """
    errorcheck()
    Input.insert(END,"+")

def zero():
    """
    zero function
    prints 0 at the end of display
    """
    errorcheck()
    Input.insert(END,"0")

def dot():
    """
    dot function
    prints . at the end of display
    """
    errorcheck()
    Input.insert(END,".")

def c():
    """
    c function
    deletes everything, that is shown on display
    """
    errorcheck()
    Input.delete(0,END)

def _help():
    """
    help function
    Opens a new window containing help message
    """

    helpWin = Tk()
    helpWin.title("Help")

    helpTextWindow = Text(helpWin,width=100)
    helpTextWindow.grid(row=0,column=0)

    # String containing help message
    helpText=StringVar()
    helpText.set("Kalkulačka sa ovláda myšou, pomocou ktorej môžete lavým tlačidlom naťukať číselné hodnoty/operácie.\n\n"+
                    "Taktiež je dostupné zadávanie cez klávesnicu.\n\n"+
                    "Pre zmazanie celého výrazu zobrazeného na displeji stlačte znak C\n\n"+
                    "Pre zmazanie jedného znaku zobrazeného na displeji stlačte DEL\n\n"+
                    "Kalkulačka podporuje desatinné čísla, ktoré sa zadavajú znakom ,\n\n"+
                    "Pre výpočet n-tej odmocniny zadajte n a následne stlačte "+"\u207f√ \n\n"+
                    "Výsledok zadanej rovnice sa zobrazí na displeji po stlačení znaku =\n\n"+
                    "Dostupné operácie:\n"+
                    "   - sčítanie -> +\n"+
                    "   - odčítanie -> -\n"+
                    "   - násobenie -> \u00d7\n"+
                    "   - delenie -> \u00f7\n\n"+
                    "Dostupné matematické funkcie:\n"+
                    "   - Druhá mocnina -> x²\n"+
                    "   - N-tá mocnina -> x\u207f\n"+
                    "   - Druhá odmocnina -> \u00b2√\n"+
                    "   - N-tá odmocnina -> \u207f√\n"+
                    "   - Faktoriál -> \u0021\n"+
                    "   - Sínus -> sin\n"+
                    "   - Kosínus -> cos\n"+
                    "   - Tangens -> tg\n\n"+
                    "Priorita operácií (od najväčšej po najmenšiu prioritu):\n"+
                    "   - Zátvorky\n"+
                    "   - Funkcie, násobenie, delenie\n"+
                    "   - Sčítanie, odčítanie\n\n"+
                    "Poznámka: Pri rovnakej priorite sa výraz vyhodnocuje zľava doprava.\n\n"+
                    "Minimalizácia aplikácie sa vykoná po zakliknutí na znak \"-\" v pravom hornom rohu.\n\n"+
                    "Vypnutie aplikácie sa vykoná po zakliknutí na znak \"+\" v pravom hornom rohu.")
    helpTextWindow.insert(1.0,helpText.get())

    helpWin.mainloop()





# Labelframe for Display
Display_frame = LabelFrame(main, text="", bg = "grey")
Display_frame.grid(row = 0, column = 0, sticky = NSEW, padx=10, pady=10)

# Entry 
Input = Entry(Display_frame, text ="", width = 23,font=("Arial",19))
Input.grid(row = 0, column = 1, padx=30, pady=10)

# Help button
Button_help = Button(main, text = "[HELP]", command = _help, width = 28,font=("Arial",15))
Button_help.grid(row = 1, column = 0, padx=1, pady=1)

# Labelframe for keyboard
Buttons_frame = LabelFrame(main, text="", bg = "lightgrey")
Buttons_frame.grid(row = 2, column = 0, padx=10, pady=10)

"""1. row of keyboard"""

# sin button
Button_sin = Button(Buttons_frame, text = "sin", command = sin, width = 6,font=("Arial",15))
Button_sin.grid(row = 0, column = 0, padx=1, pady=1)

# cos button
Button_cos = Button(Buttons_frame, text = "cos", command = cos, width = 6,font=("Arial",15))
Button_cos.grid(row = 0, column = 1, padx=1, pady=1)

# tg button
Button_tg = Button(Buttons_frame, text = "tg", command = tg, width = 6,font=("Arial",15))
Button_tg.grid(row = 0, column = 2, padx=1, pady=1)

#DEL button
Button_del = Button(Buttons_frame, text = "DEL", command = delete, width = 6,font=("Arial",15))
Button_del.grid(row = 0, column = 3, padx=1, pady=1)

"""2. row of keyboard"""

# X to power of 2 button
Button_druha_mocnina = Button(Buttons_frame, text = "x²", command = square, width = 6,font=("Arial",15))
Button_druha_mocnina.grid(row = 1, column = 0, padx=1, pady=1)

# X to power on n button
Button_nta_mocnina = Button(Buttons_frame, text = "x\u207f", command = powered, width = 6,font=("Arial",15))
Button_nta_mocnina.grid(row = 1, column = 1, padx=1, pady=1)

# Square root button
Button_druha_odmocnina = Button(Buttons_frame, text = "\u00b2√", command = sqrt, width = 6,font=("Arial",15))
Button_druha_odmocnina.grid(row = 1, column = 2, padx=1, pady=1)

# n'th root button
Button_nta_odmocnina = Button(Buttons_frame, text = "\u207f√", command = rt, width = 6,font=("Arial",15))
Button_nta_odmocnina.grid(row = 1, column = 3, padx=1, pady=1)
    
"""3. row of keyboard"""

# Factorial button
Button_faktorial = Button(Buttons_frame, text = "\u0021", command = factor, width = 6,font=("Arial",15))
Button_faktorial.grid(row = 2, column = 0, padx=1, pady=1)

# Left bracket button
Button_leftb = Button(Buttons_frame, text = "(", command = leftb, width = 6,font=("Arial",15))
Button_leftb.grid(row = 2, column = 1, padx=1, pady=1)

# Right bracket button
Button_rightb = Button(Buttons_frame, text = ")", command = rightb, width = 6,font=("Arial",15))
Button_rightb.grid(row = 2, column = 2, padx=1, pady=1)

# Division button
Button_div = Button(Buttons_frame, text = "\u00f7", command = divis, width = 6,font=("Arial",15))
Button_div.grid(row = 2, column = 3, padx=1, pady=1)

"""4. row of keyboard"""

# Number 7 button
Button_7 = Button(Buttons_frame, text = "7", command = seven, width = 6,font=("Arial",15))
Button_7.grid(row = 3, column = 0, padx=1, pady=1)

# Number 8 button
Button_8 = Button(Buttons_frame, text = "8", command = eight, width = 6,font=("Arial",15))
Button_8.grid(row = 3, column = 1, padx=1, pady=1)

# Number 9 button
Button_9 = Button(Buttons_frame, text = "9", command = nine, width = 6,font=("Arial",15))
Button_9.grid(row = 3, column = 2, padx=1, pady=1)

# Multiply button
Button_multiply = Button(Buttons_frame, text = "\u00d7", command = multip, width = 6,font=("Arial",15))
Button_multiply.grid(row = 3, column = 3, padx=1, pady=1)

"""5. row of keyboard"""

# Number 4 button
Button_4 = Button(Buttons_frame, text = "4", command = four, width = 6,font=("Arial",15))
Button_4.grid(row = 4, column = 0, padx=1, pady=1)

# Number 5 button
Button_5 = Button(Buttons_frame, text = "5", command = five, width = 6,font=("Arial",15))
Button_5.grid(row = 4, column = 1, padx=1, pady=1)

# Number 6 button
Button_6 = Button(Buttons_frame, text = "6", command = six, width = 6,font=("Arial",15))
Button_6.grid(row = 4, column = 2, padx=1, pady=1)

# Minus button
Button_minus = Button(Buttons_frame, text = "-", command = minus, width = 6,font=("Arial",15))
Button_minus.grid(row = 4, column = 3, padx=1, pady=1)

"""6. row of keyboard"""

# Number 1 button
Button_1 = Button(Buttons_frame, text = "1", command = one, width = 6,font=("Arial",15))
Button_1.grid(row = 5, column = 0, padx=1, pady=1)

# Number 2 button
Button_2 = Button(Buttons_frame, text = "2", command = two, width = 6,font=("Arial",15))
Button_2.grid(row = 5, column = 1, padx=1, pady=1)

# Number 3 button
Button_3 = Button(Buttons_frame, text = "3", command = three, width = 6,font=("Arial",15))
Button_3.grid(row = 5, column = 2, padx=1, pady=1)

# Plus button
Button_plus = Button(Buttons_frame, text = "+", command = plus, width = 6,font=("Arial",15))
Button_plus.grid(row = 5, column = 3, padx=1, pady=1)

"""7. row of keyboard"""

# Number 0 button
Button_0 = Button(Buttons_frame, text = "0", command = zero, width = 6,font=("Arial",15))
Button_0.grid(row = 6, column = 0, padx=1, pady=1)

# Dot button
Button_dot = Button(Buttons_frame, text = ",", command = dot, width = 6,font=("Arial",15))
Button_dot.grid(row = 6, column = 1, padx=1, pady=1)

# C button
Button_clr = Button(Buttons_frame, text = "C", command = c, width = 6,font=("Arial",15))
Button_clr.grid(row = 6, column = 2, padx=1, pady=1)

# = button
Button_vysledek = Button(Buttons_frame, text = "=", command = showResult, width = 6,font=("Arial",15))
Button_vysledek.grid(row = 6, column = 3, padx=1, pady=1)

main.mainloop()
