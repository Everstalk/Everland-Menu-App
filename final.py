#---------------------------------------
#Author - Michael Delasi Saneke        |
#Computer Programming for CS           |
#---------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------
import sys
from tkinter import *

items = []
names = ["Full Portion",
        "Half Portion",
        "Soft Drink",
        "Bottled Water",
        "Fruit",
        "Pastry"
        ]
itemNames = []

deluxePrice = 8
classicPrice = 6
sodasPrice = 4
volticPrice = 1
fruitPrice = 3
pastryPrice = 2

win = Tk()
win.geometry("500x500+200+100")
win.title("Everland Cafetaria")
#win.mainloop()

                                                                #Store class that contains the button functions and graphic properties                                
class Store:                                                    #Funtions executed when each button in the program is clicked

    #"Full Portion" button actions                  
    def deluxeBuy():
        total = 0
        itemNames.append("Full Portion     Ghc")
        items.append(deluxePrice)
        for i in items:
            if i == 8:
                total += 1
                dlx = Label(text=str(total)+" Full Portion",fg="lemon chiffon",bg="slate gray").place(x=200,y=70)

    #"Half-Portion" button actions    
    def classicBuy():
        total2 = 0
        itemNames.append("Half Portion    Ghc")
        items.append(classicPrice)
        for i in items:
            if i == 6:
                total2 += 1
                hlf = Label(text=str(total2)+" Half Portion",fg="lemon chiffon",bg="slate gray").place(x=200,y=100)

    #"Soft Drink" button actions    
    def sodasBuy(): 
        total3 = 0
        itemNames.append("Soft Drink      Ghc")
        items.append(sodasPrice)
        for i in items:
            if i == 4:
                total3 += 1
                dlx = Label(text=str(total3)+" Can Drink",fg="lemon chiffon",bg="slate gray").place(x=200,y=130)

    #"Bottled Water" button actions    
    def volticBuy():    
        total4 = 0
        itemNames.append("Bottled Water  Ghc")
        items.append(volticPrice)
        for i in items:
            if i == 1:
                total4 += 1
                dlx = Label(text=str(total4)+" Bottled Water",fg="lemon chiffon",bg="slate gray").place(x=200,y=160)

    #"Fruit" button actions    
    def fruitBuy(): 
        total5 = 0
        itemNames.append("Fruit             Ghc")
        items.append(fruitPrice)
        for i in items:
            if i == 3:
                total5 += 1
                dlx = Label(text=str(total5)+" Fruit",fg="lemon chiffon",bg="slate gray").place(x=200,y=190)

    #"Pastry" button actions    
    def pastryBuy():                                    
        total6 = 0
        itemNames.append("Pastry          Ghc")
        items.append(pastryPrice)
        for i in items:
            if i == 2:
                total6 += 1
                dlx = Label(text=str(total6)+" Pastry",fg="lemon chiffon",bg="slate gray").place(x=200,y=220)

    #"Clear" button actions
    def clear():                                       
        itemNames[:] = []
        items[:] = []
        canv = Canvas(win,height=400,width=200,bg="slate gray").place(x=140,y=20)
        
        
    #"Buy" button actions
    def total():                                        
        totalPrice = 0
        for i in items:
            totalPrice += i
        tt = Label(text="Your total amount is Ghc"+str(totalPrice)+".00",fg="navajo white",bg="slate gray").place(x=150,y=400)
        #Receipt Window
        win2 = Tk()
        win2.geometry("170x170")
        win2.title("Receipt")
        listbox = Listbox(win2)
        listbox.pack()
        listbox.insert(END,"Purchase Receipt:")
        for i,j in zip(itemNames,items):
            listbox.insert(END,(i,j))
        listbox.insert(END,"----------------------------------")
        listbox.insert(END,("Total:      Ghc",totalPrice,".00"))
        #mainloop()
            
    
    #Canvas on which selected items is displayed
    canvasWin = Canvas(win,height=500,width=500,bg="cornsilk4").place(x=0,y=0)
    flabel = Label(text="WELCOME, PLEASE MAKE YOUR ORDER",fg="blue4",bg="cornsilk4",font="Times").pack()
    canv = Canvas(win,height=400,width=200,bg="slate gray").place(x=140,y=20)


    #Images for Items
    deluxe = PhotoImage(file="deluxe.png")
    dlabel = Label(win,image=deluxe).place(x=20,y=50)

    classic = PhotoImage(file="classic.png")
    dlabel = Label(win,image=classic).place(x=360,y=50)

    sodas = PhotoImage(file="sodas.png")
    dlabel = Label(win,image=sodas).place(x=20,y=200)

    voltic = PhotoImage(file="voltic.png")
    dlabel = Label(win,image=voltic).place(x=360,y=200)

    fruit = PhotoImage(file="fruit.png")
    dlabel = Label(win,image=fruit).place(x=20,y=350)

    pastry = PhotoImage(file="pastry.png")
    dlabel = Label(win,image=pastry).place(x=360,y=350)

    #Labels for Item Names
    fp = Label(text="Full Portion",fg="yellow",bg="cornsilk4",font="Helvetica").place(x=20,y=100)
    hp = Label(text="Half Portion",fg="yellow",bg="cornsilk4",font="Helvetica").place(x=360,y=100)
    sd = Label(text="Soft Drink",fg="yellow",bg="cornsilk4",font="Helvetica").place(x=20,y=250)
    vt = Label(text="Small Water",fg="yellow",bg="cornsilk4",font="Helvetica").place(x=360,y=250)
    fr = Label(text="Fruit",fg="yellow",bg="cornsilk4",font="Helvetica").place(x=20,y=400)
    ps = Label(text="Pastry",fg="yellow",bg="cornsilk4",font="Helvetica").place(x=360,y=400)

    #Labels for Prices
    fpp = Label(text="Ghc 8.00",fg="dark green",bg="cornsilk4").place(x=70,y=50)
    hpp = Label(text="Ghc 6.00",fg="dark green",bg="cornsilk4").place(x=410,y=50)
    sdp = Label(text="Ghc 4.00",fg="dark green",bg="cornsilk4").place(x=70,y=200)
    vtp = Label(text="Ghc 1.00",fg="dark green",bg="cornsilk4").place(x=410,y=200)
    frp = Label(text="Ghc 3.00",fg="dark green",bg="cornsilk4").place(x=70,y=350)
    psp = Label(text="Ghc 2.00",fg="dark green",bg="cornsilk4").place(x=410,y=350)

    #Labels for Buttons
    fpb = Button(text="Select",command=deluxeBuy,bg="ivory4",fg="white").place(x=70,y=70)
    hpb = Button(text="Select",command=classicBuy,bg="ivory4",fg="white").place(x=410,y=70)
    sdb = Button(text="Select",command=sodasBuy,bg="ivory4",fg="white").place(x=70,y=220)
    vtb = Button(text="Select",command=volticBuy,bg="ivory4",fg="white").place(x=410,y=220)
    frb = Button(text="Select",command=fruitBuy,bg="ivory4",fg="white").place(x=70,y=370)
    psb = Button(text="Select",command=pastryBuy,bg="ivory4",fg="white").place(x=410,y=370)

    buy = Button(text="Buy",command=total).place(x=350,y=450)
    clear = Button(text="Clear",command=clear).place(x=250,y=450)

#----------------------------------------------------------------------------------------------------------------------------------------
#Product of the Sith Software Company
#All Rights Reserved ®
