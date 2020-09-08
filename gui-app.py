from tkinter import *
from tkinter import filedialog
import os
import tkinter.font as font
from functools import partial
import ctypes

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )

global directory
directory = "sprites"

def bleed_directory(dir = directory):
	r = []
	w.delete(0, END)
	subdirs = [x[0] for x in os.walk(directory)]
	for subdir in subdirs:
		files = os.walk(subdir).__next__()[2]
		if (len(files) > 0):
			for file in files:
				if (file.endswith(".png")):
					logtxt = "Bleeded " + subdir + "\\" + file
					print(logtxt)
					w.insert(END, logtxt)
					os.system("alpha_bleeding.exe " + subdir + "\\" + file + " " + subdir + "\\" + file)
				else:
					print("Format not supported")

def directory_contents(dir):
	r = []
	
	subdirs = [x[0] for x in os.walk(dir)]
	for subdir in subdirs:
		files = os.walk(subdir).__next__()[2]
		if (len(files) > 0):
			for file in files:
				if(file.endswith(".png")):
					r.append(subdir + "\\" + file + "\n")
	return r

def fillDir(li, dir):
	l = directory_contents(dir)
	li.delete(0, END)
	for i in range(len(l)):
		li.insert(END, l[i])

def OpenSelect(evt):
	val=str((t.get(ACTIVE)))
	os.system("\""+val+"\"")

def pick_directory():
	global directory
	directory = filedialog.askdirectory()
	fillDir(t, directory)

wind = Tk()

wind.title("Bleeding Tool")
wind.iconbitmap("assets/icon.ico")
wind.resizable(False, False)
wind.lift()
wind.attributes("-topmost", True)
wind.after(10, lambda: wind.focus_force())

consolas = font.Font(family = "consolas", size = 10)

f = Frame(wind)

fl = Frame(f)

tl = Label(fl, text = "Directory tree:							")

tl.pack()

t = Listbox(fl, font = "calibri", width = 50, height = 16, relief = FLAT);

t.bind('<Double-1>', OpenSelect)

fillDir(t, directory)

t.pack()

st = Scrollbar(fl, orient=HORIZONTAL)

st.config(command=t.xview)

st.pack(fill=X)

sw = Scrollbar(fl)

fw  = Frame(f)

wl = Label(fw, text = "Process log:							")

wl.pack()

w = Listbox(fw, font = consolas, width = 60, height = 20, bg = "#000000", fg = "#ffffff", relief = FLAT);

w.pack()

sw = Scrollbar(fw, orient=HORIZONTAL)

sw.config(command=w.xview)

sw.pack(fill=X)

fl.pack(side = LEFT)

fw.pack(side = LEFT)

f.pack()

bf = Frame(wind)

b = Button(bf, text="Bleed Directory", command=partial(bleed_directory))

b.pack(side = LEFT)

b2 = Button(bf, text="Pick Directory", command=pick_directory)

b2.pack(side = LEFT)

bf.pack()



wind.mainloop()