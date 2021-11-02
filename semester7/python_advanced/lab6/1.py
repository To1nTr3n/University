import tkinter as tk

window = tk.Tk()
frame = tk.Frame(window)
frame.pack()

button = tk.Button(frame, text ='GoodBye', command=lambda: window.destroy())
button.pack()
window.mainloop()
