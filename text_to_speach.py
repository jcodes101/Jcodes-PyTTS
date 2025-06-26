import tkinter as tk
from tkinter import *
import pyttsx3

# speak function
engine = pyttsx3.init()
def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

# new application window creation
root = Tk()

# variable set to take in text as a tring
textv = StringVar()

# frame added on top of window
obj = LabelFrame(root, text="Text to speech", font=20, bd=1)
obj.pack(fill="both", expand="yes", padx=10, pady=10)

# label for entering text
txtBox = Label(obj, text="Enter text:", font=30)
txtBox.pack(side=tk.LEFT, padx=5)

# input box for text
textEntry = Entry(obj, textvariable=textv, font=30, width=20, bd=5)
textEntry.pack(side=tk.LEFT, padx=10)

btn = Button(obj, text="Speak", font=20, bg="black", fg="white", command=speaknow)
btn.pack(side=tk.LEFT, padx=10)

# window customization
root.title("Jcodes Text to Speech App")
root.geometry("500x300")
root.resizable(False, False)
root.mainloop()

