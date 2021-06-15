# -*- coding: utf-8 -*-
"""

@author: Samuel

GUI pro projekt n.2 pro předmět IVS 2021

"""

"""Po stisknutí = se uloží obsah displaye do proměnné displayInput jako string"""

from tkinter import *

main = Tk()
main.title("Kalkulačka")
main.minsize(370,420)
main.maxsize(370,420)
main.configure(bg='grey')

displayInput = int

def getInput():
    displayInput = Input.get()
    print(displayInput)
    Input.delete(0,END)

""" Display """

Display_frame = LabelFrame(main, text="", bg = "grey")
Display_frame.grid(row = 0, column = 0, sticky = NSEW, padx=10, pady=10)

Input = Entry(Display_frame, text ="", width = 23,font=("Arial",19))
Input.grid(padx=10, pady=10)

Buttons_frame = LabelFrame(main, text="", bg = "lightgrey")
Buttons_frame.grid(row = 1, column = 0, padx=10, pady=10)

"""1.radek"""

Button_sqrt = Button(Buttons_frame, text = "sin", command = lambda:Input.insert(END,"sin("), width = 6,font=("Arial",15))
Button_sqrt.grid(row = 0, column = 0, padx=1, pady=1)
Button_left_bracket = Button(Buttons_frame, text = "cos", command = lambda:Input.insert(END,"cos("), width = 6,font=("Arial",15))
Button_left_bracket.grid(row = 0, column = 1, padx=1, pady=1)
Button_right_bracket = Button(Buttons_frame, text = "tg", command = lambda:Input.insert(END,"tg("), width = 6,font=("Arial",15))
Button_right_bracket.grid(row = 0, column = 2, padx=1, pady=1)
Button_del = Button(Buttons_frame, text = "DEL", command = lambda:Input.delete(len(Input.get())-1,END), width = 6,font=("Arial",15))
Button_del.grid(row = 0, column = 3, padx=1, pady=1)

"""2.radek"""

Button_druha_mocnina = Button(Buttons_frame, text = "x²", command = lambda:Input.insert(END,"^2"), width = 6,font=("Arial",15))
Button_druha_mocnina.grid(row = 1, column = 0, padx=1, pady=1)
Button_nta_mocnina = Button(Buttons_frame, text = "x\u207f", command = lambda:Input.insert(END,"^"), width = 6,font=("Arial",15))
Button_nta_mocnina.grid(row = 1, column = 1, padx=1, pady=1)
Button_druha_odmocnina = Button(Buttons_frame, text = "\u00b2√", command = lambda:Input.insert(END,"2 rt("), width = 6,font=("Arial",15))
Button_druha_odmocnina.grid(row = 1, column = 2, padx=1, pady=1)
Button_nta_odmocnina = Button(Buttons_frame, text = "\u207f√", command = lambda:Input.insert(END," rt("), width = 6,font=("Arial",15))
Button_nta_odmocnina.grid(row = 1, column = 3, padx=1, pady=1)
    
"""3.radek"""

Button_sin = Button(Buttons_frame, text = "\u0021", command = lambda:Input.insert(END,"!"), width = 6,font=("Arial",15))
Button_sin.grid(row = 2, column = 0, padx=1, pady=1)
Button_cos = Button(Buttons_frame, text = "(", command = lambda:Input.insert(END,"("), width = 6,font=("Arial",15))
Button_cos.grid(row = 2, column = 1, padx=1, pady=1)
Button_tg = Button(Buttons_frame, text = ")", command = lambda:Input.insert(END,")"), width = 6,font=("Arial",15))
Button_tg.grid(row = 2, column = 2, padx=1, pady=1)
Button_div = Button(Buttons_frame, text = "\u00f7", command = lambda:Input.insert(END,"/"), width = 6,font=("Arial",15))
Button_div.grid(row = 2, column = 3, padx=1, pady=1)

"""4.radek"""

Button_7 = Button(Buttons_frame, text = "7", command = lambda:Input.insert(END,"7"), width = 6,font=("Arial",15))
Button_7.grid(row = 3, column = 0, padx=1, pady=1)
Button_8 = Button(Buttons_frame, text = "8", command = lambda:Input.insert(END,"8"), width = 6,font=("Arial",15))
Button_8.grid(row = 3, column = 1, padx=1, pady=1)
Button_9 = Button(Buttons_frame, text = "9", command = lambda:Input.insert(END,"9"), width = 6,font=("Arial",15))
Button_9.grid(row = 3, column = 2, padx=1, pady=1)
Button_multiply = Button(Buttons_frame, text = "\u00d7", command = lambda:Input.insert(END,"*"), width = 6,font=("Arial",15))
Button_multiply.grid(row = 3, column = 3, padx=1, pady=1)

"""5.radek"""

Button_4 = Button(Buttons_frame, text = "4", command = lambda:Input.insert(END,"4"), width = 6,font=("Arial",15))
Button_4.grid(row = 4, column = 0, padx=1, pady=1)
Button_5 = Button(Buttons_frame, text = "5", command = lambda:Input.insert(END,"5"), width = 6,font=("Arial",15))
Button_5.grid(row = 4, column = 1, padx=1, pady=1)
Button_6 = Button(Buttons_frame, text = "6", command = lambda:Input.insert(END,"6"), width = 6,font=("Arial",15))
Button_6.grid(row = 4, column = 2, padx=1, pady=1)
Button_minus = Button(Buttons_frame, text = "-", command = lambda:Input.insert(END,"-"), width = 6,font=("Arial",15))
Button_minus.grid(row = 4, column = 3, padx=1, pady=1)

"""6.radek"""

Button_1 = Button(Buttons_frame, text = "1", command = lambda:Input.insert(END,"1"), width = 6,font=("Arial",15))
Button_1.grid(row = 5, column = 0, padx=1, pady=1)
Button_2 = Button(Buttons_frame, text = "2", command = lambda:Input.insert(END,"2"), width = 6,font=("Arial",15))
Button_2.grid(row = 5, column = 1, padx=1, pady=1)
Button_3 = Button(Buttons_frame, text = "3", command = lambda:Input.insert(END,"3"), width = 6,font=("Arial",15))
Button_3.grid(row = 5, column = 2, padx=1, pady=1)
Button_plus = Button(Buttons_frame, text = "+", command = lambda:Input.insert(END,"+"), width = 6,font=("Arial",15))
Button_plus.grid(row = 5, column = 3, padx=1, pady=1)

"""7.radek"""

Button_0 = Button(Buttons_frame, text = "0", command = lambda:Input.insert(END,"0"), width = 6,font=("Arial",15))
Button_0.grid(row = 6, column = 0, padx=1, pady=1)
Button_dot = Button(Buttons_frame, text = ",", command = lambda:Input.insert(END,"."), width = 6,font=("Arial",15))
Button_dot.grid(row = 6, column = 1, padx=1, pady=1)
Button_clr = Button(Buttons_frame, text = "C", command = lambda:Input.delete(0,END), width = 6,font=("Arial",15))
Button_clr.grid(row = 6, column = 2, padx=1, pady=1)
Button_vysledek = Button(Buttons_frame, text = "=", command = getInput, width = 6,font=("Arial",15))
Button_vysledek.grid(row = 6, column = 3, padx=1, pady=1)






main.mainloop()