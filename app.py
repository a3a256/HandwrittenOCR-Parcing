from tkinter import *
from tkinter import filedialog

class UI:
    def __init__(self, ui):
        self.ui = ui
        self.path = None

    def browsing_files(self):
        filename = filedialog.askopenfilename()
        self.path = filename

    def go(self):
        button = Button(master=self.ui, text="Select pitcure to parse...", command=self.browsing_files)
        button.grid(row=0, column=0)
        self.ui.mainloop()


if __name__ == "__main__":
    wn = Tk()
    ui = UI(wn)
    ui.go()