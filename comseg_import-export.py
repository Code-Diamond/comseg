from tkinter import filedialog
import tkinter as tk


def setImportFile():
	root.importFile =  filedialog.askopenfilename(initialdir = "/",title = "Select Video File to Import",filetypes = (("mkv files","*.mkv"),("mp4 files","*.mp4"),("all files","*.*")))
	try:
		set_text(importEntry, root.importFile)		
	except Exception as e:
		pass

def setExportLocation():
	root.exportDestination =  filedialog.askdirectory(title = "Select Destination Directory")
	try:
		set_text(exportEntry, root.exportDestination)		
	except Exception as e:
		pass


def showEntryFields():
	print("Import: %s\nExport: %s" % (importEntry.get(), exportEntry.get()))

def set_text(e, text):
    e.delete(0,tk.END)
    e.insert(0,text)
    return


root = tk.Tk()
root.title("ComSeg")

tk.Label(root, text="Import file").grid(row=0)
tk.Label(root, text="Export location").grid(row=1)

importEntry = tk.Entry(root)
exportEntry = tk.Entry(root)

importEntry.grid(row=0, column=1, ipadx="100")
exportEntry.grid(row=1, column=1, ipadx="100")

tk.Button(root, text='...', command=setImportFile).grid(row=0, column=3, sticky=tk.W, pady=4, padx=10, ipadx=10)
tk.Button(root, text='...', command=setExportLocation).grid(row=1, column=3, sticky=tk.W, pady=4,padx=10, ipadx=10)

tk.Button(root, text='Quit', command=root.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(root, text='Show', command=showEntryFields).grid(row=3, column=1, sticky=tk.W, pady=4)

tk.mainloop()