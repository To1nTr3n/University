import tkinter as tk

window = tk.Tk()
def convert(out_data, team_data):
    f= temp_data.get()
    out_data.set((f-32)*5/9)
frame = tk.Frame(window)
frame.pack()

out_data= tk.StringVar()
temp_data= tk.DoubleVar()

tk.Label(frame, text= 'Temperature in Fahrenheit').pack()
tk.Entry(frame, textvar = temp_data).pack()
tk.Label(frame, textvar = out_data).pack()
tk.Button(frame, text= 'Convert', command= lambda: convert(out_data, temp_data)).pack()
tk.Button(frame, text= 'Quit', command= lambda: window.destroy()).pack()
window.mainloop()


