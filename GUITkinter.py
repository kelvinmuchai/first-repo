from tkinter import *
import os
window = Tk()
window.title('items storage')
window.geometry('400x300')
frame1 = Frame(window)
frame1.pack()

frame2=Frame(window)
frame2.pack()
Item = StringVar()
Itemprice = IntVar()
Itemquantity = IntVar()
b=[]
def calculate():
    Price=Itemprice.get()*Itemquantity.get()
    PRICE.config(text=Price)
def addtotalprice():
    Price = Itemprice.get() * Itemquantity.get()

    b.append(Price)
    c=0
    for i in b:
        c+=i
    with open('data.txt','w') as d:
        d.write(f'Total price for all your items is {c}\n')

def Save():
    Price = Itemprice.get() * Itemquantity.get()
    with open('data.txt','a') as G:
        G.write(f'Commodity = {Item.get()}\nPrice = {Itemprice.get()}\nquantity = {Itemquantity.get()}\nTotalprice = {Price}\n\n')

def openfile():
    os.system('open ./data.txt')

itemname = Label(frame1, text='Enter a product :')
itemname.grid(row=0, column=0)

itemprice = Label(frame1, text='Price of the commodity :')
itemprice.grid(row=1, column=0)

itemquantity = Label(frame1, text='Enter the amount :')
itemquantity.grid(row=2, column=0)

totalprice = Label(frame1, text='Totalprice')
totalprice.grid(row=3, column=0,sticky=W)

PRICE=Label(frame1)
PRICE.grid(row=3,column=1)


itementry = Entry(frame1, textvariable=Item)
itementry.grid(row=0, column=1)

itempriceentry = Entry(frame1, textvariable=Itemprice)
itempriceentry.grid(row=1, column=1)

itemquantityentry = Entry(frame1, textvariable=Itemquantity)
itemquantityentry.grid(row=2, column=1)

calculatebutton = Button(frame1,text='Totalprice',command=calculate)
calculatebutton.grid(row = 4,column = 0)

savebutton=Button(frame1,text='savetofile',command=Save)
savebutton.grid(row=4,column=1)

openFile=Button(frame1,text='opentextfile',command=openfile)
openFile.grid(row=5,column=1)

addtotalprice=Button(frame1,command=addtotalprice,text='Subtotal')
addtotalprice.grid(row=5,column=0)



window.mainloop()
