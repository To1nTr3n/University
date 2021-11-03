from tkinter import Label,Tk , mainloop

root = Tk()
hello_label = Label(text= 'hello', font= ('Verdana', 24, 'bold'), bg = 'blue', fg = 'white')
hello_label.pack()

mainloop()