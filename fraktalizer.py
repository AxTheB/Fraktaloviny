import os
import random
import shutil

import Tkconstants
import Tkinter
import tkFileDialog


class TkFractalizer(Tkinter.Frame):

    def __init__(self, root):

        Tkinter.Frame.__init__(self, root)

        # options for buttons
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

        # define buttons
        Tkinter.Button(self,
                text='Source',
                command=self.askdirectory_source).pack(**button_opt)
        self.source_label = Tkinter.StringVar()
        Tkinter.Label(self,
                text="",
                textvariable=self.source_label).pack()
        Tkinter.Button(self,
                text='Target',
                command=self.askdirectory_dest).pack(**button_opt)
        self.target_label = Tkinter.StringVar()
        Tkinter.Label(self,
                text="",
                textvariable=self.target_label).pack()
        self.spinbox = Tkinter.Spinbox(self, from_=1, to=999)
        self.spinbox.pack(**button_opt)

        #opravdu neni min debilni metda jak tam zadat hodnotu?
        self.spinbox.delete(0)
        self.spinbox.insert(0, "3")

        Tkinter.Button(self,
                text='Burn my computer!',
                command=self.go).pack(**button_opt)
        self.status_label = Tkinter.StringVar()
        Tkinter.Label(self, textvariable=self.status_label).pack()
        self.status_label.set("Ready")

        # defining options for opening a directory
        self.dir_opt_source = options_source = {}
        options_source['initialdir'] = '/etc/apm'
        options_source['mustexist'] = True
        options_source['parent'] = root
        options_source['title'] = 'Source directory'

        self.dir_opt_dest = options_dest = {}
        options_dest['initialdir'] = '/tmp/pokus'
        options_dest['mustexist'] = True
        options_dest['parent'] = root
        options_dest['title'] = 'Target directory'

        self.fromdir = options_source['initialdir']
        self.todir = options_dest['initialdir']
        self.source_label.set(self.fromdir)
        self.target_label.set(self.todir)

    def askdirectory_source(self):

        """Returns a selected directoryname."""

        self.fromdir = tkFileDialog.askdirectory(**self.dir_opt_source)
        self.dir_opt_source['initialdir'] = self.fromdir
        self.source_label.set(self.fromdir)

    def askdirectory_dest(self):

        """Returns a selected directoryname."""

        self.todir = tkFileDialog.askdirectory(**self.dir_opt_dest)
        self.dir_opt_dest['initialdir'] = self.todir
        self.target_label.set(self.todir)

    def go(self):
        """ Traverses _source directory, selects Spinbox files and
        copies them to _dest direcotry"""
        self.status_label.set('Working')
        self.filelist = []
        numfiles = int(self.spinbox.get())
        for root, dirs, files in os.walk(self.fromdir):
            for name in files:
                #pokud by bylo treba delat filtr na typ souboru tak ho dat sem
                if name[-3:] == "psd":
                    self.filelist.append(os.path.join(root, name))

        self.status_label.set("Found %s files" % len(self.filelist))
        self.tarfilelist = []

        if len(self.filelist) < numfiles:
            self.tarfilelist = self.filelist
        else:
            for num in range(numfiles):
                work_item = self.filelist[random.randint(0,
                    len(self.filelist) - 1)]
                self.tarfilelist.append(work_item)
                self.filelist.remove(work_item)

        for work_file in self.tarfilelist:
            dest_file_name = work_file[len(self.fromdir) + 1:].replace(
                    os.path.sep, "_")
            print dest_file_name
            shutil.copy(work_file, os.path.join(self.todir, dest_file_name))

        return True


if __name__ == '__main__':
    root = Tkinter.Tk()
    TkFractalizer(root).pack()
    root.mainloop()
