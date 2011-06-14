import Tkconstants
import Tkinter
import tkFileDialog
import time

budici_soubor = '/tmp/neco'
chci_budit = False
#tohle je v milisekundach, 
budici_interval = 8 * 60 * 1000


class TkBuditel(Tkinter.Frame):

    def budit(self):
        global chci_budit
        chci_budit = not(chci_budit)
        self.tick()

    def tick(self):
        global chci_budit
        global curtime
        global budici_interval
        newtime = time.strftime('%H:%M:%S')
        if chci_budit:
            newtime = "Budim: " + newtime + ""
            soubor = open(budici_soubor, 'w')
            soubor.write("""
lupDujHomwIj luteb gharghmey
""" + newtime + "\n")
            soubor.close()

        else:
            newtime = "Nebudim: " + newtime + ""

        self.clock.config(text=newtime)
        self.clock.after(budici_interval, self.tick)

    def __init__(self, root):

        Tkinter.Frame.__init__(self, root)

        # options for buttons
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

        # define buttons
        self.btnBudit = Tkinter.Button(self,
                text='<|>',
                command=self.budit).pack(**button_opt)

        curtime = ''
        self.clock = Tkinter.Label()
        self.clock.pack()

        self.tick()

if __name__ == '__main__':
    root = Tkinter.Tk()
    TkBuditel(root).pack()
    root.mainloop()
