from Tkinter import *
import os

root = Tk()
root.title("Text2Speech")
T = Text(root, height=5, width=30)
T.pack()

def speak():
    os.system("say " + T.get("1.0",END))

B = Button(root, text ="Speak", command = speak)
B.pack()
T.insert(END, "Text Here will be spoken!")
mainloop()
