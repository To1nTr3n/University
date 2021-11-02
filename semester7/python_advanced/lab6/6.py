import tkinter as tk
import tkinter.filedialog as dialog
class TextEditor:
    """A simple text editor."""
    def __init__(self, parent):
        """Create the GUI."""
        # Framework
        self.parent = parent
        self.frame = tk.Frame(parent)
        self.frame.pack()
        # Text box for editing.
        self.text = tk.Text(parent)
        self.text.pack()
        # Menus.
        menubar = tk.Menu(parent)
        filemenu = tk.Menu(menubar)
        filemenu.add_command(label='Save', command=self.save_click)
        filemenu.add_command(label='Quit', command=self.quit_click)
        menubar.add_cascade(label='File', menu=filemenu)
        window.config(menu=menubar)

    def save_click(self):
        """Handle click on 'Save' menu."""
        data = self.text.get('0.0', tk.END)
        filename = dialog.asksaveasfilename(
            parent=self.parent,
            filetypes=[('Text', '*.txt')],
            title='Save as...')
        writer = open(filename, 'w')
        writer.write(data)
        writer.close()

    def quit_click(self):
        """Handle click on 'Quit' menu."""
        self.parent.destroy()
if __name__ == '__main__':
    window = tk.Tk()
    app = TextEditor(window)
    window.mainloop()