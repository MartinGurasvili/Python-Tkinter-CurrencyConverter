import tkinter
from tkinter import *
from currency_converter import CurrencyConverter


root = Tk()
currencyval1 = StringVar(root)
currencyval2 = StringVar(root)
currencyval1.set("From")
currencyval2.set("To")

c = CurrencyConverter()

currecyinput = StringVar(root)
currecyoutput = StringVar(root)

root.title("Currency Coverter")


root.minsize(width=300, height=300)

running = True

def convert_cur(amount,fromm,too):
    print("hello")
    if(amount == None or fromm.get() == "From" or too.get() == "To"):
        pass
    else:
        print(amount,fromm.get(),too.get())
        currecyoutput.set(c.convert(amount,fromm.get(),too.get()))

def entry_valid(input):
    global currencyval1,currencyval2,currecyinput
    print("25.50".isdigit())
    if input[-1] == "." or input[-1].isdigit():
        currecyinput = input
        if(currencyval1.get() != "From" and currencyval2.get() != "To"):
            convert_cur(input,currencyval1,currencyval2)
            return True
        else:
            
            return True
                    
    
    elif input is "":
        return True
  
    else:

        return False
            
def callback(*args):
    global  currecyinput,currencyval1,currencyval2
    convert_cur(currecyinput,currencyval1,currencyval2)

label = Label(root, text='Currency Coverter', fg="#898989", font="Helveca 40 bold",bg="#282828")
label.pack()
amount = Entry(root,textvariable=currecyinput, fg="white", font="Geneva 30 bold",bg="#282828",justify=CENTER)
amount.pack()

reg = root.register(entry_valid)
  
amount.config(validate="key", validatecommand=(reg, '%P'))

currencyfrom= OptionMenu(root,currencyval1,*["EUR","USD","GBP","CAD","JPY","CNY","RUB"])
currencyfrom.config(width=38,height=2,fg="white", font="Helveca 15 bold",bg="#282828",justify=CENTER)
currencyfrom.pack()



currencyto= OptionMenu(root,currencyval2,*["EUR","USD","GBP","CAD","JPY","CNY","RUB"])
currencyto.config(width=38,height=2,fg="white", font="Helveca 15 bold",bg="#282828",justify=CENTER)
currencyto.pack()
currencyval1.trace('w',callback)
currencyval2.trace('w',callback)
output = Entry(root,textvariable=currecyoutput, fg="white", font="Geneva 30 bold",bg="#282828",justify=CENTER)
output.pack()


root.attributes("-alpha", 0.90)
root.configure(background="#282828")

root.mainloop()
conversion_loop()
