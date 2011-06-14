import Tkinter
import Tkconstants
import tkFileDialog
import os
import random
import shutil

"""Skopíruje numfiles soubrů z fromdir a podadresářů  do todir"""

fromdir = os.curdir
todir = '/tmp/pokus'
numfiles = 80
#filtr na přípony
extension = ''


def build_filelist():
    filelist = []
    for root, dirs, files in os.walk(fromdir):
        for name in files:
            if extension == "" or name[-len(extension):] == extension:
                filelist.append(os.path.join(root, name))
    return filelist

filelist = build_filelist()

tarfilelist = []


def filelist_shuffle(num):
    work_item = filelist[random.randint(0, len(filelist) - 1)]
    tarfilelist.append(work_item)
    filelist.remove(work_item)

if len(filelist) < numfiles:
    tarfilelist = filelist
else:
    for num in range(numfiles):
        filelist_shuffle(num)

for work_file in tarfilelist:
    dest_file_name = work_file[len(fromdir) + 1:].replace(os.path.sep, "_")
    print dest_file_name
    shutil.copy(work_file, os.path.join(todir, dest_file_name))
