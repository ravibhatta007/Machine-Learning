# Gallons to Liters
from tkinter import *
gl=Tk()
gl.title("Unit Conversion")
n='arial',14,'bold'
Label(gl,text='Gallons',padx=25,font=(n)).grid(row=0,column=0,sticky=W)
e1=Entry(gl,width=25)
e1.grid(row=0,column=1)
Label(gl,text='Liters',padx=25,font=(n)).grid(row=1,column=0,sticky=W)
e2=Entry(gl,width=25)
e2.grid(row=1,column=1)
def convertgl1():
    try:
        e2.delete(0, END)
        var3=float(e1.get())*3.785
        e2.insert(0,var3)
    except:
        e1.delete(0,END)
        e1.insert(0,'Enter value here')
def convertgl2():
    try:
        e1.delete(0, END)
        var3=float(e2.get())/3.785
        e1.insert(0,var3)
    except:
        e2.delete(0,END)
        e2.insert(0,'Enter value here')
def clearsc():
    e1.delete(0, END)
    e2.delete(0, END)
Button(gl,text='Convert to Liter',command=convertgl1,font=(n)).grid(row=2,column=0)
Button(gl,text='Convert to Gallon',command=convertgl2,font=(n)).grid(row=2,column=1)
Button(gl,text='Clear',command=clearsc,font=(n)).grid(row=3,column=0)
Button(gl,text='Exit',command=gl.destroy,font=(n)).grid(row=3,column=1)
gl.mainloop()