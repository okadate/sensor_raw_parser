import os, tkinter, tkinter.filedialog


def filedialog():
    root = tkinter.Tk()
    root.withdraw()

    idir = os.path.abspath(os.path.dirname(__file__))
    f = tkinter.filedialog.askopenfilename(filetypes=[("","csv")], initialdir=idir)
    root.update()
    
    return f