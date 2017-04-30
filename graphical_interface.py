from tkinter import *
import os, tkinter.filedialog, tkinter.ttk, tkinter.simpledialog, tkinter.messagebox

backgroundColor = "#a5ba8d"

root = Tk()
root.wm_title("")

root.configure(bg=backgroundColor)
root.resizable(0,0)
message = StringVar()


topFrame = Frame(root)
topFrame.configure(bg=backgroundColor)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.configure(bg=backgroundColor)
bottomFrame.pack(side=BOTTOM)

title_opt = {'padx': 50, 'pady': 30}
button1_opt = {'pady': 30}
pb_opt = {'pady': 45}


def runSimulator():
    print("Main Application Started")
    os.system("python3 main.py")



def selectIndividuals():
    print("Dummy Button Pushed")
    #Implement


title = Label(topFrame, text="Ecosystems Evolution", fg="#f2edd0", background=backgroundColor, font=("Helvetica", 26))
title.pack(title_opt)

runButton = Button(root, text='Start Simulation',  highlightbackground=backgroundColor, command=runSimulator)
runButton.pack(button1_opt)

openButton = Button(root, text='Select Specimens', highlightbackground=backgroundColor, command=selectIndividuals)
openButton.pack(pb_opt)


root.mainloop()
