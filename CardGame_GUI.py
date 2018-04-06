import tkinter as tk



class Statusbar:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)


class Main:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)

    # parent.title("Hello World")
    # parent.geometry('650x450')



class MainApplication:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.statusbar = Statusbar(master)
        self.main = Main(master)

        self.statusbar.frame.pack(side="bottom", fill="x")
        self.main.frame.pack(side="right", fill="both", expand=True)




if __name__ == "__main__":
    root = tk.Tk()
    mainApp = MainApplication(root)
    root.mainloop()
