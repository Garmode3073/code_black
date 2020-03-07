from tkinter import *
import demo as d

def bill():
    window2 = Tk()
    window2.config(bg="white")
    window2.title("YOUR BILL")
    scrollbar = Scrollbar(window2)
    scrollbar.pack( side = RIGHT, fill=Y )
    s=d.text_detected
    label=Label(text=s, relief="solid", font=("ariel", 14, "bold"))
    #label.place(x=40,y=40)
    area = Text(window2, yscrollcommand = scrollbar.set, )
    area.pack(expand=True, fill='both')
    area.insert(END,s)
    scrollbar.config( command = area.yview )
    window2.mainloop()

bill()
