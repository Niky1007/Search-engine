from tkinter import*
from wikipedia import summary


window  = Tk()

window.geometry('1366x768')

window.title("Navis/wiki")


photo = PhotoImage(file="C://Users//Karthikeyan//Desktop//html2//threed.png")

can = Canvas(width=1366,height=768)
can.pack()
def information():

    entry.insert(INSERT,summary(e.get()))
    

can.create_image(0,0,image=photo,anchor=NW)

w = Button(window,background="red",text="EXIT" ,activebackground="white" , activeforeground="red",fg="white",bd=0,font=('arial',15,'bold'),command=lambda:window.destroy())

w.place(x=50,y=50)


q = Button(window,text="Search:",font=('arial',13,'bold'),bd=0,activebackground="white",activeforeground="black",bg="#3C3352",fg="white",highlightbackground="black",highlightthickness=5,highlightcolor="black",command=information)

q.pack(side=LEFT)

q.place(x=50,y=110)


e = Entry(window, bd=0, width=50,font=('arial',18),highlightbackground="black",highlightcolor="black",highlightthickness=2,background="white",fg="black")

e.pack(side=RIGHT)

e.place(x=160,y=110)


entry = Text(window,bd=0,font=('serif',15),background="white",highlightbackground="black",highlightcolor="#FF6363",highlightthickness=2,fg="black")

entry.pack(side=LEFT)

entry.place(x=160,y=160,width=1100,height=500)


window.mainloop()

    





                    










