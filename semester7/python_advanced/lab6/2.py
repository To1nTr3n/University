import tkinter as tk
from typing import Text

def increment(text):
    count = int(text.get())
    text.set(str(count+1))

window = tk.Tk()
frame = tk.Frame(window)
frame.pack()

text = tk.IntVar()
text.set(0)
button = tk.Button(frame, textvariable=text, command= lambda: increment(text))

button.pack()
window.mainloop()