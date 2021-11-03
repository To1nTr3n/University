import tkinter as tk
window = tk.Tk()
def s_circle(r,pi):
    r= r.get()
    pi= pi.get()
    s.set(pi * r* r)
frame = tk.Frame(window)
frame.pack()

s= tk.DoubleVar()
r= tk.DoubleVar()
pi= tk.DoubleVar()

tk.Label(frame, text= 'Calculate the area of a circle').pack()

tk.Label(frame, text= 'Input radius').pack()
tk.Entry(frame, textvar = r).pack()
tk.Label(frame, text= 'input pi').pack()
tk.Entry(frame, textvar = pi).pack()
tk.Label(frame, text= 'The area of the circle is').pack()
tk.Label(frame, textvar = s).pack()

tk.Button(frame, text= 'Calculate', command= lambda: s_circle(r,pi)).pack()
tk.Button(frame, text= 'Quit', command= lambda: window.destroy()).pack()
window.mainloop()


