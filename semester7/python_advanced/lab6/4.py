import tkinter as tk
def count(text, out_data):
    """ Update out_data with the total number of As, Ts, Cs, and Gs found in
    text."""
    data = text.get('0.0', tk.END)
    counts = {}
    for char in 'ATCG':
        counts[char] = data.count(char)
    out_data.set(f"Num As: {counts['A']} -  Num Ts: {counts['T']} -  Num Cs: {counts['C']} -  Num Gs: {counts['G']}")

window = tk.Tk()

text = tk.Text(window, height=10, width=40)
text.pack()
out_data = tk.StringVar()
button = tk.Button(window, text='Count', command= lambda: count(text,out_data))
button.pack()
label = tk.Label(window, textvar=out_data)
label.pack()
window.mainloop()